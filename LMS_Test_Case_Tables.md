# Library Management System Test Case Tables

Generated from the provided approach refinement and test identification content for F001 through F0012.

## F001 Sign Up

### Table 2.4.1 TC-01-001 Verify successful Sign Up with valid data inputs Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-01-001 |
| Related Feature ID | F001 |
| Objective | Verify successful Sign Up with valid data inputs |
| Covered Test Coverage Items | TCOV-01-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = John; Email = j@mail.com; Password = P@ss123 | System accepts the registration data, creates the member account, saves it in the database, and displays a successful registration message. | Registration database must be available. | None |

### Table 2.4.2 TC-01-002 Verify Sign Up failure when mandatory fields are left blank Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-01-002 |
| Related Feature ID | F001 |
| Objective | Verify Sign Up failure when mandatory fields are left blank |
| Covered Test Coverage Items | TCOV-01-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Email = blank; other mandatory fields contain valid values | System rejects the submission, does not create an account, and displays a required-field error message. | None | None |

### Table 2.4.3 TC-01-003 Verify Sign Up failure when input formats are invalid Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-01-003 |
| Related Feature ID | F001 |
| Objective | Verify Sign Up failure when input formats are invalid |
| Covered Test Coverage Items | TCOV-01-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = John; Email = john.mail.com; Password = P@ss123 | System rejects the submission, does not create an account, and displays an invalid email format error message. | None | None |

### Table 2.4.4 TC-01-004 Verify Sign Up failure when registering with an already existing account Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-01-004 |
| Related Feature ID | F001 |
| Objective | Verify Sign Up failure when registering with an already existing account |
| Covered Test Coverage Items | TCOV-01-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = John; Email = existing@mail.com; Password = P@ss123 | System rejects the registration and displays an account already exists error message. | existing@mail.com must already exist in the database. | TC-01-001 or equivalent seeded account |

## F002 Login

### Table 2.4.5 TC-02-001 Verify successful Login with registered email and correct password Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-02-001 |
| Related Feature ID | F002 |
| Objective | Verify successful Login with registered email and correct password |
| Covered Test Coverage Items | TCOV-02-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Registered email or username = j@mail.com; Password = P@ss123 | System verifies the credentials, creates a user session, and redirects the user to the dashboard. | Registered user account must exist. | TC-01-001 or equivalent seeded account |

### Table 2.4.6 TC-02-002 Verify Login failure with registered email but incorrect password Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-02-002 |
| Related Feature ID | F002 |
| Objective | Verify Login failure with registered email but incorrect password |
| Covered Test Coverage Items | TCOV-02-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Registered email or username = j@mail.com; Password = WrongPass123 | System rejects the login, does not create a session, and displays "Invalid username or password". | Registered user account must exist. | TC-01-001 or equivalent seeded account |

### Table 2.4.7 TC-02-003 Verify Login failure with unregistered email and correct password Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-02-003 |
| Related Feature ID | F002 |
| Objective | Verify Login failure with unregistered email and correct password |
| Covered Test Coverage Items | TCOV-02-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Unregistered email or username = unknown@mail.com; Password = P@ss123 | System rejects the login, does not create a session, and displays "Invalid username or password". | Email must not exist in the database. | None |

### Table 2.4.8 TC-02-004 Verify Login failure with unregistered email and incorrect password Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-02-004 |
| Related Feature ID | F002 |
| Objective | Verify Login failure with unregistered email and incorrect password |
| Covered Test Coverage Items | TCOV-02-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Unregistered email or username = unknown@mail.com; Password = WrongPass123 | System rejects the login, does not create a session, and displays "Invalid username or password". | Email must not exist in the database. | None |

## F003 Logout

### Table 2.4.9 TC-03-001 Verify successful Logout via the "Logout" button Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-03-001 |
| Related Feature ID | F003 |
| Objective | Verify successful Logout via the "Logout" button |
| Covered Test Coverage Items | TCOV-03-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User clicks "Logout" while logged in. | System terminates the active session, removes local cookies or tokens, and redirects the user to the login page. | User must have an active login session. | TC-02-001 |

