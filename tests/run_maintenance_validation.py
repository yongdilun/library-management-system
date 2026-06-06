import json
import os
from datetime import datetime
from pathlib import Path

import pymysql
import requests


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "reports" / "maintenance_evidence"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "maintenance_validation_results.json"


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
DB_CONFIG = {
    "host": os.environ.get("MYSQL_DATABASE_HOST", "localhost"),
    "user": os.environ.get("MYSQL_DATABASE_USER", "root"),
    "password": os.environ.get("MYSQL_DATABASE_PASSWORD", ""),
    "database": os.environ.get("MYSQL_DATABASE_DB", "lms"),
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True,
}

LEGACY_HASH = "025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8"


def db_execute(sql, params=None):
    with pymysql.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur


def scalar(sql, params=None):
    cur = db_execute(sql, params)
    row = cur.fetchone()
    if not row:
        return None
    return next(iter(row.values()))


def fetchone(sql, params=None):
    cur = db_execute(sql, params)
    return cur.fetchone()


def admin_session():
    session = requests.Session()
    session.post(
        BASE_URL + "/admin/signin/",
        data={"email": "hamza@gmail.com", "password": "password"},
        timeout=10,
    )
    return session


def record(case_id, objective, passed, evidence):
    return {
        "case_id": case_id,
        "objective": objective,
        "result": "Pass" if passed else "Fail",
        "evidence": evidence,
    }


