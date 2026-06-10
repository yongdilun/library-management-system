import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import pymysql
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
OUT_PATH = ROOT / "LMS_Test_Log_Results.json"
TESTER = "Yong Di Lun"

DB_CONFIG = {
    "host": os.environ.get("MYSQL_DATABASE_HOST", "localhost"),
    "user": os.environ.get("MYSQL_DATABASE_USER", "root"),
    "password": os.environ.get("MYSQL_DATABASE_PASSWORD", ""),
    "database": os.environ.get("MYSQL_DATABASE_DB", "lms"),
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True,
}

KNOWN_HASH = "025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8"

CASE_PROCEDURES = {
    "TC-01-001": "TP-01-001",
    "TC-01-002": "TP-01-001",
    "TC-01-003": "TP-01-001",
    "TC-01-004": "TP-01-002",
    "TC-02-001": "TP-02-001",
    "TC-02-002": "TP-02-002",
    "TC-02-003": "TP-02-002",
    "TC-02-004": "TP-02-002",
    "TC-03-001": "TP-03-001",
    "TC-03-002": "TP-03-002",
    "TC-03-003": "TP-03-002",
    "TC-04-001": "TP-04-001",
    "TC-04-002": "TP-04-002",
    "TC-04-003": "TP-04-002",
    "TC-04-004": "TP-04-002",
    "TC-04-005": "TP-04-003",
    "TC-05-001": "TP-05-001",
    "TC-05-002": "TP-05-002",
    "TC-05-003": "TP-05-001",
    "TC-05-004": "TP-05-002",
    "TC-06-001": "TP-06-001",
    "TC-06-002": "TP-06-003",
    "TC-06-003": "TP-06-001",
    "TC-06-004": "TP-06-002",
    "TC-06-005": "TP-06-003",
    "TC-07-001": "TP-07-001",
    "TC-07-002": "TP-07-002",
    "TC-07-003": "TP-07-003",
    "TC-07-004": "TP-07-003",
    "TC-07-005": "TP-07-001",
    "TC-07-006": "TP-07-002",
    "TC-08-001": "TP-08-001",
    "TC-08-002": "TP-08-002",
    "TC-08-003": "TP-08-003",
    "TC-08-004": "TP-08-002",
    "TC-08-005": "TP-08-003",
    "TC-09-001": "TP-09-001",
    "TC-09-002": "TP-09-002",
    "TC-09-003": "TP-09-003",
    "TC-09-004": "TP-09-001",
    "TC-09-005": "TP-09-002",
    "TC-10-001": "TP-10-001",
    "TC-10-002": "TP-10-002",
    "TC-10-003": "TP-10-002",
    "TC-10-004": "TP-10-003",
    "TC-10-005": "TP-10-003",
    "TC-10-006": "TP-10-003",
    "TC-10-007": "TP-10-002",
    "TC-10-008": "TP-10-002",
    "TC-10-009": "TP-10-001",
    "TC-11-001": "TP-11-001",
    "TC-11-002": "TP-11-003",
    "TC-11-003": "TP-11-003",
    "TC-11-004": "TP-11-004",
    "TC-11-005": "TP-11-001",
    "TC-11-006": "TP-11-002",
    "TC-11-007": "TP-11-001",
    "TC-11-008": "TP-11-003",
    "TC-12-001": "TP-12-001",
    "TC-12-002": "TP-12-002",
    "TC-12-003": "TP-12-003",
    "TC-12-004": "TP-12-003",
    "TC-12-005": "TP-12-004",
    "TC-12-006": "TP-12-004",
    "TC-12-007": "TP-12-001",
    "TC-12-008": "TP-12-005",
    "TC-12-009": "TP-12-003",
    "TC-12-010": "TP-12-001",
}


def feature_id(case_id):
    num = int(case_id.split("-")[1])
    return f"F{num:03d}" if num < 10 else f"F00{num}"


def test_design_id(case_id):
    num = int(case_id.split("-")[1])
    return f"TDS-2.3.{num}"


def connect_db():
    return pymysql.connect(**DB_CONFIG)


def scalar(sql, params=None):
    with connect_db() as conn:
        with conn.cursor() as cur:
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
            row = cur.fetchone()
            if not row:
                return None
            return next(iter(row.values()))


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


def execute(sql, params=None):
    with connect_db() as conn:
        with conn.cursor() as cur:
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
            return cur.lastrowid


