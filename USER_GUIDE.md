# User Guide

This guide explains how normal users and admin users operate the Library Management System.

## 1. User Workflows

### 1.1 Sign Up

1. Open the LMS home page.
2. Click `Signup`.
3. Enter name, email address, and password.
4. Submit the form.

The improved system validates required fields, email format, duplicate email, and password length.

### 1.2 Sign In

1. Click `Signin`.
2. Enter registered email and password.
3. Submit the form.

If credentials are invalid, the improved system displays:

```text
Email or password incorrect
```

### 1.3 Browse Books

1. Click `Books`.
2. Review available books in the catalogue.
3. Open a book detail page to view more information.

The improved UI displays the title, description, author, availability status, and quantity more clearly.

### 1.4 Search Books

1. Use the search field on the home page or books page.
2. Enter a title or author keyword.
3. Submit the search form.

If the keyword is empty, the improved system displays:

```text
Please enter a search keyword
```

### 1.5 Reserve Book

1. Sign in as a user.
2. Open a book detail page.
3. Click `Add` or reserve button.

The improved system handles:

- Successful reservation.
- Book unavailable.
- Duplicate reservation.
- Reservation limit reached.

### 1.6 View Reserved Books

1. Sign in as a user.
2. Open `Profile`.
3. Review reserved books under the user profile page.

### 1.7 Update Profile

1. Sign in as a user.
2. Open `Profile`.
3. Open the profile edit form.
4. Update name, email, password, or bio.
5. Submit the form.

The improved system validates empty name, invalid email, and short password.

## 2. Admin Workflows

### 2.1 Admin Sign In

1. Open `/admin/signin/`.
2. Enter admin email and password.
3. Submit the form.

Seed admin account:

```text
Email: hamza@gmail.com
Password: password
```

### 2.2 View Inventory

1. Sign in as admin.
2. Open `Manage Books`.
3. Review the book inventory table.

The improved admin table shows title, author, availability, quantity, edit action, and delete action.

### 2.3 Add Book

1. Sign in as admin.
2. Open `Manage Books > Add Book`.
3. Enter title, author, edition, quantity, availability, and description.
4. Submit the form.

The improved system saves the book and displays:

```text
Book added successfully
```

### 2.4 Edit Book

1. Sign in as admin.
2. Open `Manage Books`.
3. Click `Edit` for a book.
4. Update book details.
5. Submit the form.

The improved system updates the record and displays:

```text
Book updated successfully
```

### 2.5 Delete Book

1. Sign in as admin.
2. Open `Manage Books`.
3. Click `Delete`.
4. Confirm the browser confirmation prompt.

The improved system asks for confirmation before deleting a book.

## 3. Demo Accounts

| Role | Email | Password |
|---|---|---|
| User/Admin seed account | `hamza@gmail.com` | `password` |
| User seed account | `naveed@gmail.com` | `password` |

Temporary demo accounts such as `daydemo_wayman@example.test` are created only for presentation screenshots and are not part of the original SQL seed file.
