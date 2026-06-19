# FAQ

## 1. What is this project?

This is a Flask and MySQL Library Management System used for a software maintenance assignment. The original open-source project was enhanced to improve security, validation, admin workflows, reservation reliability, UI/UX, testing, and documentation.

## 2. What is the original repository?

```text
https://github.com/hamzaavvan/library-management-system
```

## 3. What is the assignment repository?

```text
https://github.com/yongdilun/library-management-system
```

## 4. Which branch should I use?

Use:

```text
main
```

for the baseline system and automated test comparison.

Use:

```text
software-maintainability-assignment
```

for the improved system.

## 5. What are the default login credentials?

Seed accounts:

| Role | Email | Password |
|---|---|---|
| User/Admin seed account | `hamza@gmail.com` | `password` |
| User seed account | `naveed@gmail.com` | `password` |

## 6. Why is `.env` missing after cloning?

`.env` is ignored by Git because it contains local secrets such as database password and secret key. Create it from `.env.example`:

```powershell
copy .env.example .env
```

## 7. How do I start the server?

Use:

```powershell
.\start_server.bat
```

or:

```powershell
python -m flask run --host 127.0.0.1 --port 5000
```

## 8. Why do the baseline tests fail?

The baseline branch intentionally contains the original system behavior. The failing tests show the issues found during analysis, including incomplete admin functions, weak validation, reservation reliability issues, and non-functional requirement failures.

## 9. Is the test pipeline only Selenium?

No. The test pipeline uses:

- Selenium for browser workflows.
- Python Requests for route-level HTTP checks.
- PyMySQL for database checks.
- Playwright for screenshot evidence.

## 10. Where are screenshots and generated reports stored?

Generated evidence is stored under:

```text
reports/
```

Generated report files are ignored by Git to keep the repository clean.

## 11. Why does local development use HTTP instead of HTTPS?

The local Flask development server runs on HTTP. For production, the app should be deployed behind a TLS-enabled reverse proxy such as Nginx, Apache, IIS, or a managed hosting platform. Production should use HTTPS/TLS 1.2 or higher and set:

```text
SESSION_COOKIE_SECURE=true
```

## 12. What are the most important improvements?

The improved branch includes:

- Safer password hashing and environment-based secret key.
- Completed admin add/edit/delete book workflows.
- User and admin validation improvements.
- Duplicate reservation and reservation limit handling.
- Reservation database integrity migration.
- Modern responsive UI upgrade.
- Automated functional, non-functional, and maintainability tests.