def cleanup_test_data():
    execute(
        """
        DELETE FROM reserve
        WHERE user_id IN (SELECT id FROM users WHERE email LIKE 'svv_%@example.test')
           OR book_id IN (SELECT id FROM books WHERE name LIKE 'SVV Test %%')
        """
    )
    execute("DELETE FROM users WHERE email LIKE 'svv_%@example.test'")
    execute("DELETE FROM books WHERE name LIKE 'SVV Test %%'")


def ensure_user(email, name="SVV Test User", bio="SVV test account"):
    execute(
        """
        INSERT INTO users (name, email, password, bio, mob, `lock`)
        VALUES (%s, %s, %s, %s, '', 0)
        ON DUPLICATE KEY UPDATE name=VALUES(name), password=VALUES(password), bio=VALUES(bio), mob='', `lock`=0
        """,
        (name, email, KNOWN_HASH, bio),
    )
    row = fetchone("SELECT id FROM users WHERE email=%s", (email,))
    return row["id"]


def ensure_book(name, count=3, availability=1, author="SVV Author", desc="SVV automated test book"):
    execute(
        """
        INSERT INTO books (name, `desc`, author, availability, edition, count)
        VALUES (%s, %s, %s, %s, '1', %s)
        """,
        (name, desc, author, availability, count),
    )
    return scalar("SELECT id FROM books WHERE name=%s ORDER BY id DESC LIMIT 1", (name,))