### Table 2.4.10 TC-03-002 Verify access denial when using the browser "Back" button post-logout Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-03-002 |
| Related Feature ID | F003 |
| Objective | Verify access denial when using the browser "Back" button post-logout |
| Covered Test Coverage Items | TCOV-03-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| After logout, user clicks the browser Back button. | System prevents dashboard access and redirects to the login page or displays an access denied message. | User must be logged out after a previous active session. | TC-03-001 |

### Table 2.4.11 TC-03-003 Verify access denial when entering the Dashboard URL directly post-logout Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-03-003 |
| Related Feature ID | F003 |
| Objective | Verify access denial when entering the Dashboard URL directly post-logout |
| Covered Test Coverage Items | TCOV-03-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| After logout, user enters the Dashboard URL directly. | System blocks direct dashboard access and redirects to the login page or displays an access denied message. | User must be logged out after a previous active session. | TC-03-001 |

## F004 Manage Profile

### Table 2.4.12 TC-04-001 Update profile with valid inputs Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-04-001 |
| Related Feature ID | F004 |
| Objective | Update profile with valid inputs |
| Covered Test Coverage Items | TCOV-04-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Ali; Email = ali@test.com | System validates the data, updates the profile in the database, and displays a success message. | User must be logged in. | TC-02-001 |

### Table 2.4.13 TC-04-002 Update profile with invalid email Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-04-002 |
| Related Feature ID | F004 |
| Objective | Update profile with invalid email |
| Covered Test Coverage Items | TCOV-04-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Email = ali.com | System rejects the update and displays an invalid email format error message. | User must be logged in. | TC-02-001 |

### Table 2.4.14 TC-04-003 Update profile with empty name Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-04-003 |
| Related Feature ID | F004 |
| Objective | Update profile with empty name |
| Covered Test Coverage Items | TCOV-04-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = blank; Email = ali@test.com | System rejects the update and displays a missing name error message. | User must be logged in. | TC-02-001 |

### Table 2.4.15 TC-04-004 Update profile with empty email Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-04-004 |
| Related Feature ID | F004 |
| Objective | Update profile with empty email |
| Covered Test Coverage Items | TCOV-04-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Ali; Email = blank | System rejects the update and displays a missing email error message. | User must be logged in. | TC-02-001 |

### Table 2.4.16 TC-04-005 Access profile without login Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-04-005 |
| Related Feature ID | F004 |
| Objective | Access profile without login |
| Covered Test Coverage Items | TCOV-04-005 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User session = none; user opens Profile page. | System denies access and redirects the user to the login page or displays an unauthorized access message. | No active user session. | None |

## F005 View Book List

### Table 2.4.17 TC-05-001 View book list successfully Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-05-001 |
| Related Feature ID | F005 |
| Objective | View book list successfully |
| Covered Test Coverage Items | TCOV-05-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Books exist in database. | System retrieves book records and displays the book list with basic details. | Database must contain at least one book record. | None |

### Table 2.4.18 TC-05-002 View book list when no books are available Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-05-002 |
| Related Feature ID | F005 |
| Objective | View book list when no books are available |
| Covered Test Coverage Items | TCOV-05-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Database has no books. | System displays "No books available" or an equivalent empty list message. | Book table must be empty for this test. | None |

### Table 2.4.19 TC-05-003 Verify book title, author, and availability are displayed Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-05-003 |
| Related Feature ID | F005 |
| Objective | Verify book title, author, and availability are displayed |
| Covered Test Coverage Items | TCOV-05-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book = Book A | System displays Book A with title, author, and availability information. | Book A must exist in the database with complete display fields. | TC-05-001 or equivalent seeded book |

### Table 2.4.20 TC-05-004 Verify error message when database retrieval fails Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-05-004 |
| Related Feature ID | F005 |
| Objective | Verify error message when database retrieval fails |
| Covered Test Coverage Items | TCOV-05-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Simulated database retrieval failure. | System handles the retrieval failure gracefully and displays an appropriate error message. | Simulate or mock database failure. | None |

## F006 View Book Details

### Table 2.4.21 TC-06-001 View details of selected book successfully Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-06-001 |
| Related Feature ID | F006 |
| Objective | View details of selected book successfully |
| Covered Test Coverage Items | TCOV-06-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101 | System retrieves and displays detailed information for the selected book. | Book ID 101 must exist. | TC-05-001 or equivalent seeded book |

