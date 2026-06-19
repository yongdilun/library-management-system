# Installation Guide

This guide explains how to install and run the Library Management System locally for development, testing, and demonstration.

## 1. Prerequisites

Install the following software:

- Python 3.13 or compatible Python 3 version
- MySQL Server
- Google Chrome, required for Selenium and Playwright evidence capture
- Git

Recommended Python packages are listed in `requirements.txt`.

## 2. Clone Repository

```powershell
git clone https://github.com/yongdilun/library-management-system.git
cd library-management-system
git checkout software-maintainability-assignment
```

Use `main` when testing the baseline version, and `software-maintainability-assignment` when testing the improved version.

## 3. Install Python Dependencies

```powershell
pip install -r requirements.txt
```

Some test and evidence scripts also use Selenium, Requests, PyMySQL, and Playwright. If they are not already installed:

```powershell
pip install selenium requests pymysql playwright
```

## 4. Configure Environment File

Create a local `.env` file from the example:

```powershell
copy .env.example .env
```

Update the database password and database name in `.env`.

Example development values:

```text
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=change-this-secret-key
SESSION_COOKIE_SECURE=false
MYSQL_DATABASE_HOST=localhost
MYSQL_DATABASE_USER=root
MYSQL_DATABASE_PASSWORD=your-local-password
MYSQL_DATABASE_DB=lms_improved
```

Do not commit `.env` because it contains local secrets.

## 5. Create Database

Log in to MySQL and create a database:

```powershell
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS lms_improved;"
```

Import the schema and seed data:

```powershell
Get-Content db\lms.sql | mysql -u root -p lms_improved
```

For the improved branch, apply the reservation integrity migration if required:

```powershell
Get-Content db\migrations\001_reservation_integrity.sql | mysql -u root -p lms_improved
```

## 6. Start Application

Quick start:

```powershell
.\start_server.bat
```

Manual start:

```powershell
python -m flask run --host 127.0.0.1 --port 5000
```

Open the application:

```text
http://127.0.0.1:5000
```

## 7. Seed Login Accounts

The seed database includes:

| Role | Email | Password |
|---|---|---|
| User/Admin seed account | `hamza@gmail.com` | `password` |
| User seed account | `naveed@gmail.com` | `password` |

## 8. Running Baseline and Improved Versions Together

The project was tested using two worktrees:

| Version | Branch | Port | Database |
|---|---|---:|---|
| Baseline | `main` | `5001` | `lms_main` |
| Improved | `software-maintainability-assignment` | `5000` | `lms_improved` |

See `WORKTREE_RUN_AND_TEST_COMMANDS.md` for detailed commands.

## 9. Troubleshooting

- If login fails after database reset, confirm the app is using the correct `.env` database name.
- If port `5000` or `5001` is busy, stop the old Flask process or use another port.
- If tests fail because the browser cannot start, confirm Google Chrome is installed.
- If MySQL import fails in PowerShell, use `Get-Content db\lms.sql | mysql -u root -p database_name` instead of `< db\lms.sql`.