def main():
    results = []
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    title = f"Maintenance Validation Book {stamp}"
    duplicate_title = f"Maintenance Duplicate Book {stamp}"
    delete_title = f"Maintenance Delete Book {stamp}"
    reserve_email = f"maintenance_reserve_{stamp}@example.test"
    limit_email = f"maintenance_limit_{stamp}@example.test"

    wrong_login = requests.post(
        BASE_URL + "/signin",
        data={"email": "hamza@gmail.com", "password": "wrong-password"},
        timeout=10,
    )
    results.append(
        record(
            "MV-SEC-001",
            "Wrong password is rejected after secure password verification change",
            "Email or password incorrect" in wrong_login.text and "/signin" in wrong_login.url,
            f"URL={wrong_login.url}; contains_error={'Email or password incorrect' in wrong_login.text}",
        )
    )

    signup_empty = requests.post(
        BASE_URL + "/signup",
        data={"name": "", "email": "", "password": ""},
        timeout=10,
    )
    results.append(
        record(
            "MV-VAL-002",
            "Signup empty-field validation returns a clear error",
            "All fields are required" in signup_empty.text,
            f"contains_required_message={'All fields are required' in signup_empty.text}",
        )
    )

    signup_invalid_email = requests.post(
        BASE_URL + "/signup",
        data={"name": "Validation User", "email": "invalid-email", "password": "password"},
        timeout=10,
    )
    results.append(
        record(
            "MV-VAL-003",
            "Signup invalid email is rejected by server-side validation",
            "valid email" in signup_invalid_email.text.lower(),
            f"contains_email_message={'valid email' in signup_invalid_email.text.lower()}",
        )
    )

    user = requests.Session()
    user.post(BASE_URL + "/signin", data={"email": "hamza@gmail.com", "password": "password"}, timeout=10)
    profile_empty_name = user.post(
        BASE_URL + "/user",
        data={"name": "", "email": "hamza@gmail.com", "password": "", "bio": "Profile validation evidence"},
        timeout=10,
    )
    results.append(
        record(
            "MV-VAL-004",
            "Profile empty-name validation blocks invalid update",
            "Name is required" in profile_empty_name.text,
            f"contains_name_error={'Name is required' in profile_empty_name.text}",
        )
    )

    admin = admin_session()
    db_execute("DELETE FROM books WHERE name=%s", (title,))
    db_execute("DELETE FROM books WHERE name IN (%s, %s)", (duplicate_title, delete_title))
    add_response = admin.post(
        BASE_URL + "/admin/books/add",
        data={
            "title": title,
            "author": "Yong Di Lun",
            "edition": "1",
            "qty": "2",
            "available": "on",
            "desc": "Maintenance validation evidence book.",
        },
        timeout=10,
        allow_redirects=True,
    )
    inserted_count = scalar("SELECT COUNT(*) FROM books WHERE name=%s", (title,))
    results.append(
        record(
            "MV-ADM-001",
            "Admin Add Book persists a valid book record",
            inserted_count == 1 and "Book added successfully" in add_response.text,
            f"inserted_count={inserted_count}; success_message={'Book added successfully' in add_response.text}",
        )
    )

    book_id = scalar("SELECT id FROM books WHERE name=%s", (title,))
    edit_response = admin.post(
        BASE_URL + f"/admin/books/edit/{book_id}",
        data={
            "title": title + " Updated",
            "author": "Yong Di Lun",
            "edition": "2",
            "qty": "3",
            "available": "on",
            "desc": "Updated maintenance validation evidence book.",
        },
        timeout=10,
        allow_redirects=True,
    )
    updated_count = scalar("SELECT COUNT(*) FROM books WHERE name=%s AND edition='2' AND count=3", (title + " Updated",))
    results.append(
        record(
            "MV-ADM-002",
            "Admin Edit Book updates persisted book data",
            updated_count == 1 and "Book updated successfully" in edit_response.text,
            f"updated_count={updated_count}; success_message={'Book updated successfully' in edit_response.text}",
        )
    )

    missing_desc = admin.post(
        BASE_URL + "/admin/books/add",
        data={
            "title": f"Maintenance Missing Description {stamp}",
            "author": "Yong Di Lun",
            "edition": "1",
            "qty": "1",
            "available": "on",
        },
        timeout=10,
    )
    results.append(
        record(
            "MV-ADM-003",
            "Admin Add Book missing-description validation is shown",
            "Description is required" in missing_desc.text,
            f"contains_description_error={'Description is required' in missing_desc.text}",
        )
    )

    db_execute(
        "INSERT INTO books (name, `desc`, author, availability, edition, count) VALUES (%s, %s, %s, 1, '1', 1)",
        (duplicate_title, "Duplicate validation fixture.", "Yong Di Lun"),
    )
    duplicate_response = admin.post(
        BASE_URL + "/admin/books/add",
        data={
            "title": duplicate_title,
            "author": "Yong Di Lun",
            "edition": "1",
            "qty": "1",
            "available": "on",
            "desc": "Duplicate validation fixture.",
        },
        timeout=10,
    )
    results.append(
        record(
            "MV-ADM-004",
            "Admin Add Book duplicate-title validation is shown",
            "already exists" in duplicate_response.text,
            f"contains_duplicate_error={'already exists' in duplicate_response.text}",
        )
    )

    db_execute(
        "INSERT INTO books (name, `desc`, author, availability, edition, count) VALUES (%s, %s, %s, 1, '1', 1)",
        (delete_title, "Delete workflow fixture.", "Yong Di Lun"),
    )
    delete_book_id = scalar("SELECT id FROM books WHERE name=%s ORDER BY id DESC LIMIT 1", (delete_title,))
    delete_response = admin.get(BASE_URL + f"/admin/books/delete/{delete_book_id}", timeout=10, allow_redirects=True)
    deleted_count = scalar("SELECT COUNT(*) FROM books WHERE id=%s", (delete_book_id,))
    results.append(
        record(
            "MV-ADM-005",
            "Admin Delete Book removes a selected record",
            deleted_count == 0 and "Book deleted successfully" in delete_response.text,
            f"deleted_count={deleted_count}; success_message={'Book deleted successfully' in delete_response.text}",
        )
    )

    admin_books_page = admin.get(BASE_URL + "/admin/books/", timeout=10)
    results.append(
        record(
            "MV-ADM-006",
            "Admin Delete Book link includes explicit confirmation text",
            "confirm(" in admin_books_page.text and "Cancel" in admin_books_page.text,
            f"has_confirm={'confirm(' in admin_books_page.text}; has_cancel={'Cancel' in admin_books_page.text}",
        )
    )

    search_response = requests.get(BASE_URL + "/books/search", params={"keyword": ""}, timeout=10)
    results.append(
        record(
            "MV-VAL-001",
            "Empty search keyword shows validation message",
            "Please enter a search keyword" in search_response.text,
            f"contains_validation_message={'Please enter a search keyword' in search_response.text}",
        )
    )

    db_execute("DELETE FROM users WHERE email IN (%s, %s)", (reserve_email, limit_email))
    db_execute(
        "INSERT INTO users (name, email, password, bio, mob, `lock`) VALUES (%s, %s, %s, %s, '', 0)",
        ("Maintenance Reserve User", reserve_email, LEGACY_HASH, "Reservation validation user."),
    )
    reserve_user_id = scalar("SELECT id FROM users WHERE email=%s", (reserve_email,))
    db_execute(
        "INSERT INTO books (name, `desc`, author, availability, edition, count) VALUES (%s, %s, %s, 1, '1', 3)",
        (f"Maintenance Duplicate Reserve {stamp}", "Duplicate reserve fixture.", "Yong Di Lun"),
    )
    reserve_book_id = scalar("SELECT id FROM books WHERE name=%s", (f"Maintenance Duplicate Reserve {stamp}",))
    reserve_session = requests.Session()
    reserve_session.post(BASE_URL + "/signin", data={"email": reserve_email, "password": "password"}, timeout=10)
    reserve_session.get(BASE_URL + f"/books/add/{reserve_book_id}", timeout=10)
    duplicate_reserve = reserve_session.get(BASE_URL + f"/books/add/{reserve_book_id}", timeout=10)
    reserve_count = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (reserve_user_id, reserve_book_id),
    )
    results.append(
        record(
            "MV-RES-001",
            "Duplicate reservation attempt is blocked",
            reserve_count == 1 and "already reserved" in duplicate_reserve.text,
            f"reserve_count={reserve_count}; duplicate_message={'already reserved' in duplicate_reserve.text}",
        )
    )

    db_execute(
        "INSERT INTO users (name, email, password, bio, mob, `lock`) VALUES (%s, %s, %s, %s, '', 0)",
        ("Maintenance Limit User", limit_email, LEGACY_HASH, "Reservation limit validation user."),
    )
    limit_user_id = scalar("SELECT id FROM users WHERE email=%s", (limit_email,))
    for idx in range(5):
        book_name = f"Maintenance Limit Existing {stamp} {idx}"
        db_execute(
            "INSERT INTO books (name, `desc`, author, availability, edition, count) VALUES (%s, %s, %s, 1, '1', 1)",
            (book_name, "Reservation limit existing fixture.", "Yong Di Lun"),
        )
        existing_book_id = scalar("SELECT id FROM books WHERE name=%s", (book_name,))
        db_execute("INSERT INTO reserve (user_id, book_id) VALUES (%s, %s)", (limit_user_id, existing_book_id))
    target_limit_name = f"Maintenance Limit Target {stamp}"
    db_execute(
        "INSERT INTO books (name, `desc`, author, availability, edition, count) VALUES (%s, %s, %s, 1, '1', 2)",
        (target_limit_name, "Reservation limit target fixture.", "Yong Di Lun"),
    )
    target_limit_book_id = scalar("SELECT id FROM books WHERE name=%s", (target_limit_name,))
    limit_session = requests.Session()
    limit_session.post(BASE_URL + "/signin", data={"email": limit_email, "password": "password"}, timeout=10)
    limit_response = limit_session.get(BASE_URL + f"/books/add/{target_limit_book_id}", timeout=10)
    limit_target_count = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (limit_user_id, target_limit_book_id),
    )
    results.append(
        record(
            "MV-RES-002",
            "Reservation limit prevents a sixth active reservation",
            limit_target_count == 0 and "limit" in limit_response.text.lower(),
            f"target_reserve_count={limit_target_count}; limit_message={'limit' in limit_response.text.lower()}",
        )
    )

    migration_path = ROOT / "db" / "migrations" / "001_reservation_integrity.sql"
    migration_text = migration_path.read_text(encoding="utf-8") if migration_path.exists() else ""
    results.append(
        record(
            "MV-DB-001",
            "Database migration defines reservation foreign keys and duplicate prevention",
            "fk_reserve_user" in migration_text and "uniq_user_book_reservation" in migration_text,
            f"migration_file={migration_path}; has_fk={'fk_reserve_user' in migration_text}; has_unique={'uniq_user_book_reservation' in migration_text}",
        )
    )

    if book_id:
        db_execute("DELETE FROM books WHERE id=%s OR name=%s", (book_id, title + " Updated"))
    db_execute("DELETE FROM reserve WHERE user_id IN (SELECT id FROM users WHERE email IN (%s, %s))", (reserve_email, limit_email))
    db_execute("DELETE FROM users WHERE email IN (%s, %s)", (reserve_email, limit_email))
    db_execute("DELETE FROM books WHERE name LIKE %s", (f"Maintenance%{stamp}%",))
    db_execute("DELETE FROM books WHERE name=%s", (duplicate_title,))

    payload = {
        "executed_at": datetime.now().isoformat(timespec="seconds"),
        "base_url": BASE_URL,
        "summary": {
            "total": len(results),
            "pass": sum(1 for item in results if item["result"] == "Pass"),
            "fail": sum(1 for item in results if item["result"] == "Fail"),
        },
        "results": results,
    }
    OUT_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    print(f"Created {OUT_PATH}")


if __name__ == "__main__":
    main()
