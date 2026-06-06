# Test Incident Report

Tester: Yong Di Lun
Scope: Functional requirements F001 to F0012 and non-functional requirements REQ_Q001 to REQ_Q004.
References: LMS_TPS_1.0.0, LMS_TL_1.0.0, LMS_TSR_1.0.0, LMS_NFR_1.0.0

## Non-Functional Requirement Coverage

| Requirement ID | Category | Test Case ID | Test Procedure ID | Pass/Fail | Incident ID |
|---|---|---|---|---|---|
| REQ_Q001 | Reliability & Accuracy | TC-Q001 | TP-Q-001 | Pass | - |
| REQ_Q002 | Reliability & Accuracy | TC-Q002 | TP-Q-002 | Fail | LMS_TIR_1.0/TIR-029 |
| REQ_Q003 | Security | TC-Q003 | TP-Q-003 | Fail | LMS_TIR_1.0/TIR-030 |
| REQ_Q004 | Security | TC-Q004 | TP-Q-004 | Fail | LMS_TIR_1.0/TIR-031 |

## Incidents

## LMS_TIR_1.0/TIR-001 - TC-02-002

Summary: Verify Login failure with registered email but incorrect password
Severity: Mission Critical
Status: Open
Test Procedure: TP-02-002
Expected Result: System rejects the login, does not create a session, and displays "Invalid username or password".
Actual Result: Registered email with wrong password was accepted if this row fails.
Corrective Action: Fix password verification so the supplied password is hashed and compared correctly. Add regression tests for wrong-password login.

## LMS_TIR_1.0/TIR-002 - TC-04-003

Summary: Update profile with empty name
Severity: Major
Status: Open
Test Procedure: TP-04-002
Expected Result: System rejects the update and displays a missing name error message.
Actual Result: Empty name was submitted through the profile update form.
Corrective Action: Add server-side validation for profile name and email fields before updating user records.

## LMS_TIR_1.0/TIR-003 - TC-04-004

Summary: Update profile with empty email
Severity: Major
Status: Open
Test Procedure: TP-04-002
Expected Result: System rejects the update and displays a missing email error message.
Actual Result: Empty email was submitted through the profile update form.
Corrective Action: Add server-side validation for profile name and email fields before updating user records.

## LMS_TIR_1.0/TIR-004 - TC-05-003

Summary: Verify book title, author, and availability are displayed
Severity: Minor
Status: Open
Test Procedure: TP-05-001
Expected Result: System displays Book A with title, author, and availability information.
Actual Result: Book list displayed title, author, and availability/count.
Corrective Action: Ensure book list displays required title, author, availability/count fields and catches database retrieval errors gracefully.

## LMS_TIR_1.0/TIR-005 - TC-05-004

Summary: Verify error message when database retrieval fails
Severity: Mission Critical
Status: Open
Test Procedure: TP-05-002
Expected Result: System handles the retrieval failure gracefully and displays an appropriate error message.
Actual Result: Simulated BookManager.list database failure returned HTTP 500. The system returned an unhandled server error.
Corrective Action: Ensure book list displays required title, author, availability/count fields and catches database retrieval errors gracefully.

## LMS_TIR_1.0/TIR-006 - TC-06-005

Summary: Verify error message when database retrieval fails
Severity: Mission Critical
Status: Open
Test Procedure: TP-06-003
Expected Result: System handles the retrieval failure gracefully and displays an appropriate error message.
Actual Result: Simulated BookManager.getBook database failure returned HTTP 500. The system returned an unhandled server error.
Corrective Action: Catch book detail retrieval exceptions and display a controlled user-facing error message instead of HTTP 500.

## LMS_TIR_1.0/TIR-007 - TC-07-002

Summary: Search with empty input
Severity: Major
Status: Open
Test Procedure: TP-07-002
Expected Result: System rejects the search and displays a validation message for empty input.
Actual Result: Empty search input was submitted from the home search form.
Corrective Action: Add search input validation for empty keyword, maximum length, and validation message display.

## LMS_TIR_1.0/TIR-008 - TC-07-003

Summary: Search with long keyword
Severity: Major
Status: Open
Test Procedure: TP-07-003
Expected Result: System rejects or safely handles the long keyword and displays a validation message if the keyword exceeds the allowed length.
Actual Result: A 60-character keyword was submitted.
Corrective Action: Add search input validation for empty keyword, maximum length, and validation message display.

## LMS_TIR_1.0/TIR-009 - TC-07-006

Summary: Verify validation message for empty input
Severity: Major
Status: Open
Test Procedure: TP-07-002
Expected Result: System displays the correct empty-input validation message and does not perform a search.
Actual Result: Empty search validation message was checked.
Corrective Action: Add search input validation for empty keyword, maximum length, and validation message display.

## LMS_TIR_1.0/TIR-010 - TC-08-003

