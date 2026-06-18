import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import pymysql
import requests


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load_local_env():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_local_env()

BASE_URL = os.environ.get("LMS_BASE_URL", "http://127.0.0.1:5000")
OUT_PATH = ROOT / "LMS_Non_Functional_Test_Results.json"
TESTER = "Yong Di Lun"
KNOWN_HASH = "025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8"

DB_CONFIG = {
    "host": os.environ.get("MYSQL_DATABASE_HOST", "localhost"),
    "user": os.environ.get("MYSQL_DATABASE_USER", "root"),
    "password": os.environ.get("MYSQL_DATABASE_PASSWORD", ""),
    "database": os.environ.get("MYSQL_DATABASE_DB", "lms"),
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True,
}


NFR_CASES = {
    "TC-Q001": {
        "requirement_id": "REQ_Q001",
        "procedure_id": "TP-Q-001",
        "objective": "Verify 100% transactional accuracy for concurrent book reservations",
        "expected": "Only one user can reserve the final available copy of a book; no double booking and no negative count can occur.",
    },
    "TC-Q002": {
        "requirement_id": "REQ_Q002",
        "procedure_id": "TP-Q-002",
        "objective": "Verify database foreign key integrity between User, Book, and Reservation tables",
        "expected": "Database rejects orphaned Reservation records and defines foreign key constraints for user_id and book_id.",
    },
    "TC-Q003": {
        "requirement_id": "REQ_Q003",
        "procedure_id": "TP-Q-003",
        "objective": "Verify secure password hashing and salting before database storage",
        "expected": "Passwords are not stored in plain text and each password hash uses a secure salted algorithm such as bcrypt.",
    },
    "TC-Q004": {
        "requirement_id": "REQ_Q004",
        "procedure_id": "TP-Q-004",
        "objective": "Verify HTTPS/TLS 1.2 or higher production deployment readiness is documented and configurable",
        "expected": "Production deployment guidance requires HTTPS/TLS 1.2 or higher and the application exposes secure-cookie configuration for HTTPS environments.",
    },
}


def connect_db():
    return pymysql.connect(**DB_CONFIG)


def execute(sql, params=None):
    with connect_db() as conn:
        with conn.cursor() as cur:
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
            return cur.lastrowid


def fetchone(sql, params=None):
    with connect_db() as conn:
        with conn.cursor() as cur:
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
            return cur.fetchone()


def fetchall(sql, params=None):
    with connect_db() as conn:
        with conn.cursor() as cur:
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
            return cur.fetchall()


def cleanup():
    execute(
        """
        DELETE FROM reserve
        WHERE user_id IN (SELECT id FROM users WHERE email LIKE 'nfr_%@example.test')
           OR book_id IN (SELECT id FROM books WHERE name LIKE 'NFR Test %%')
        """
    )
    execute("DELETE FROM users WHERE email LIKE 'nfr_%@example.test'")
    execute("DELETE FROM books WHERE name LIKE 'NFR Test %%'")


def ensure_user(email, name):
    execute(
        "INSERT INTO users (name, email, password, bio, mob, `lock`) VALUES (%s, %s, %s, '', '', 0)",
        (name, email, KNOWN_HASH),
    )
    return fetchone("SELECT id FROM users WHERE email=%s", (email,))["id"]


def ensure_book(name, count=1, availability=1):
    execute(
        "INSERT INTO books (name, `desc`, author, availability, edition, count) VALUES (%s, %s, %s, %s, '1', %s)",
        (name, "NFR automated test book", "NFR Author", availability, count),
    )
    return fetchone("SELECT id FROM books WHERE name=%s ORDER BY id DESC LIMIT 1", (name,))["id"]


def server_alive():
    try:
        return requests.get(BASE_URL + "/", timeout=3).status_code < 500
    except requests.RequestException:
        return False