### Table 2.4.22 TC-06-002 View details using invalid book ID Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-06-002 |
| Related Feature ID | F006 |
| Objective | View details using invalid book ID |
| Covered Test Coverage Items | TCOV-06-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 999 | System displays "Book not found" or an equivalent error message. | Book ID 999 must not exist. | None |

### Table 2.4.23 TC-06-003 Verify reserve option appears for available book Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-06-003 |
| Related Feature ID | F006 |
| Objective | Verify reserve option appears for available book |
| Covered Test Coverage Items | TCOV-06-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Availability = Available | System displays the book details and shows the reserve option. | Selected book must be available. | TC-06-001 |

### Table 2.4.24 TC-06-004 Verify unavailable status for unavailable book Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-06-004 |
| Related Feature ID | F006 |
| Objective | Verify unavailable status for unavailable book |
| Covered Test Coverage Items | TCOV-06-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Availability = Unavailable | System displays the book details with unavailable status and does not offer reservation as available. | Selected book must be unavailable. | None |

### Table 2.4.25 TC-06-005 Verify error message when database retrieval fails Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-06-005 |
| Related Feature ID | F006 |
| Objective | Verify error message when database retrieval fails |
| Covered Test Coverage Items | TCOV-06-005 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Simulated database retrieval failure. | System handles the retrieval failure gracefully and displays an appropriate error message. | Simulate or mock database failure. | None |

## F007 Search Book

### Table 2.4.26 TC-07-001 Search with valid keyword Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-07-001 |
| Related Feature ID | F007 |
| Objective | Search with valid keyword |
| Covered Test Coverage Items | TCOV-07-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Search keyword = Harry Potter | System retrieves matching book records and displays search results with availability. | At least one matching book should exist. | None |

### Table 2.4.27 TC-07-002 Search with empty input Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-07-002 |
| Related Feature ID | F007 |
| Objective | Search with empty input |
| Covered Test Coverage Items | TCOV-07-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Search keyword = blank | System rejects the search and displays a validation message for empty input. | None | None |

### Table 2.4.28 TC-07-003 Search with long keyword Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-07-003 |
| Related Feature ID | F007 |
| Objective | Search with long keyword |
| Covered Test Coverage Items | TCOV-07-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Search keyword = 60-character string | System rejects or safely handles the long keyword and displays a validation message if the keyword exceeds the allowed length. | Prepare a 60-character input string. | None |

### Table 2.4.29 TC-07-004 Search with special characters Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-07-004 |
| Related Feature ID | F007 |
| Objective | Search with special characters |
| Covered Test Coverage Items | TCOV-07-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Search keyword = @@@### | System handles the invalid input safely and displays an appropriate validation or no-result message. | None | None |

### Table 2.4.30 TC-07-005 Verify system displays correct search results Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-07-005 |
| Related Feature ID | F007 |
| Objective | Verify system displays correct search results |
| Covered Test Coverage Items | TCOV-07-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Search keyword = Harry Potter | System displays only book records that match the entered keyword and includes availability information. | Known matching search data must exist. | TC-07-001 |

### Table 2.4.31 TC-07-006 Verify validation message for empty input Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-07-006 |
| Related Feature ID | F007 |
| Objective | Verify validation message for empty input |
| Covered Test Coverage Items | TCOV-07-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Search keyword = blank | System displays the correct empty-input validation message and does not perform a search. | None | TC-07-002 |

## F008 Reserve Book

### Table 2.4.32 TC-08-001 Reserve available book successfully Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-08-001 |
| Related Feature ID | F008 |
| Objective | Reserve available book successfully |
| Covered Test Coverage Items | TCOV-08-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101 (available and exists) | System verifies availability, stores the reservation, and displays a success message. | User must be logged in and Book ID 101 must be available. | TC-02-001; TC-06-003 |

### Table 2.4.33 TC-08-002 Attempt to reserve unavailable book Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-08-002 |
| Related Feature ID | F008 |
| Objective | Attempt to reserve unavailable book |
| Covered Test Coverage Items | TCOV-08-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 999 or unavailable book ID | System prevents the reservation and displays an unavailable book message. | User must be logged in and selected book must be unavailable or non-reservable. | TC-02-001 |

