# Library Management System

A Flask and MySQL web application for managing library users, books, reservations, and administrative inventory tasks.

![Library Management App - Flask](https://github.com/hamzaavvan/library-management-system/blob/master/ss/ss2.JPG?raw=true)

## Repository Information

- Original repository: https://github.com/hamzaavvan/library-management-system
- Assignment repository: https://github.com/yongdilun/library-management-system
- Baseline and automated testing branch: `main`
- Enhancement branch: `software-maintainability-assignment`

## Project Documentation

This repository provides the following documentation for the software maintenance assignment:

| Document | Purpose |
|---|---|
| `README.md` | Project overview, feature summary, setup summary, and branch information. |
| [`docs/INSTALLATION_GUIDE.md`](docs/INSTALLATION_GUIDE.md) | Detailed local installation, database setup, and server startup instructions. |
| [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md) | User and admin workflow guide for operating the LMS. |
| [`docs/DEVELOPER_DOCUMENTATION.md`](docs/DEVELOPER_DOCUMENTATION.md) | Codebase structure, architecture notes, database overview, and maintenance changes. |
| [`docs/TEST_DOCUMENTATION.md`](docs/TEST_DOCUMENTATION.md) | Test strategy, tools, commands, baseline results, improved results, and evidence files. |
| [`docs/FAQ.md`](docs/FAQ.md) | Common questions about setup, credentials, branches, testing, and known behavior. |

## Key Features

- User sign up, login, logout, and profile management.
- Book browsing, search, detail viewing, and reservation.
- Admin sign in, user viewing, and book inventory management.
- Server-side validation for important user and admin forms.
- Safer reservation handling with duplicate-reservation and reservation-limit checks.

## Installation

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create a local environment file from the example:

```bash
copy .env.example .env
```

Update `.env` with the local database password and a private `SECRET_KEY`.

## Environment Variables

```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=change-this-secret-key
SESSION_COOKIE_SECURE=false
MYSQL_DATABASE_HOST=localhost
MYSQL_DATABASE_USER=root
MYSQL_DATABASE_PASSWORD=your-local-password
MYSQL_DATABASE_DB=lms
```

## Database Setup

Import the database schema from:

```bash
db/lms.sql
```

Apply the reservation integrity migration when updating an existing database:

```bash
mysql -u root -p lms < db/migrations/001_reservation_integrity.sql
```

## Start Server

Windows quick start:

```bat
start_server.bat
```

Manual command:

```bash
python -m flask run --host 127.0.0.1 --port 5000
```

Then open:

```text
http://127.0.0.1:5000
```

## Production HTTPS/TLS Deployment

The local Flask development server is intended for development only and runs on HTTP. For production, deploy the LMS behind a TLS-enabled web server or reverse proxy such as Nginx, Apache, IIS, or a managed hosting platform.

Production deployment requirements:

- Use HTTPS with TLS 1.2 or higher for all browser-to-server traffic.
- Redirect HTTP traffic to HTTPS at the web server or reverse proxy.
- Use a valid SSL/TLS certificate from a trusted certificate authority.
- Set `SESSION_COOKIE_SECURE=true` when the application is served through HTTPS.
- Keep `SECRET_KEY` private and unique per deployment environment.

## Maintenance Validation

The maintenance enhancement is validated with a focused automated test runner:

Windows batch files:

```bat
run_full_pipeline_tests.bat
run_maintenance_validation_tests.bat
run_nfr_tests.bat
```

Manual command:

```bash
python tests/run_maintenance_validation.py
```

The runner verifies:

- Wrong-password login is rejected.
- Admin add-book saves a new record.
- Admin edit-book updates an existing record.
- Empty search keyword shows validation feedback.
- Reservation migration defines foreign keys and duplicate prevention.

Validation output is saved to:

```text
reports/maintenance_evidence/maintenance_validation_results.json
```

## Enhancement Evidence

The final maintenance report and evidence screenshots are generated under the project root and `reports/maintenance_evidence/`.

```bash
python tests/generate_final_maintenance_report.py
```