def ensure_server():
    if server_alive():
        return None
    env = os.environ.copy()
    env["FLASK_APP"] = "app.py"
    process = subprocess.Popen(
        [sys.executable, "-m", "flask", "run", "--host", "127.0.0.1", "--port", "5000"],
        cwd=str(ROOT),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for _ in range(30):
        if server_alive():
            return process
        time.sleep(1)
    raise RuntimeError("LMS server did not become reachable")


def login_session(email):
    session = requests.Session()
    response = session.post(BASE_URL + "/signin", data={"email": email, "password": "password"}, timeout=10)
    return session, response


def record(case_id, passed, actual, evidence, tool):
    case = NFR_CASES[case_id]
    return {
        "requirement_id": case["requirement_id"],
        "test_design_id": "TDS-QA-NFR",
        "test_case_id": case_id,
        "test_procedure_id": case["procedure_id"],
        "type_of_testing": "Non-Functional Testing",
        "tool": tool,
        "pass_fail": "Pass" if passed else "Fail",
        "incident_id": "-" if passed else "",
        "objective": case["objective"],
        "expected": case["expected"],
        "actual": actual,
        "remark": evidence,
    }


def compact_actual(row):
    actual = row["actual"].replace("\n", " ")
    case_id = row["test_case_id"]
    if case_id == "TC-Q001":
        return actual
    if case_id == "TC-Q002":
        return "Foreign keys enforced; orphan reservation rejected." if row["pass_fail"] == "Pass" else "Foreign keys missing or orphan reservation was accepted."
    if case_id == "TC-Q003":
        parts = [part.strip() for part in actual.split(";") if "Stored hashes" not in part]
        return "; ".join(parts).strip()
    if case_id == "TC-Q004":
        return actual
    return actual


def print_console_report(summary, rows):
    print()
    print("LMS Non-Functional Requirement Tests")
    print("=" * 80)
    print(f"Base URL     : {BASE_URL}")
    print(f"Result file  : {OUT_PATH}")
    print(
        "Summary      : "
        f"{summary['pass']}/{summary['total']} passed, "
        f"{summary['fail']} failed, "
        f"{summary['not_executed']} not executed"
    )
    print()
    print(f"{'Test Case':<10} {'Requirement':<10} {'Result':<6} Finding")
    print("-" * 80)
    for row in rows:
        finding = compact_actual(row)
        if len(finding) > 95:
            finding = finding[:92] + "..."
        print(f"{row['test_case_id']:<10} {row['requirement_id']:<10} {row['pass_fail']:<6} {finding}")
    print()
    print("Note         : Full evidence and raw values are saved in the JSON result file.")
    print()


def test_concurrent_reservation():
    cleanup()
    user_a = ensure_user("nfr_concurrent_a@example.test", "NFR Concurrent A")
    user_b = ensure_user("nfr_concurrent_b@example.test", "NFR Concurrent B")
    book_id = ensure_book("NFR Test Concurrent Single Copy", count=1)
    session_a, _ = login_session("nfr_concurrent_a@example.test")
    session_b, _ = login_session("nfr_concurrent_b@example.test")

    def reserve(session):
        return session.get(BASE_URL + f"/books/add/{book_id}", timeout=20).status_code

    with ThreadPoolExecutor(max_workers=2) as executor:
        statuses = list(executor.map(reserve, [session_a, session_b]))

    reserved = fetchone("SELECT COUNT(*) AS c FROM reserve WHERE book_id=%s", (book_id,))["c"]
    count_left = fetchone("SELECT count FROM books WHERE id=%s", (book_id,))["count"]
    passed = reserved == 1 and count_left == 0
    actual = f"HTTP statuses = {statuses}; reservations created = {reserved}; book count after test = {count_left}."
    evidence = "Concurrent reservation route was executed by two authenticated users against one available physical copy."
    return record("TC-Q001", passed, actual, evidence, "Postman/HTTP")


def test_foreign_keys():
    cleanup()
    book_id = ensure_book("NFR Test FK Valid Book", count=1)
    fk_rows = fetchall(
        """
        SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE()
          AND TABLE_NAME = 'reserve'
          AND REFERENCED_TABLE_NAME IS NOT NULL
        """
    )
    insert_succeeded = False
    orphan_id = None
    try:
        orphan_id = execute("INSERT INTO reserve (user_id, book_id) VALUES (%s, %s)", (999999, book_id))
        insert_succeeded = True
    except Exception:
        insert_succeeded = False
    finally:
        if orphan_id:
            execute("DELETE FROM reserve WHERE id=%s", (orphan_id,))
    has_user_fk = any(row["COLUMN_NAME"] == "user_id" and row["REFERENCED_TABLE_NAME"] == "users" for row in fk_rows)
    has_book_fk = any(row["COLUMN_NAME"] == "book_id" and row["REFERENCED_TABLE_NAME"] == "books" for row in fk_rows)
    passed = has_user_fk and has_book_fk and not insert_succeeded
    actual = f"Foreign keys found = {fk_rows}; orphan reservation insert succeeded = {insert_succeeded}."
    evidence = "Database metadata and orphan reservation insertion were checked against the live lms database."
    return record("TC-Q002", passed, actual, evidence, "Postman/HTTP")


def test_password_hashing():
    cleanup()
    requests.post(
        BASE_URL + "/signup",
        data={"name": "NFR Password A", "email": "nfr_password_a@example.test", "password": "password"},
        timeout=10,
    )
    requests.post(
        BASE_URL + "/signup",
        data={"name": "NFR Password B", "email": "nfr_password_b@example.test", "password": "password"},
        timeout=10,
    )
    rows = fetchall("SELECT email,password FROM users WHERE email LIKE 'nfr_password_%@example.test' ORDER BY email")
    hashes = [row["password"] for row in rows]
    plaintext_absent = all(row["password"] not in {"password", "password-a", "password-b"} for row in rows)
    secure_salted_algorithm = all(
        h.startswith("pbkdf2:") or h.startswith("scrypt:") or h.startswith("$2a$") or h.startswith("$2b$") or h.startswith("$2y$")
        for h in hashes
    )
    unique_hashes = len(set(hashes)) == len(hashes)
    passed = len(rows) == 2 and plaintext_absent and secure_salted_algorithm and unique_hashes
    actual = f"Stored hashes = {hashes}; plaintext absent = {plaintext_absent}; secure salted algorithm = {secure_salted_algorithm}; unique hashes = {unique_hashes}."
    evidence = "Password storage was inspected in the live users table for secure salted hashing behavior."
    return record("TC-Q003", passed, actual, evidence, "Postman/HTTP")


def test_https_tls():
    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
    app_py = (ROOT / "app.py").read_text(encoding="utf-8", errors="replace")
    env_example = (ROOT / ".env.example").read_text(encoding="utf-8", errors="replace")

    mentions_https = "HTTPS" in readme and "TLS 1.2" in readme
    mentions_reverse_proxy = any(term in readme for term in ["reverse proxy", "Nginx", "Apache", "IIS"])
    secure_cookie_configured = "SESSION_COOKIE_SECURE" in app_py and "SESSION_COOKIE_SECURE" in env_example
    production_true_documented = "SESSION_COOKIE_SECURE=true" in readme and "SESSION_COOKIE_SECURE=true" in env_example

    passed = mentions_https and mentions_reverse_proxy and secure_cookie_configured and production_true_documented
    actual = (
        f"HTTPS/TLS 1.2 guidance documented = {mentions_https}; "
        f"reverse proxy/deployment guidance documented = {mentions_reverse_proxy}; "
        f"SESSION_COOKIE_SECURE configurable = {secure_cookie_configured}; "
        f"production secure-cookie value documented = {production_true_documented}."
    )
    evidence = "README.md, .env.example, and app.py were inspected for production HTTPS/TLS readiness and secure cookie configuration."
    return record("TC-Q004", passed, actual, evidence, "Postman/HTTP")


def main():
    process = None
    start = datetime.now()
    rows = []
    try:
        process = ensure_server()
        rows = [
            test_concurrent_reservation(),
            test_foreign_keys(),
            test_password_hashing(),
            test_https_tls(),
        ]
    finally:
        cleanup()
        if process:
            process.terminate()
            process.wait(timeout=10)
    incident_counter = 29
    for row in rows:
        if row["pass_fail"] == "Fail":
            row["incident_id"] = f"LMS_TIR_1.0/TIR-{incident_counter:03d}"
            incident_counter += 1
    summary = {
        "total": len(rows),
        "pass": sum(1 for r in rows if r["pass_fail"] == "Pass"),
        "fail": sum(1 for r in rows if r["pass_fail"] == "Fail"),
        "not_executed": 0,
    }
    payload = {
        "tester": TESTER,
        "start_time": start.isoformat(timespec="seconds"),
        "end_time": datetime.now().isoformat(timespec="seconds"),
        "results": rows,
        "summary": summary,
    }
    OUT_PATH.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print_console_report(summary, rows)


if __name__ == "__main__":
    main()