Summary: Reservation limit exceeded
Severity: Major
Status: Open
Test Procedure: TP-08-003
Expected Result: System prevents the reservation and displays a reservation limit error message.
Actual Result: A user with five reservations attempted another reservation.
Corrective Action: Enforce reservation limit and duplicate reservation checks in backend logic and display clear reservation failure messages.

## LMS_TIR_1.0/TIR-011 - TC-08-004

Summary: Verify system prevents duplicate reservation
Severity: Major
Status: Open
Test Procedure: TP-08-002
Expected Result: System prevents the duplicate reservation and displays an appropriate error message.
Actual Result: Duplicate reservation route was invoked directly with an authenticated user session.
Corrective Action: Enforce reservation limit and duplicate reservation checks in backend logic and display clear reservation failure messages.

## LMS_TIR_1.0/TIR-012 - TC-08-005

Summary: Verify correct error message when limit reached
Severity: Major
Status: Open
Test Procedure: TP-08-003
Expected Result: System displays the correct reservation limit reached message.
Actual Result: Reservation limit message was checked after exceeding the limit.
Corrective Action: Enforce reservation limit and duplicate reservation checks in backend logic and display clear reservation failure messages.

## LMS_TIR_1.0/TIR-013 - TC-10-001

Summary: Add Book with all valid inputs
Severity: Mission Critical
Status: Open
Test Procedure: TP-10-001
Expected Result: System validates the input, inserts the new book into the database, and displays a success confirmation message.
Actual Result: Admin Add Book route was submitted with valid data.
Corrective Action: Implement the admin Add Book submit route correctly and add server-side validation for required fields, quantity limits, and duplicate names.

## LMS_TIR_1.0/TIR-014 - TC-10-009

Summary: Verify successful database insertion
Severity: Mission Critical
Status: Open
Test Procedure: TP-10-001
Expected Result: System inserts the book record into the database and the new book can be found in the inventory or book list.
Actual Result: Database insertion was checked after valid Add Book submission.
Corrective Action: Implement the admin Add Book submit route correctly and add server-side validation for required fields, quantity limits, and duplicate names.

## LMS_TIR_1.0/TIR-015 - TC-10-003

Summary: Add Book with empty Description
Severity: Minor
Status: Open
Test Procedure: TP-10-002
Expected Result: System rejects the submission and displays a validation error for missing description.
Actual Result: Description field was inspected for required validation.
Corrective Action: Implement the admin Add Book submit route correctly and add server-side validation for required fields, quantity limits, and duplicate names.

## LMS_TIR_1.0/TIR-016 - TC-10-004

Summary: Add Book with negative Count
Severity: Major
Status: Open
Test Procedure: TP-10-003
Expected Result: System rejects the submission and displays a validation error for invalid count.
Actual Result: Quantity field was inspected for a minimum value rule.
Corrective Action: Implement the admin Add Book submit route correctly and add server-side validation for required fields, quantity limits, and duplicate names.

## LMS_TIR_1.0/TIR-017 - TC-10-006

Summary: Add Book with duplicate book name
Severity: Major
Status: Open
Test Procedure: TP-10-003
Expected Result: System rejects the submission and displays a duplicate entry error message.
Actual Result: Duplicate book handling was checked against the real Add Book route/page.
Corrective Action: Implement the admin Add Book submit route correctly and add server-side validation for required fields, quantity limits, and duplicate names.

## LMS_TIR_1.0/TIR-018 - TC-10-008

Summary: Verify system displays error messages correctly
Severity: Minor
Status: Open
Test Procedure: TP-10-002
Expected Result: System displays the correct field-specific error message for the invalid input.
Actual Result: Field-specific error message was checked for missing Description.
Corrective Action: Implement the admin Add Book submit route correctly and add server-side validation for required fields, quantity limits, and duplicate names.

## LMS_TIR_1.0/TIR-019 - TC-11-002

Summary: Deletion fails due to system/database error
Severity: Mission Critical
Status: Open
Test Procedure: TP-11-003
Expected Result: System aborts the deletion, keeps the book record unchanged, and displays an error message.
Actual Result: Simulated BookManager.delete failure returned HTTP 500; target book still exists = True. The system returned an unhandled server error.
Corrective Action: Add explicit delete confirmation, non-existing book handling, and database exception handling for admin deletion.

## LMS_TIR_1.0/TIR-020 - TC-11-003

Summary: Attempt to delete non-existing book
Severity: Major
Status: Open
Test Procedure: TP-11-003
Expected Result: System aborts deletion and displays an error message indicating the book does not exist.
Actual Result: Delete non-existing book returned HTTP 302.
Corrective Action: Add explicit delete confirmation, non-existing book handling, and database exception handling for admin deletion.

## LMS_TIR_1.0/TIR-021 - TC-11-005

Summary: Delete book with confirmation
Severity: Minor
Status: Open
Test Procedure: TP-11-001
Expected Result: System proceeds with deletion only after confirmation and displays a success message.
Actual Result: Admin delete link was inspected for an explicit confirmation step.
Corrective Action: Add explicit delete confirmation, non-existing book handling, and database exception handling for admin deletion.

