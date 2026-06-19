# Developer Documentation

This document describes the project structure, main components, and maintenance enhancements implemented for the Library Management System.

## 1. Technology Stack

| Layer | Technology |
|---|---|
| Backend framework | Flask |
| Database | MySQL |
| Templates | Jinja2 HTML templates |
| Styling | CSS, Bootstrap icons |
| Functional testing | Selenium and Python Requests |
| Database testing | PyMySQL |
| Evidence capture | Playwright |

## 2. Repository Branches

| Branch | Purpose |
|---|---|
| `main` | Baseline system plus automated test pipeline. |
| `software-maintainability-assignment` | Improved system with maintenance enhancements. |

## 3. Project Structure

```text
App/                         Session/auth helper classes
Controllers/                 Manager classes for admin, user, and book workflows
Models/                      DAO and database access classes
Misc/                        Shared helper functions such as hashing and validation helpers
routes/                      Flask route handlers
templates/                   Jinja2 HTML pages
static/                      CSS and static assets
db/                          SQL schema and migration scripts
tests/                       Functional, non-functional, and maintainability test runners
reports/                     Generated evidence and screenshots, ignored by Git
```

## 4. Main Runtime Flow

1. `app.py` creates the Flask app and configures the DAO.
2. Blueprints are registered from `routes/user.py`, `routes/book.py`, and `routes/admin.py`.
3. Routes call manager classes in `Controllers/`.
4. Manager classes call DAO classes in `Models/`.
5. DAO classes execute SQL operations against MySQL.
6. Jinja templates render the user and admin interfaces.

## 5. Key Components

### 5.1 User Module

Files:

- `routes/user.py`
- `Controllers/UserManager.py`
- `templates/signin.html`
- `templates/signup.html`
- `templates/profile.html`

Responsibilities:

- User sign up.
- User sign in and sign out.
- Profile display and update.
- User validation and feedback.

### 5.2 Book Module

Files:

- `routes/book.py`
- `Controllers/BookManager.py`
- `Models/BookDAO.py`
- `templates/books.html`
- `templates/book_view.html`

Responsibilities:

- Book list.
- Book detail.
- Search.
- Reservation.
- Duplicate and limit handling.

### 5.3 Admin Module

Files:

- `routes/admin.py`
- `Controllers/AdminManager.py`
- `templates/admin/`

Responsibilities:

- Admin sign in.
- Inventory list.
- Add book.
- Edit book.
- Delete book.
- Admin validation messages.

## 6. Maintenance Enhancements

### 6.1 Security

The improved branch replaces unsafe password handling with Werkzeug password hashing and verification. It also uses environment-based secret key configuration.

Important files:

- `Misc/functions.py`
- `app.py`
- `.env.example`

### 6.2 Admin Book Management

The improved branch completes add, edit, and delete book workflows with backend persistence, validation, and user feedback.

Important files:

- `routes/admin.py`
- `Models/BookDAO.py`
- `templates/admin/books/add.html`
- `templates/admin/books/edit.html`
- `templates/admin/books/views.html`

### 6.3 User Validation

The improved branch adds validation for login, sign up, profile update, and search input.

Important files:

- `routes/user.py`
- `routes/book.py`
- `templates/profile.html`

### 6.4 Reservation Reliability

The improved branch adds duplicate reservation checks, reservation limit handling, safer stock decrement, and database migration support.

Important files:

- `Models/BookDAO.py`
- `routes/book.py`
- `db/migrations/001_reservation_integrity.sql`

### 6.5 UI/UX Upgrade

The improved branch modernizes the user and admin interfaces, including responsive layouts, clearer forms, alerts, cards, and inventory tables.

Important files:

- `static/style.css`
- `templates/shared/layout.html`
- `templates/shared/admin_layout.html`
- `templates/home.html`
- `templates/books.html`
- `templates/profile.html`
- `templates/admin/`

## 7. Database Notes

The seed SQL is stored in:

```text
db/lms.sql
```

The improved reservation integrity migration is stored in:

```text
db/migrations/001_reservation_integrity.sql
```

The migration adds stronger reservation integrity rules, including relationships between users, books, and reservations.

## 8. Development Rules

- Keep `.env` private and do not commit it.
- Use the `main` branch only for baseline comparison.
- Use `software-maintainability-assignment` for enhancement work.
- Run the functional, non-functional, and maintainability tests after code changes.
- Keep generated reports and screenshots out of Git unless specifically required by the lecturer.

## 9. Known Local Development Ports

| Version | Port |
|---|---:|
| Improved branch | `5000` |
| Baseline branch | `5001` |

See `WORKTREE_RUN_AND_TEST_COMMANDS.md` for running both versions together.