def ensure_reserve(user_id, book_id):
    execute("INSERT INTO reserve (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))


def setup_data():
    cleanup_test_data()
    data = {
        "user_id": ensure_user("svv_user@example.test", "SVV User"),
        "profile_user_id": ensure_user("svv_profile@example.test", "SVV Profile"),
        "duplicate_user_id": ensure_user("svv_duplicate@example.test", "SVV Duplicate"),
        "reserved_user_id": ensure_user("svv_reserved@example.test", "SVV Reserved"),
        "empty_user_id": ensure_user("svv_empty@example.test", "SVV Empty"),
        "limit_user_id": ensure_user("svv_limit@example.test", "SVV Limit"),
    }
    data["available_book_id"] = ensure_book("SVV Test Book Available", count=4)
    data["search_book_id"] = ensure_book("SVV Test Harry Potter Automation", count=2, desc="Harry Potter search fixture")
    data["unavailable_book_id"] = ensure_book("SVV Test Book Unavailable", count=0)
    data["reserved_book_id"] = ensure_book("SVV Test Book Reserved", count=5)
    data["limit_book_id"] = ensure_book("SVV Test Book Limit Target", count=5)
    data["duplicate_reserve_book_id"] = ensure_book("SVV Test Book Duplicate Reserve", count=5)
    for i in range(5):
        b_id = ensure_book(f"SVV Test Limit Existing {i + 1}", count=1)
        ensure_reserve(data["limit_user_id"], b_id)
    ensure_reserve(data["reserved_user_id"], data["reserved_book_id"])
    ensure_reserve(data["user_id"], data["duplicate_reserve_book_id"])
    return data


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
    raise RuntimeError("LMS server did not become reachable on http://127.0.0.1:5000")


def make_driver():
    opts = Options()
    opts.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--window-size=1366,900")
    return webdriver.Chrome(options=opts)


def page(driver, path):
    driver.get(BASE_URL + path)
    time.sleep(0.2)


def fill(driver, name, value):
    elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, name)))
    try:
        elem.clear()
        elem.send_keys(value)
    except ElementNotInteractableException:
        driver.execute_script(
            """
            const el = arguments[0];
            const value = arguments[1];
            el.value = value;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            elem,
            value,
        )


def form_valid(driver):
    return driver.execute_script("return document.querySelector('form').checkValidity();")


def click_submit(driver):
    button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    try:
        button.click()
    except (ElementClickInterceptedException, ElementNotInteractableException):
        driver.execute_script("arguments[0].click();", button)
    time.sleep(0.35)


def source_has(driver, *terms):
    source = driver.page_source
    return all(term in source for term in terms)


def login_user(driver, email="svv_user@example.test", password="password"):
    driver.delete_all_cookies()
    page(driver, "/signin")
    fill(driver, "email", email)
    fill(driver, "password", password)
    click_submit(driver)
    time.sleep(0.4)


def login_admin(driver, password="password"):
    driver.delete_all_cookies()
    page(driver, "/admin/signin/")
    fill(driver, "email", "hamza@gmail.com")
    fill(driver, "password", password)
    click_submit(driver)
    time.sleep(0.6)


def open_admin_page(driver, path):
    page(driver, path)
    if "/admin/signin" in driver.current_url or "ADMIN SIGNIN" in driver.page_source:
        login_admin(driver)
        page(driver, path)


def req_session_user(email="svv_user@example.test", password="password"):
    s = requests.Session()
    s.post(BASE_URL + "/signin", data={"email": email, "password": password}, timeout=10)
    return s


def req_session_admin(password="password"):
    s = requests.Session()
    s.post(BASE_URL + "/admin/signin/", data={"email": "hamza@gmail.com", "password": password}, timeout=10)
    return s


def simulated_failure_response(route_path, target_module_name, manager_name, method_name, session_key=None):
    import importlib

    import werkzeug

    if not hasattr(werkzeug, "__version__"):
        werkzeug.__version__ = "3"

    from app import app as flask_app

    target_module = importlib.import_module(target_module_name)
    manager = getattr(target_module, manager_name)
    original = getattr(manager, method_name)
    original_propagate = flask_app.config.get("PROPAGATE_EXCEPTIONS")

    def raise_db_failure(*args, **kwargs):
        raise RuntimeError("Simulated database failure for test procedure execution")

    setattr(manager, method_name, raise_db_failure)
    flask_app.config["PROPAGATE_EXCEPTIONS"] = False
    try:
        with flask_app.test_client() as client:
            if session_key:
                with client.session_transaction() as sess:
                    sess[session_key] = 1
            return client.get(route_path)
    finally:
        setattr(manager, method_name, original)
        flask_app.config["PROPAGATE_EXCEPTIONS"] = original_propagate


class Recorder:
    def __init__(self):
        self.rows = []
        self.incident = 1

    def add(self, case_id, passed, tool, remark="-", not_executed=False):
        if not_executed:
            status = "Not Executed"
        else:
            status = "Pass" if passed else "Fail"
        incident = "-"
        if status == "Fail":
            incident = f"LMS_TIR_1.0/TIR-{self.incident:03d}"
            self.incident += 1
        self.rows.append(
            {
                "requirement_id": f"REQ-{feature_id(case_id)}",
                "test_design_id": test_design_id(case_id),
                "test_case_id": case_id,
                "test_procedure_id": CASE_PROCEDURES[case_id],
                "type_of_testing": "Functional Testing",
                "tool": tool,
                "pass_fail": status,
                "incident_id": incident,
                "remark": remark,
            }
        )


def run_tests(driver, data, rec):
    # F001 Sign Up
    execute("DELETE FROM users WHERE email=%s", ("svv_signup_new@example.test",))
    page(driver, "/signup")
    fill(driver, "name", "SVV Signup")
    fill(driver, "email", "svv_signup_new@example.test")
    fill(driver, "password", "password")
    click_submit(driver)
    exists = scalar("SELECT COUNT(*) FROM users WHERE email=%s", ("svv_signup_new@example.test",)) == 1
    rec.add("TC-01-001", exists and "registered" in driver.page_source.lower(), "Selenium", "Registered test account through the real Sign Up form.")

    page(driver, "/signup")
    fill(driver, "name", "SVV Signup")
    fill(driver, "email", "")
    fill(driver, "password", "password")
    click_submit(driver)
    rec.add("TC-01-002", "All fields are required" in driver.page_source, "Selenium", "Blank email submitted through the Sign Up form.")

    page(driver, "/signup")
    fill(driver, "name", "SVV Signup")
    fill(driver, "email", "john.mail.com")
    fill(driver, "password", "password")
    valid = form_valid(driver)
    click_submit(driver)
    rec.add("TC-01-003", not valid, "Selenium", "Invalid email was rejected by browser email-field validation.")

    page(driver, "/signup")
    fill(driver, "name", "SVV Duplicate")
    fill(driver, "email", "svv_duplicate@example.test")
    fill(driver, "password", "password")
    click_submit(driver)
    rec.add("TC-01-004", "User already exists with this email" in driver.page_source, "Selenium", "Duplicate seeded account was submitted through Sign Up.")

    # F002 Login
    login_user(driver, "svv_user@example.test", "password")
    rec.add("TC-02-001", source_has(driver, "Signout", "Profile"), "Selenium", "Valid user credentials opened a logged-in session.")

    login_user(driver, "svv_user@example.test", "wrong-password")
    rec.add("TC-02-002", "Email or password incorrect" in driver.page_source, "Selenium", "Registered email with wrong password was accepted if this row fails.")

    login_user(driver, "svv_unknown@example.test", "password")
    rec.add("TC-02-003", "Email or password incorrect" in driver.page_source, "Selenium", "Unregistered email was submitted with a password.")

    login_user(driver, "svv_unknown@example.test", "wrong-password")
    rec.add("TC-02-004", "Email or password incorrect" in driver.page_source, "Selenium", "Unregistered email was submitted with an incorrect password.")

    # F003 Logout
    login_user(driver, "svv_user@example.test", "password")
    page(driver, "/signout/")
    rec.add("TC-03-001", "Signin" in driver.page_source and "Signout" not in driver.page_source, "Selenium", "Logout route ended the active user session.")

    login_user(driver, "svv_user@example.test", "password")
    page(driver, "/user/")
    page(driver, "/signout/")
    driver.back()
    time.sleep(0.2)
    driver.refresh()
    time.sleep(0.2)
    rec.add("TC-03-002", "/signin" in driver.current_url or "SIGNIN" in driver.page_source, "Selenium", "Browser Back after logout was followed by refresh to verify session protection.")

    login_user(driver, "svv_user@example.test", "password")
    page(driver, "/signout/")
    page(driver, "/user/")
    rec.add("TC-03-003", "/signin" in driver.current_url or "SIGNIN" in driver.page_source, "Selenium", "Protected user profile URL was opened directly after logout.")

    # F004 Manage Profile
    execute("UPDATE users SET name=%s,email=%s,bio=%s,password=%s WHERE id=%s", ("SVV Profile", "svv_profile@example.test", "SVV profile", KNOWN_HASH, data["profile_user_id"]))
    login_user(driver, "svv_profile@example.test", "password")
    page(driver, "/user/")
    driver.find_element(By.ID, "profile-tab").click()
    fill(driver, "name", "Ali")
    fill(driver, "email", "ali@test.com")
    fill(driver, "password", "password")
    fill(driver, "bio", "Updated profile")
    click_submit(driver)
    updated = fetchone("SELECT name,email FROM users WHERE id=%s", (data["profile_user_id"],))
    rec.add("TC-04-001", updated["name"] == "Ali" and updated["email"] == "ali@test.com", "Selenium", "Profile was updated through the real profile form.")

    execute("UPDATE users SET name=%s,email=%s,bio=%s,password=%s WHERE id=%s", ("SVV Profile", "svv_profile@example.test", "SVV profile", KNOWN_HASH, data["profile_user_id"]))
    login_user(driver, "svv_profile@example.test", "password")
    page(driver, "/user/")
    driver.find_element(By.ID, "profile-tab").click()
    fill(driver, "email", "ali.com")
    valid = form_valid(driver)
    click_submit(driver)
    rec.add("TC-04-002", not valid, "Selenium", "Invalid email was rejected by browser email-field validation.")

    execute("UPDATE users SET name=%s,email=%s,bio=%s,password=%s WHERE id=%s", ("SVV Profile", "svv_profile@example.test", "SVV profile", KNOWN_HASH, data["profile_user_id"]))
    login_user(driver, "svv_profile@example.test", "password")
    page(driver, "/user/")
    driver.find_element(By.ID, "profile-tab").click()
    fill(driver, "name", "")
    fill(driver, "email", "svv_profile@example.test")
    fill(driver, "password", "password")
    click_submit(driver)
    name_after = scalar("SELECT name FROM users WHERE id=%s", (data["profile_user_id"],))
    rec.add("TC-04-003", name_after == "SVV Profile", "Selenium", "Empty name was submitted through the profile update form.")

    execute("UPDATE users SET name=%s,email=%s,bio=%s,password=%s WHERE id=%s", ("SVV Profile", "svv_profile@example.test", "SVV profile", KNOWN_HASH, data["profile_user_id"]))
    login_user(driver, "svv_profile@example.test", "password")
    page(driver, "/user/")
    driver.find_element(By.ID, "profile-tab").click()
    fill(driver, "name", "SVV Profile")
    fill(driver, "email", "")
    fill(driver, "password", "password")
    click_submit(driver)
    email_after = scalar("SELECT email FROM users WHERE id=%s", (data["profile_user_id"],))
    rec.add("TC-04-004", email_after == "svv_profile@example.test", "Selenium", "Empty email was submitted through the profile update form.")

    driver.delete_all_cookies()
    page(driver, "/user/")
    rec.add("TC-04-005", "/signin" in driver.current_url or "SIGNIN" in driver.page_source, "Selenium", "Profile page was opened without a user session.")

    # F005 View Book List
    page(driver, "/books/")
    rec.add("TC-05-001", "SVV Test Book Available" in driver.page_source, "Selenium", "Book list page displayed seeded available books.")

    original_availability = fetchall("SELECT id, availability FROM books")
    try:
        execute("UPDATE books SET availability=0")
        page(driver, "/books/")
        rec.add("TC-05-002", "No Books Found!" in driver.page_source, "Selenium", "All books were temporarily hidden to verify empty-list behavior.")
    finally:
        for row in original_availability:
            execute("UPDATE books SET availability=%s WHERE id=%s", (row["availability"], row["id"]))

    page(driver, "/books/")
    rec.add("TC-05-003", source_has(driver, "SVV Test Book Available", "SVV Author", "Books Left"), "Selenium", "Book list displayed title, author, and availability/count.")
    failure = simulated_failure_response("/books/", "routes.book", "book_manager", "list")
    rec.add(
        "TC-05-004",
        failure.status_code < 500 and "error" in failure.get_data(as_text=True).lower(),
        "Postman/HTTP",
        f"Simulated BookManager.list database failure returned HTTP {failure.status_code}.",
    )

    # F006 View Book Details
    page(driver, f"/books/{data['available_book_id']}")
    rec.add("TC-06-001", source_has(driver, "SVV Test Book Available", "SVV automated test book", "SVV Author"), "Selenium", "Existing book details page was opened.")

    r = requests.get(BASE_URL + "/books/999999", timeout=10)
    rec.add("TC-06-002", r.status_code == 200 and "No Book Found" in r.text, "Postman/HTTP", f"GET /books/999999 returned HTTP {r.status_code}.")

    page(driver, f"/books/{data['available_book_id']}")
    rec.add("TC-06-003", "Add" in driver.page_source and "Books Left" in driver.page_source, "Selenium", "Available book details page displayed a reserve/add option.")

    page(driver, f"/books/{data['unavailable_book_id']}")
    rec.add("TC-06-004", "All gone" in driver.page_source, "Selenium", "Unavailable book details page displayed zero-count status.")
    failure = simulated_failure_response(f"/books/{data['available_book_id']}", "routes.book", "book_manager", "getBook")
    rec.add(
        "TC-06-005",
        failure.status_code < 500 and "error" in failure.get_data(as_text=True).lower(),
        "Postman/HTTP",
        f"Simulated BookManager.getBook database failure returned HTTP {failure.status_code}.",
    )

    # F007 Search Book
    page(driver, "/books/search?keyword=Harry%20Potter")
    rec.add("TC-07-001", source_has(driver, "Search Found", "SVV Test Harry Potter Automation"), "Selenium", "Search was executed with a valid keyword.")

    page(driver, "/")
    driver.find_element(By.NAME, "keyword").clear()
    click_submit(driver)
    rec.add("TC-07-002", "validation" in driver.page_source.lower() or "required" in driver.page_source.lower(), "Selenium", "Empty search input was submitted from the home search form.")

    long_keyword = "A" * 60
    page(driver, f"/books/search?keyword={long_keyword}")
    long_search_source = driver.page_source.lower()
    rec.add(
        "TC-07-003",
        "validation" in long_search_source or "too long" in long_search_source or "not exceed" in long_search_source,
        "Selenium",
        "A 60-character keyword was submitted.",
    )

    page(driver, "/books/search?keyword=%40%40%40%23%23%23")
    rec.add("TC-07-004", "No Books Found!" in driver.page_source, "Selenium", "Special-character search returned a safe no-results page.")

    page(driver, "/books/search?keyword=Harry%20Potter")
    rec.add("TC-07-005", "SVV Test Harry Potter Automation" in driver.page_source, "Selenium", "Search results contained the seeded matching book.")

    page(driver, "/")
    driver.find_element(By.NAME, "keyword").clear()
    click_submit(driver)
    rec.add("TC-07-006", "validation" in driver.page_source.lower() or "required" in driver.page_source.lower(), "Selenium", "Empty search validation message was checked.")

    # F008 Reserve Book
    login_user(driver, "svv_user@example.test", "password")
    page(driver, f"/books/{data['available_book_id']}")
    driver.find_element(By.LINK_TEXT, "Add").click()
    time.sleep(0.3)
    reserved = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (data["user_id"], data["available_book_id"]),
    )
    rec.add("TC-08-001", reserved == 1 and "Book reserved" in driver.page_source, "Selenium", "Available book was reserved through the UI.")

    login_user(driver, "svv_user@example.test", "password")
    page(driver, f"/books/{data['unavailable_book_id']}")
    driver.find_element(By.LINK_TEXT, "Add").click()
    time.sleep(0.3)
    unavailable_reserved = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (data["user_id"], data["unavailable_book_id"]),
    )
    rec.add("TC-08-002", unavailable_reserved == 0 and "unavailable" in driver.page_source.lower(), "Selenium", "Unavailable book reservation was attempted through the UI.")

    login_user(driver, "svv_limit@example.test", "password")
    page(driver, f"/books/{data['limit_book_id']}")
    driver.find_element(By.LINK_TEXT, "Add").click()
    time.sleep(0.3)
    limit_reserved = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (data["limit_user_id"], data["limit_book_id"]),
    )
    rec.add("TC-08-003", limit_reserved == 0 and "limit" in driver.page_source.lower(), "Selenium", "A user with five reservations attempted another reservation.")

    s = req_session_user("svv_user@example.test")
    before = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (data["user_id"], data["duplicate_reserve_book_id"]),
    )
    s.get(BASE_URL + f"/books/add/{data['duplicate_reserve_book_id']}", timeout=10)
    after = scalar(
        "SELECT COUNT(*) FROM reserve WHERE user_id=%s AND book_id=%s",
        (data["user_id"], data["duplicate_reserve_book_id"]),
    )
    rec.add("TC-08-004", after == before, "Postman/HTTP", "Duplicate reservation route was invoked directly with an authenticated user session.")

    rec.add("TC-08-005", limit_reserved == 0 and "limit" in driver.page_source.lower(), "Selenium", "Reservation limit message was checked after exceeding the limit.")

    # F009 View Reserved Books
    login_user(driver, "svv_reserved@example.test", "password")
    page(driver, "/user/")
    rec.add("TC-09-001", "SVV Test Book Reserved" in driver.page_source, "Selenium", "Profile page displayed reserved books for the logged-in user.")
    rec.add("TC-09-004", "SVV Test Book Reserved" in driver.page_source and "SVV Test Book Duplicate Reserve" not in driver.page_source, "Selenium", "Reservation list was checked for the current user's records only.")

    login_user(driver, "svv_empty@example.test", "password")
    page(driver, "/user/")
    rec.add("TC-09-002", "No Books You Reserved!" in driver.page_source, "Selenium", "User with no reservations opened the profile page.")
    rec.add("TC-09-005", "No Books You Reserved!" in driver.page_source, "Selenium", "Empty reservation message was checked.")

    driver.delete_all_cookies()
    page(driver, "/user/")
    rec.add("TC-09-003", "/signin" in driver.current_url or "SIGNIN" in driver.page_source, "Selenium", "Reserved-book/profile page was opened without a session.")

    # F0010 Add Book
    admin_session = req_session_admin()
    add_page = admin_session.get(BASE_URL + "/admin/books/add", timeout=10).text
    admin_session.post(
        BASE_URL + "/admin/books/add",
        data={"title": "SVV Test Add Via UI", "qty": "10", "avaliable": "on", "desc": "Added through admin form"},
        timeout=10,
    )
    add_exists = scalar("SELECT COUNT(*) FROM books WHERE name=%s", ("SVV Test Add Via UI",))
    rec.add("TC-10-001", add_exists == 1, "Postman/HTTP", "Admin Add Book route was submitted with valid data.")
    rec.add("TC-10-009", add_exists == 1, "Postman/HTTP", "Database insertion was checked after valid Add Book submission.")

    rec.add("TC-10-002", 'name="title"' in add_page and "required" in add_page, "Postman/HTTP", "Add Book HTML marks title as a required field.")
    rec.add("TC-10-003", 'name="desc"' in add_page and 'name="desc" required' in add_page, "Postman/HTTP", "Description field was inspected for required validation.")
    rec.add("TC-10-004", 'name="qty"' in add_page and "min=" in add_page, "Postman/HTTP", "Quantity field was inspected for a minimum value rule.")
    rec.add("TC-10-005", 'name="qty"' in add_page and 'type="number"' in add_page, "Postman/HTTP", "Quantity field uses a browser number input for non-numeric validation.")

    duplicate_count = scalar("SELECT COUNT(*) FROM books WHERE name=%s", ("SVV Test Book Available",))
    rec.add("TC-10-006", duplicate_count == 1 and "duplicate" in add_page.lower(), "Postman/HTTP", "Duplicate book handling was checked against the real Add Book route/page.")
    rec.add("TC-10-007", 'name="title"' in add_page and 'name="qty"' in add_page and "required" in add_page, "Postman/HTTP", "All-empty submission is blocked partly by required fields in the HTML form.")
    rec.add("TC-10-008", "description" in add_page.lower() and "error" in add_page.lower(), "Postman/HTTP", "Field-specific error message was checked for missing Description.")

    # F0011 Delete Book
    delete_book_id = ensure_book("SVV Test Delete Target", count=1)
    admin_session = req_session_admin()
    admin_session.get(BASE_URL + f"/admin/books/delete/{delete_book_id}", timeout=10)
    deleted = scalar("SELECT COUNT(*) FROM books WHERE id=%s", (delete_book_id,)) == 0
    rec.add("TC-11-001", deleted, "Postman/HTTP", "Existing book was deleted through the real admin delete route.")
    rec.add("TC-11-007", deleted, "Postman/HTTP", "Inventory database was checked after deletion.")

    failure_book_id = ensure_book("SVV Test Delete Failure Target", count=1)
    failure = simulated_failure_response(
        f"/admin/books/delete/{failure_book_id}",
        "routes.admin",
        "book_manager",
        "delete",
        session_key="admin",
    )
    still_exists_after_failure = scalar("SELECT COUNT(*) FROM books WHERE id=%s", (failure_book_id,)) == 1
    rec.add(
        "TC-11-002",
        failure.status_code < 500 and still_exists_after_failure and "error" in failure.get_data(as_text=True).lower(),
        "Postman/HTTP",
        f"Simulated BookManager.delete failure returned HTTP {failure.status_code}; target book still exists = {still_exists_after_failure}.",
    )

    r = admin_session.get(BASE_URL + "/admin/books/delete/999999", timeout=10, allow_redirects=False)
    rec.add("TC-11-003", "not exist" in r.text.lower() or "error" in r.text.lower(), "Postman/HTTP", f"Delete non-existing book returned HTTP {r.status_code}.")

    normal_session = req_session_user("svv_user@example.test")
    auth_book_id = ensure_book("SVV Test Unauthorized Delete Target", count=1)
    r = normal_session.get(BASE_URL + f"/admin/books/delete/{auth_book_id}", timeout=10, allow_redirects=False)
    still_exists = scalar("SELECT COUNT(*) FROM books WHERE id=%s", (auth_book_id,)) == 1
    rec.add("TC-11-004", r.status_code in (301, 302) and "/admin/signin" in r.headers.get("Location", "") and still_exists, "Postman/HTTP", "Normal user attempted the admin delete route.")

    login_admin(driver)
    open_admin_page(driver, "/admin/books/")
    rec.add("TC-11-005", "confirm(" in driver.page_source.lower(), "Selenium", "Admin delete link was inspected for an explicit confirmation step.")
    rec.add("TC-11-006", "confirm(" in driver.page_source.lower() and "cancel" in driver.page_source.lower(), "Selenium", "Cancel deletion flow was checked; no confirmation dialog is implemented.")
    rec.add(
        "TC-11-008",
        failure.status_code < 500 and "error" in failure.get_data(as_text=True).lower(),
        "Postman/HTTP",
        f"Deletion failure message check used simulated delete failure response HTTP {failure.status_code}.",
    )

    # F0012 Edit Book
    edit_book_id = ensure_book("SVV Test Edit Target", count=3, desc="Original description")
    admin_session.post(
        BASE_URL + f"/admin/books/edit/{edit_book_id}",
        data={"title": "Updated Book", "qty": "10", "desc": "Updated description", "avaliable": "1"},
        timeout=10,
    )
    edited = fetchone("SELECT name,count,`desc` FROM books WHERE id=%s", (edit_book_id,))
    edit_success = edited and edited["name"] == "Updated Book" and edited["count"] == 10
    rec.add("TC-12-001", edit_success, "Postman/HTTP", "Admin edit route was submitted with valid values.")
    rec.add("TC-12-010", edit_success, "Postman/HTTP", "Database was checked after valid edit submission.")

    r = admin_session.get(BASE_URL + "/admin/books/edit/999999", timeout=10)
    rec.add("TC-12-002", r.status_code == 200 and "No book found" in r.text, "Postman/HTTP", f"Invalid edit Book ID returned HTTP {r.status_code}.")

    edit_page = admin_session.get(BASE_URL + f"/admin/books/edit/{edit_book_id}", timeout=10).text
    rec.add("TC-12-003", 'name="title"' in edit_page and "required" in edit_page, "Postman/HTTP", "Edit Book HTML marks title as a required field.")
    rec.add("TC-12-009", 'name="title"' in edit_page and "required" in edit_page, "Postman/HTTP", "Validation feedback for missing title is provided by browser required-field validation.")
    rec.add("TC-12-004", 'name="qty"' in edit_page and "required" in edit_page, "Postman/HTTP", "Edit Book HTML marks quantity as a required field.")
    rec.add("TC-12-005", 'name="qty"' in edit_page and "min=" in edit_page, "Postman/HTTP", "Quantity field was inspected for a positive/minimum value rule.")
    rec.add("TC-12-006", 'name="qty"' in edit_page and 'type="number"' in edit_page, "Postman/HTTP", "Quantity field uses a browser number input for non-numeric validation.")

    before_desc = scalar("SELECT `desc` FROM books WHERE id=%s", (edit_book_id,))
    admin_session.post(
        BASE_URL + f"/admin/books/edit/{edit_book_id}",
        data={"title": "SVV Test Edit Target", "qty": "3", "desc": "Partial update text", "avaliable": "1"},
        timeout=10,
    )
    after_desc = scalar("SELECT `desc` FROM books WHERE id=%s", (edit_book_id,))
    rec.add("TC-12-007", after_desc == "Partial update text" and before_desc != after_desc, "Postman/HTTP", "Description-only edit was submitted through the edit route.")

    user_session = req_session_user("svv_user@example.test")
    r = user_session.get(BASE_URL + f"/admin/books/edit/{edit_book_id}", timeout=10, allow_redirects=False)
    rec.add("TC-12-008", r.status_code in (301, 302) and "/admin/signin" in r.headers.get("Location", ""), "Postman/HTTP", "Normal user attempted the admin edit route.")


def main():
    start_time = datetime.now()
    process = None
    driver = None
    rec = Recorder()
    environment_error = None
    try:
        process = ensure_server()
        data = setup_data()
        driver = make_driver()
        run_tests(driver, data, rec)
    except Exception as exc:
        environment_error = f"{type(exc).__name__}: {exc}"
    finally:
        if driver:
            driver.quit()
        try:
            cleanup_test_data()
        except Exception as exc:
            environment_error = environment_error or f"Cleanup error: {type(exc).__name__}: {exc}"
        if process:
            process.terminate()
            process.wait(timeout=10)

    end_time = datetime.now()
    payload = {
        "tester": TESTER,
        "base_url": BASE_URL,
        "start_time": start_time.isoformat(timespec="seconds"),
        "end_time": end_time.isoformat(timespec="seconds"),
        "environment_error": environment_error,
        "results": rec.rows,
        "summary": {
            "total": len(rec.rows),
            "pass": sum(1 for row in rec.rows if row["pass_fail"] == "Pass"),
            "fail": sum(1 for row in rec.rows if row["pass_fail"] == "Fail"),
            "not_executed": sum(1 for row in rec.rows if row["pass_fail"] == "Not Executed"),
        },
    }
    OUT_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    if environment_error:
        print(environment_error)
        sys.exit(1)


if __name__ == "__main__":
    main()