### Table 2.4.34 TC-08-003 Reservation limit exceeded Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-08-003 |
| Related Feature ID | F008 |
| Objective | Reservation limit exceeded |
| Covered Test Coverage Items | TCOV-08-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User has 5 reservations; user attempts another reservation. | System prevents the reservation and displays a reservation limit error message. | User account must already have the maximum allowed reservations. | TC-02-001 |

### Table 2.4.35 TC-08-004 Verify system prevents duplicate reservation Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-08-004 |
| Related Feature ID | F008 |
| Objective | Verify system prevents duplicate reservation |
| Covered Test Coverage Items | TCOV-08-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User attempts to reserve a book already reserved by the same user. | System prevents the duplicate reservation and displays an appropriate error message. | User must already have an active reservation for the selected book. | TC-08-001 or equivalent seeded reservation |

### Table 2.4.36 TC-08-005 Verify correct error message when limit reached Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-08-005 |
| Related Feature ID | F008 |
| Objective | Verify correct error message when limit reached |
| Covered Test Coverage Items | TCOV-08-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User has 5 reservations; user clicks Reserve for another available book. | System displays the correct reservation limit reached message. | User account must already have the maximum allowed reservations. | TC-08-003 |

## F009 View Reserved Books

### Table 2.4.37 TC-09-001 View reserved books (main flow) Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-09-001 |
| Related Feature ID | F009 |
| Objective | View reserved books (main flow) |
| Covered Test Coverage Items | TCOV-09-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User has 2 reservations. | System retrieves and displays the user's reserved books with details. | User must be logged in and have two reservation records. | TC-08-001 or equivalent seeded reservations |

### Table 2.4.38 TC-09-002 View when no reservation exists Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-09-002 |
| Related Feature ID | F009 |
| Objective | View when no reservation exists |
| Covered Test Coverage Items | TCOV-09-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User has no reservation records. | System displays an empty reservation list message. | User must be logged in with no reservation records. | TC-02-001 |

### Table 2.4.39 TC-09-003 Unauthorized user access Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-09-003 |
| Related Feature ID | F009 |
| Objective | Unauthorized user access |
| Covered Test Coverage Items | TCOV-09-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User session = none; user opens View Reserved Books page. | System denies access and redirects the user to the login page or displays an access denied message. | No active user session. | None |

### Table 2.4.40 TC-09-004 Verify system displays correct reservation list Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-09-004 |
| Related Feature ID | F009 |
| Objective | Verify system displays correct reservation list |
| Covered Test Coverage Items | TCOV-09-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User has known reservation records. | System displays the correct reservation records for the logged-in user only. | User must be logged in with known reservation data. | TC-09-001 |

### Table 2.4.41 TC-09-005 Verify empty message displayed correctly Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-09-005 |
| Related Feature ID | F009 |
| Objective | Verify empty message displayed correctly |
| Covered Test Coverage Items | TCOV-09-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User has no reservation records. | System displays the correct empty reservation message. | User must be logged in with no reservation records. | TC-09-002 |

## F0010 Add Book

### Table 2.4.42 TC-10-001 Add Book with all valid inputs Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-001 |
| Related Feature ID | F0010 |
| Objective | Add Book with all valid inputs |
| Covered Test Coverage Items | TCOV-10-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Book A; Description = Test Book; Count = 10 | System validates the input, inserts the new book into the database, and displays a success confirmation message. | Admin must be logged in. | Admin login session |

### Table 2.4.43 TC-10-002 Add Book with empty Book Name Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-002 |
| Related Feature ID | F0010 |
| Objective | Add Book with empty Book Name |
| Covered Test Coverage Items | TCOV-10-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = blank; Description = Test Book; Count = 10 | System rejects the submission and displays a validation error for missing book name. | Admin must be logged in. | Admin login session |

### Table 2.4.44 TC-10-003 Add Book with empty Description Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-003 |
| Related Feature ID | F0010 |
| Objective | Add Book with empty Description |
| Covered Test Coverage Items | TCOV-10-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Book A; Description = blank; Count = 10 | System rejects the submission and displays a validation error for missing description. | Admin must be logged in. | Admin login session |

### Table 2.4.45 TC-10-004 Add Book with negative Count Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-004 |
| Related Feature ID | F0010 |
| Objective | Add Book with negative Count |
| Covered Test Coverage Items | TCOV-10-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Book A; Description = Test; Count = -1 | System rejects the submission and displays a validation error for invalid count. | Admin must be logged in. | Admin login session |