## LMS_TIR_1.0/TIR-022 - TC-11-006

Summary: Cancel deletion (no confirmation)
Severity: Minor
Status: Open
Test Procedure: TP-11-002
Expected Result: System cancels the deletion and keeps the book record unchanged.
Actual Result: Cancel deletion flow was checked; no confirmation dialog is implemented.
Corrective Action: Add explicit delete confirmation, non-existing book handling, and database exception handling for admin deletion.

## LMS_TIR_1.0/TIR-023 - TC-11-008

Summary: Verify error message on deletion failure
Severity: Mission Critical
Status: Open
Test Procedure: TP-11-003
Expected Result: System displays the correct deletion failure error message.
Actual Result: Deletion failure message check used simulated delete failure response HTTP 500. The system returned an unhandled server error.
Corrective Action: Add explicit delete confirmation, non-existing book handling, and database exception handling for admin deletion.

## LMS_TIR_1.0/TIR-024 - TC-12-001

Summary: Edit book with valid inputs
Severity: Mission Critical
Status: Open
Test Procedure: TP-12-001
Expected Result: System validates the input, updates the book details in the database, and displays a success message.
Actual Result: Admin edit route was submitted with valid values.
Corrective Action: Implement admin Edit Book POST persistence and validation for invalid book ID, quantity constraints, and partial updates.

## LMS_TIR_1.0/TIR-025 - TC-12-010

Summary: Verify successful update in database
Severity: Mission Critical
Status: Open
Test Procedure: TP-12-001
Expected Result: System persists the updated values in the database and displays the updated details when the book is viewed again.
Actual Result: Database was checked after valid edit submission.
Corrective Action: Implement admin Edit Book POST persistence and validation for invalid book ID, quantity constraints, and partial updates.

## LMS_TIR_1.0/TIR-026 - TC-12-002

Summary: Edit book with invalid Book ID
Severity: Major
Status: Open
Test Procedure: TP-12-002
Expected Result: System aborts the edit flow and displays "No book found" or an equivalent error message.
Actual Result: Invalid edit Book ID returned HTTP 200.
Corrective Action: Implement admin Edit Book POST persistence and validation for invalid book ID, quantity constraints, and partial updates.

## LMS_TIR_1.0/TIR-027 - TC-12-005

Summary: Edit book with negative Quantity
Severity: Major
Status: Open
Test Procedure: TP-12-004
Expected Result: System rejects the update and displays a validation error requiring a positive quantity.
Actual Result: Quantity field was inspected for a positive/minimum value rule.
Corrective Action: Implement admin Edit Book POST persistence and validation for invalid book ID, quantity constraints, and partial updates.

## LMS_TIR_1.0/TIR-028 - TC-12-007

Summary: Partial update of book details
Severity: Mission Critical
Status: Open
Test Procedure: TP-12-001
Expected Result: System updates only the selected field and keeps unchanged fields with their previous values.
Actual Result: Description-only edit was submitted through the edit route.
Corrective Action: Implement admin Edit Book POST persistence and validation for invalid book ID, quantity constraints, and partial updates.

## LMS_TIR_1.0/TIR-029 - TC-Q002

Summary: Verify database foreign key integrity between User, Book, and Reservation tables
Severity: Major
Status: Open
Test Procedure: TP-Q-002
Expected Result: Database rejects orphaned Reservation records and defines foreign key constraints for user_id and book_id.
Actual Result: Foreign keys found = (); orphan reservation insert succeeded = True.
Corrective Action: Add foreign key constraints between reservation records and the related user/book records. Remove orphaned records and rerun integrity tests.

## LMS_TIR_1.0/TIR-030 - TC-Q003

Summary: Verify secure password hashing and salting before database storage
Severity: Mission Critical
Status: Open
Test Procedure: TP-Q-003
Expected Result: Passwords are not stored in plain text and each password hash uses a secure salted algorithm such as bcrypt.
Actual Result: Stored hashes = ['025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8']; plaintext absent = True; bcrypt-like = False; unique hashes = False.
Corrective Action: Replace the current password storage method with a secure salted hashing algorithm such as bcrypt. Force password reset or migration for existing test accounts, then rerun authentication/security tests.

## LMS_TIR_1.0/TIR-031 - TC-Q004

Summary: Verify HTTPS/TLS 1.2 or higher is used for client-to-server interactions
Severity: Mission Critical
Status: Open
Test Procedure: TP-Q-004
Expected Result: Login and profile traffic are served through HTTPS/TLS 1.2 or higher.
Actual Result: HTTP login URL = http://127.0.0.1:5000/signin; HTTPS endpoint available = False; HTTPS error = SSLError: HTTPSConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded with url: /signin (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1028)'))).
Corrective Action: Deploy the LMS behind HTTPS/TLS 1.2 or higher and redirect sensitive HTTP routes to HTTPS. Rerun login/profile traffic verification.