### Table 2.4.46 TC-10-005 Add Book with non-numeric Count Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-005 |
| Related Feature ID | F0010 |
| Objective | Add Book with non-numeric Count |
| Covered Test Coverage Items | TCOV-10-005 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Book A; Description = Test; Count = abc | System rejects the submission and displays a validation error requiring numeric count. | Admin must be logged in. | Admin login session |

### Table 2.4.47 TC-10-006 Add Book with duplicate book name Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-006 |
| Related Feature ID | F0010 |
| Objective | Add Book with duplicate book name |
| Covered Test Coverage Items | TCOV-10-006 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Existing Book; Description = Duplicate; Count = 5 | System rejects the submission and displays a duplicate entry error message. | Admin must be logged in and Existing Book must already exist. | Seeded existing book |

### Table 2.4.48 TC-10-007 Verify system rejects submission with all empty fields Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-007 |
| Related Feature ID | F0010 |
| Objective | Verify system rejects submission with all empty fields |
| Covered Test Coverage Items | TCOV-10-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = blank; Description = blank; Count = blank | System rejects the submission and displays validation errors for all required fields. | Admin must be logged in. | Admin login session |

### Table 2.4.49 TC-10-008 Verify system displays error messages correctly Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-008 |
| Related Feature ID | F0010 |
| Objective | Verify system displays error messages correctly |
| Covered Test Coverage Items | TCOV-10-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Book A; Description = blank; Count = 10 | System displays the correct field-specific error message for the invalid input. | Admin must be logged in. | TC-10-003 |

### Table 2.4.50 TC-10-009 Verify successful database insertion Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-10-009 |
| Related Feature ID | F0010 |
| Objective | Verify successful database insertion |
| Covered Test Coverage Items | TCOV-10-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Name = Book A; Description = Test Book; Count = 10 | System inserts the book record into the database and the new book can be found in the inventory or book list. | Admin must be logged in and database must be available. | TC-10-001 |

## F0011 Delete Book

### Table 2.4.51 TC-11-001 Delete existing book successfully Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-001 |
| Related Feature ID | F0011 |
| Objective | Delete existing book successfully |
| Covered Test Coverage Items | TCOV-11-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101 (exists); Confirm = Yes | System deletes the book record, refreshes the inventory view, and displays a success message. | Admin must be logged in and Book ID 101 must exist. | Seeded existing book |

### Table 2.4.52 TC-11-002 Deletion fails due to system/database error Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-002 |
| Related Feature ID | F0011 |
| Objective | Deletion fails due to system/database error |
| Covered Test Coverage Items | TCOV-11-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101; Confirm = Yes; simulated database failure | System aborts the deletion, keeps the book record unchanged, and displays an error message. | Admin must be logged in and database failure must be simulated. | Seeded existing book |

### Table 2.4.53 TC-11-003 Attempt to delete non-existing book Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-003 |
| Related Feature ID | F0011 |
| Objective | Attempt to delete non-existing book |
| Covered Test Coverage Items | TCOV-11-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 999 (does not exist); Confirm = Yes | System aborts deletion and displays an error message indicating the book does not exist. | Admin must be logged in and Book ID 999 must not exist. | None |

### Table 2.4.54 TC-11-004 Unauthorized user attempts deletion Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-004 |
| Related Feature ID | F0011 |
| Objective | Unauthorized user attempts deletion |
| Covered Test Coverage Items | TCOV-11-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User role = normal user; user attempts Delete action. | System blocks the action and displays an unauthorized access error message. | Use a non-admin user session. | Normal user login session |

### Table 2.4.55 TC-11-005 Delete book with confirmation Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-005 |
| Related Feature ID | F0011 |
| Objective | Delete book with confirmation |
| Covered Test Coverage Items | TCOV-11-005 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101; Confirm = Yes | System proceeds with deletion only after confirmation and displays a success message. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.56 TC-11-006 Cancel deletion (no confirmation) Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-006 |
| Related Feature ID | F0011 |
| Objective | Cancel deletion (no confirmation) |
| Covered Test Coverage Items | TCOV-11-005 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101; Confirm = No | System cancels the deletion and keeps the book record unchanged. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.57 TC-11-007 Verify inventory updates after deletion Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-007 |
| Related Feature ID | F0011 |
| Objective | Verify inventory updates after deletion |
| Covered Test Coverage Items | TCOV-11-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101 deleted successfully. | System refreshes the inventory list and the deleted book is no longer displayed. | A successful deletion must be completed first. | TC-11-001 |

### Table 2.4.58 TC-11-008 Verify error message on deletion failure Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-11-008 |
| Related Feature ID | F0011 |
| Objective | Verify error message on deletion failure |
| Covered Test Coverage Items | TCOV-11-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 101; simulated database failure | System displays the correct deletion failure error message. | Admin must be logged in and database failure must be simulated. | TC-11-002 |

## F0012 Edit Book

### Table 2.4.59 TC-12-001 Edit book with valid inputs Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-001 |
| Related Feature ID | F0012 |
| Objective | Edit book with valid inputs |
| Covered Test Coverage Items | TCOV-12-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Title = Updated Book; Quantity = 10 | System validates the input, updates the book details in the database, and displays a success message. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.60 TC-12-002 Edit book with invalid Book ID Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-002 |
| Related Feature ID | F0012 |
| Objective | Edit book with invalid Book ID |
| Covered Test Coverage Items | TCOV-12-002 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Book ID = 999 (does not exist) | System aborts the edit flow and displays "No book found" or an equivalent error message. | Admin must be logged in and Book ID 999 must not exist. | None |

### Table 2.4.61 TC-12-003 Edit book with empty Title Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-003 |
| Related Feature ID | F0012 |
| Objective | Edit book with empty Title |
| Covered Test Coverage Items | TCOV-12-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Title = blank; Quantity = 10 | System rejects the update and displays a validation error for missing title. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.62 TC-12-004 Edit book with empty Quantity Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-004 |
| Related Feature ID | F0012 |
| Objective | Edit book with empty Quantity |
| Covered Test Coverage Items | TCOV-12-004 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Title = Updated Book; Quantity = blank | System rejects the update and displays a validation error for missing quantity. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.63 TC-12-005 Edit book with negative Quantity Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-005 |
| Related Feature ID | F0012 |
| Objective | Edit book with negative Quantity |
| Covered Test Coverage Items | TCOV-12-005 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Quantity = -5 | System rejects the update and displays a validation error requiring a positive quantity. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.64 TC-12-006 Edit book with non-numeric Quantity Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-006 |
| Related Feature ID | F0012 |
| Objective | Edit book with non-numeric Quantity |
| Covered Test Coverage Items | TCOV-12-006 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Quantity = abc | System rejects the update and displays a validation error requiring numeric quantity. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.65 TC-12-007 Partial update of book details Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-007 |
| Related Feature ID | F0012 |
| Objective | Partial update of book details |
| Covered Test Coverage Items | TCOV-12-007 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Change Description only; leave other fields unchanged. | System updates only the selected field and keeps unchanged fields with their previous values. | Admin must be logged in and target book must exist. | Seeded existing book |

### Table 2.4.66 TC-12-008 Unauthorized user attempts edit Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-008 |
| Related Feature ID | F0012 |
| Objective | Unauthorized user attempts edit |
| Covered Test Coverage Items | TCOV-12-008 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| User role = normal user; user attempts Edit action. | System blocks the action and displays an unauthorized access error message. | Use a non-admin user session. | Normal user login session |

### Table 2.4.67 TC-12-009 Verify error message on validation failure Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-009 |
| Related Feature ID | F0012 |
| Objective | Verify error message on validation failure |
| Covered Test Coverage Items | TCOV-12-003 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Title = blank; Quantity = 10 | System displays the correct field-specific validation error message. | Admin must be logged in and target book must exist. | TC-12-003 |

### Table 2.4.68 TC-12-010 Verify successful update in database Test Case

| Field | Value |
|---|---|
| Test Case ID | TC-12-010 |
| Related Feature ID | F0012 |
| Objective | Verify successful update in database |
| Covered Test Coverage Items | TCOV-12-001 |

| Input | Expected Result | Special Procedural Requirements | Intercase Dependency |
|---|---|---|---|
| Title = Updated Book; Quantity = 10 | System persists the updated values in the database and displays the updated details when the book is viewed again. | Admin must be logged in and database must be available. | TC-12-001 |
