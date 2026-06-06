# 2.3 Library Management System Test Procedure

The following test procedures are designed to execute and cover all identified LMS test cases for features F001 through F0012.

## 2.3.1 F001 Sign Up Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. The Sign Up page must be accessible from the browser.
3. The test database must allow test accounts to be created and removed.
4. An existing account with email existing@mail.com must be available for duplicate-account testing.

### Table 2.3.1.1 Sign Up Main Flow and Input Validation Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-01-001 |
| Objective | Sign Up Main Flow and Input Validation |
| Test Cases To Be Executed | TC-01-001, TC-01-002, TC-01-003 |
| Set Up | 1. Open the LMS Sign Up page.<br>2. Input Name = John, Email = j@mail.com, and Password = P@ss123, then submit the form. [TC-01-001]<br>3. Return to the Sign Up page and leave Email blank while other mandatory fields contain valid values, then submit. [TC-01-002]<br>4. Return to the Sign Up page and input Email = john.mail.com, then submit. [TC-01-003] |
| Wrap Up | 1. Remove the test account j@mail.com if it was created.<br>2. Clear browser form/session data. |

### Table 2.3.1.2 Sign Up Duplicate Account Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-01-002 |
| Objective | Sign Up Alternate Flow - Duplicate Account |
| Test Cases To Be Executed | TC-01-004 |
| Set Up | 1. Confirm that existing@mail.com already exists in the test database.<br>2. Open the LMS Sign Up page.<br>3. Input Name = John, Email = existing@mail.com, and Password = P@ss123, then submit. [TC-01-004] |
| Wrap Up | 1. Keep the seeded duplicate account unchanged.<br>2. Clear browser form/session data. |

## 2.3.2 F002 Login Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. A registered member account j@mail.com with password P@ss123 must exist.
3. unknown@mail.com must not exist in the database.
4. The Login page must be accessible from the browser.

### Table 2.3.2.1 Login Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-02-001 |
| Objective | Login Main Flow - Registered Email and Correct Password |
| Test Cases To Be Executed | TC-02-001 |
| Set Up | 1. Open the LMS Login page.<br>2. Input registered email or username = j@mail.com.<br>3. Input Password = P@ss123, then click Login. [TC-02-001] |
| Wrap Up | 1. Log out from the dashboard.<br>2. Clear browser session data if needed. |

### Table 2.3.2.2 Login Invalid Credential Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-02-002 |
| Objective | Login Alternate Flows - Invalid Credential Combinations |
| Test Cases To Be Executed | TC-02-002, TC-02-003, TC-02-004 |
| Set Up | 1. Open the LMS Login page.<br>2. Input registered email or username = j@mail.com and Password = WrongPass123, then click Login. [TC-02-002]<br>3. Clear the login form.<br>4. Input unregistered email or username = unknown@mail.com and Password = P@ss123, then click Login. [TC-02-003]<br>5. Clear the login form.<br>6. Input unregistered email or username = unknown@mail.com and Password = WrongPass123, then click Login. [TC-02-004] |
| Wrap Up | 1. Confirm no user session is created.<br>2. Clear browser session data. |

## 2.3.3 F003 Logout Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running.
2. A valid user account must exist.
3. User must be able to log in and access the dashboard.
4. Browser Back button and direct dashboard URL access must be available for testing.

### Table 2.3.3.1 Logout Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-03-001 |
| Objective | Logout Main Flow |
| Test Cases To Be Executed | TC-03-001 |
| Set Up | 1. Log in using a valid user account.<br>2. Confirm that the dashboard is displayed.<br>3. Click the Logout button. [TC-03-001] |
| Wrap Up | 1. Confirm the user is redirected to the Login page.<br>2. Clear any remaining cookies or tokens if required. |

### Table 2.3.3.2 Logout State Protection Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-03-002 |
| Objective | Logout State Protection - Back Button and Direct URL Access |
| Test Cases To Be Executed | TC-03-002, TC-03-003 |
| Set Up | 1. Execute TP-03-001 to log out from an active session.<br>2. Press the browser Back button after logout. [TC-03-002]<br>3. Return to the Login page if needed.<br>4. Enter the Dashboard URL directly in the browser address bar. [TC-03-003] |
| Wrap Up | 1. Confirm the user remains logged out.<br>2. Clear browser session data. |

## 2.3.4 F004 Manage Profile Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. A valid member account must exist.
3. The user must be logged in for profile update procedures.
4. No active session must exist for unauthorized profile access testing.

### Table 2.3.4.1 Manage Profile Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-04-001 |
| Objective | Manage Profile Main Flow - Valid Profile Update |
| Test Cases To Be Executed | TC-04-001 |
| Set Up | 1. Log in using a valid member account.<br>2. Open the Profile page.<br>3. Input Name = Ali and Email = ali@test.com, then submit the update. [TC-04-001] |
| Wrap Up | 1. Restore the original profile data if required.<br>2. Log out from the member account. |

### Table 2.3.4.2 Manage Profile Input Validation Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-04-002 |
| Objective | Manage Profile Alternate Flows - Invalid or Missing Input |
| Test Cases To Be Executed | TC-04-002, TC-04-003, TC-04-004 |
| Set Up | 1. Log in using a valid member account and open the Profile page.<br>2. Input Email = ali.com and submit the update. [TC-04-002]<br>3. Return to edit mode and input Name = blank with Email = ali@test.com, then submit. [TC-04-003]<br>4. Return to edit mode and input Name = Ali with Email = blank, then submit. [TC-04-004] |
| Wrap Up | 1. Confirm profile data remains unchanged after rejected updates.<br>2. Log out from the member account. |

### Table 2.3.4.3 Manage Profile Unauthorized Access Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-04-003 |
| Objective | Manage Profile Alternate Flow - Unauthorized Access |
| Test Cases To Be Executed | TC-04-005 |
| Set Up | 1. Ensure no user is logged in.<br>2. Open the Profile page URL directly or click Profile without a session. [TC-04-005] |
| Wrap Up | 1. Confirm no profile data is displayed to the unauthorized user.<br>2. Clear browser session data. |

## 2.3.5 F005 View Book List Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. A test dataset with at least one book must be available for main-flow testing.
3. A test state with no books must be available for empty-list testing.
4. Database retrieval failure must be simulated or mocked for error testing.

### Table 2.3.5.1 View Book List Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-05-001 |
| Objective | View Book List Main Flow and Book Summary Display |
| Test Cases To Be Executed | TC-05-001, TC-05-003 |
| Set Up | 1. Prepare the database with Book A and at least one available book record.<br>2. Open the LMS book list page.<br>3. Click View Book List or navigate to the book list view. [TC-05-001]<br>4. Verify that Book A displays title, author, and availability information. [TC-05-003] |
| Wrap Up | 1. Leave the seeded book data available for later book-detail tests. |

### Table 2.3.5.2 View Book List Empty and Error Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-05-002 |
| Objective | View Book List Alternate Flows - Empty List and Retrieval Error |
| Test Cases To Be Executed | TC-05-002, TC-05-004 |
| Set Up | 1. Prepare a test state where the book table has no records.<br>2. Open the book list page. [TC-05-002]<br>3. Restore or switch to a test state that supports database error simulation.<br>4. Simulate database retrieval failure and open the book list page again. [TC-05-004] |
| Wrap Up | 1. Restore normal database connectivity and standard book test data. |

## 2.3.6 F006 View Book Details Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. Book ID 101 must exist for successful detail testing.
3. At least one available and one unavailable book record must be available.
4. Book ID 999 must not exist for invalid book testing.
5. Database retrieval failure must be simulated or mocked for error testing.

### Table 2.3.6.1 View Book Details Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-06-001 |
| Objective | View Book Details Main Flow and Available Book Reserve Option |
| Test Cases To Be Executed | TC-06-001, TC-06-003 |
| Set Up | 1. Open the book list page.<br>2. Select Book ID = 101. [TC-06-001]<br>3. Confirm the selected book has Availability = Available.<br>4. Verify that the reserve option is displayed. [TC-06-003] |
| Wrap Up | 1. Return to the book list page. |

### Table 2.3.6.2 View Book Details Unavailable Book Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-06-002 |
| Objective | View Book Details Alternate Flow - Unavailable Book |
| Test Cases To Be Executed | TC-06-004 |
| Set Up | 1. Open the book list page.<br>2. Select a book with Availability = Unavailable.<br>3. Open the selected book details. [TC-06-004] |
| Wrap Up | 1. Return to the book list page. |

### Table 2.3.6.3 View Book Details Invalid and Error Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-06-003 |
| Objective | View Book Details Alternate Flows - Invalid Book ID and Retrieval Error |
| Test Cases To Be Executed | TC-06-002, TC-06-005 |
| Set Up | 1. Open a book details URL with Book ID = 999. [TC-06-002]<br>2. Restore the normal details view if required.<br>3. Simulate database retrieval failure and request a valid book details page. [TC-06-005] |
| Wrap Up | 1. Restore normal database connectivity. |

## 2.3.7 F007 Search Book Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. At least one book matching Harry Potter must exist for valid search testing.
3. The Search Book page or search bar must be accessible.
4. A 60-character search string must be prepared.

### Table 2.3.7.1 Search Book Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-07-001 |
| Objective | Search Book Main Flow and Result Accuracy |
| Test Cases To Be Executed | TC-07-001, TC-07-005 |
| Set Up | 1. Open the Search Book page.<br>2. Input search keyword = Harry Potter and click Search. [TC-07-001]<br>3. Verify that only matching search results are displayed with availability information. [TC-07-005] |
| Wrap Up | 1. Clear the search field. |

### Table 2.3.7.2 Search Book Empty Input Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-07-002 |
| Objective | Search Book Alternate Flow - Empty Input Validation |
| Test Cases To Be Executed | TC-07-002, TC-07-006 |
| Set Up | 1. Open the Search Book page.<br>2. Leave the search keyword blank and click Search. [TC-07-002]<br>3. Verify that the correct validation message is displayed for empty input. [TC-07-006] |
| Wrap Up | 1. Clear the search field. |

### Table 2.3.7.3 Search Book Invalid Input Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-07-003 |
| Objective | Search Book Alternate Flows - Long Keyword and Special Characters |
| Test Cases To Be Executed | TC-07-003, TC-07-004 |
| Set Up | 1. Open the Search Book page.<br>2. Input a 60-character string and click Search. [TC-07-003]<br>3. Clear the search field.<br>4. Input @@@### and click Search. [TC-07-004] |
| Wrap Up | 1. Clear the search field and return to the default book search page. |

## 2.3.8 F008 Reserve Book Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. A valid user must be logged in.
3. Book ID 101 must exist and be available for successful reservation testing.
4. An unavailable or already reserved book must be available for negative testing.
5. A user account with five existing reservations must be prepared for limit testing.

### Table 2.3.8.1 Reserve Book Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-08-001 |
| Objective | Reserve Book Main Flow - Available Book |
| Test Cases To Be Executed | TC-08-001 |
| Set Up | 1. Log in using a valid user account.<br>2. Open the details page for Book ID = 101.<br>3. Click Reserve for the available book. [TC-08-001] |
| Wrap Up | 1. Remove or reset the reservation record if needed for repeat testing. |

### Table 2.3.8.2 Reserve Book Unavailable and Duplicate Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-08-002 |
| Objective | Reserve Book Alternate Flows - Unavailable and Duplicate Reservation |
| Test Cases To Be Executed | TC-08-002, TC-08-004 |
| Set Up | 1. Log in using a valid user account.<br>2. Open the details page for an unavailable book or Book ID = 999, then click Reserve. [TC-08-002]<br>3. Prepare a book already reserved by the same user.<br>4. Attempt to reserve the same book again. [TC-08-004] |
| Wrap Up | 1. Reset duplicate reservation test data if needed. |

### Table 2.3.8.3 Reserve Book Limit Exceeded Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-08-003 |
| Objective | Reserve Book Alternate Flow - Reservation Limit Exceeded |
| Test Cases To Be Executed | TC-08-003, TC-08-005 |
| Set Up | 1. Log in using a user account that already has five reservations.<br>2. Open the details page for another available book.<br>3. Click Reserve. [TC-08-003]<br>4. Verify that the correct reservation limit reached message is displayed. [TC-08-005] |
| Wrap Up | 1. Restore reservation count to the standard test state. |

## 2.3.9 F009 View Reserved Books Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. A valid user account with two reservations must be available.
3. A valid user account with no reservations must be available.
4. No active session must exist for unauthorized access testing.

### Table 2.3.9.1 View Reserved Books Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-09-001 |
| Objective | View Reserved Books Main Flow and List Accuracy |
| Test Cases To Be Executed | TC-09-001, TC-09-004 |
| Set Up | 1. Log in using a user account that has two reservation records.<br>2. Click View Reserved Books. [TC-09-001]<br>3. Verify that the displayed reservation list matches the user's reservation records only. [TC-09-004] |
| Wrap Up | 1. Log out from the user account. |

### Table 2.3.9.2 View Reserved Books Empty List Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-09-002 |
| Objective | View Reserved Books Alternate Flow - No Reservation |
| Test Cases To Be Executed | TC-09-002, TC-09-005 |
| Set Up | 1. Log in using a user account with no reservation records.<br>2. Click View Reserved Books. [TC-09-002]<br>3. Verify that the correct empty reservation message is displayed. [TC-09-005] |
| Wrap Up | 1. Log out from the user account. |

### Table 2.3.9.3 View Reserved Books Unauthorized Access Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-09-003 |
| Objective | View Reserved Books Alternate Flow - Unauthorized Access |
| Test Cases To Be Executed | TC-09-003 |
| Set Up | 1. Ensure no user is logged in.<br>2. Open the View Reserved Books page directly. [TC-09-003] |
| Wrap Up | 1. Confirm no reservation data is exposed.<br>2. Clear browser session data. |

## 2.3.10 F0010 Add Book Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. An admin account must be available and logged in.
3. The Add Book page must be accessible from the admin dashboard.
4. A book named Existing Book must already exist for duplicate-entry testing.
5. Book A test records must be removable after successful insertion tests.

### Table 2.3.10.1 Add Book Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-10-001 |
| Objective | Add Book Main Flow and Database Insertion |
| Test Cases To Be Executed | TC-10-001, TC-10-009 |
| Set Up | 1. Log in as an admin user.<br>2. Open the Add Book page.<br>3. Input Name = Book A, Description = Test Book, and Count = 10, then click Add. [TC-10-001]<br>4. Open the inventory or book list and verify that Book A exists in the database/list. [TC-10-009] |
| Wrap Up | 1. Remove Book A if it is not needed for later tests. |

### Table 2.3.10.2 Add Book Missing Field Validation Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-10-002 |
| Objective | Add Book Alternate Flows - Missing Required Fields |
| Test Cases To Be Executed | TC-10-002, TC-10-003, TC-10-007, TC-10-008 |
| Set Up | 1. Log in as an admin user and open the Add Book page.<br>2. Input Name = blank, Description = Test Book, Count = 10, then click Add. [TC-10-002]<br>3. Input Name = Book A, Description = blank, Count = 10, then click Add. [TC-10-003]<br>4. Input Name = blank, Description = blank, Count = blank, then click Add. [TC-10-007]<br>5. Verify that field-specific error messages are displayed correctly for the missing Description scenario. [TC-10-008] |
| Wrap Up | 1. Confirm no invalid book record is inserted.<br>2. Clear the Add Book form. |

### Table 2.3.10.3 Add Book Invalid Count and Duplicate Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-10-003 |
| Objective | Add Book Alternate Flows - Invalid Count and Duplicate Entry |
| Test Cases To Be Executed | TC-10-004, TC-10-005, TC-10-006 |
| Set Up | 1. Log in as an admin user and open the Add Book page.<br>2. Input Name = Book A, Description = Test, Count = -1, then click Add. [TC-10-004]<br>3. Input Name = Book A, Description = Test, Count = abc, then click Add. [TC-10-005]<br>4. Input Name = Existing Book, Description = Duplicate, Count = 5, then click Add. [TC-10-006] |
| Wrap Up | 1. Confirm no invalid or duplicate book record is inserted.<br>2. Clear the Add Book form. |

## 2.3.11 F0011 Delete Book Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. An admin account must be available and logged in for authorized deletion procedures.
3. A normal user account must be available for unauthorized deletion testing.
4. Book ID 101 or an equivalent existing book must be prepared for deletion tests.
5. Book ID 999 must not exist for invalid book ID testing.
6. Database deletion failure must be simulated or mocked for error testing.

### Table 2.3.11.1 Delete Book Confirmed Deletion Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-11-001 |
| Objective | Delete Book Main Flow - Confirmed Deletion and Inventory Update |
| Test Cases To Be Executed | TC-11-001, TC-11-005, TC-11-007 |
| Set Up | 1. Log in as an admin user.<br>2. Open the book management list.<br>3. Select Delete for Book ID = 101.<br>4. Choose Confirm = Yes. [TC-11-005]<br>5. Verify the book is deleted successfully. [TC-11-001]<br>6. Verify the inventory refreshes and the deleted book is no longer displayed. [TC-11-007] |
| Wrap Up | 1. Restore the deleted book record if required for later tests. |

### Table 2.3.11.2 Delete Book Cancel Deletion Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-11-002 |
| Objective | Delete Book Alternate Flow - Cancel Deletion |
| Test Cases To Be Executed | TC-11-006 |
| Set Up | 1. Log in as an admin user.<br>2. Open the book management list.<br>3. Select Delete for an existing book.<br>4. Choose Confirm = No. [TC-11-006] |
| Wrap Up | 1. Confirm the selected book still exists in the inventory. |

### Table 2.3.11.3 Delete Book Invalid and Error Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-11-003 |
| Objective | Delete Book Alternate Flows - Invalid Book ID and Database Error |
| Test Cases To Be Executed | TC-11-002, TC-11-003, TC-11-008 |
| Set Up | 1. Log in as an admin user.<br>2. Attempt to delete Book ID = 999 and confirm deletion. [TC-11-003]<br>3. Prepare an existing book and simulate database deletion failure.<br>4. Attempt to delete the existing book and confirm deletion. [TC-11-002]<br>5. Verify that the correct deletion failure error message is displayed. [TC-11-008] |
| Wrap Up | 1. Restore normal database connectivity.<br>2. Confirm no unintended book record was removed. |

### Table 2.3.11.4 Delete Book Unauthorized Access Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-11-004 |
| Objective | Delete Book Alternate Flow - Unauthorized Access |
| Test Cases To Be Executed | TC-11-004 |
| Set Up | 1. Log in using a normal user account.<br>2. Attempt to access the delete function or click Delete for a book. [TC-11-004] |
| Wrap Up | 1. Log out from the normal user account.<br>2. Confirm no book record was deleted. |

## 2.3.12 F0012 Edit Book Test Procedure

Prior to execution of the following test procedures, these special requirements must be prepared:
1. LMS application must be running and connected to the test database.
2. An admin account must be available and logged in for authorized edit procedures.
3. A normal user account must be available for unauthorized edit testing.
4. An existing editable book record must be prepared.
5. Book ID 999 must not exist for invalid book ID testing.

### Table 2.3.12.1 Edit Book Main Flow Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-12-001 |
| Objective | Edit Book Main Flow, Partial Update, and Database Verification |
| Test Cases To Be Executed | TC-12-001, TC-12-007, TC-12-010 |
| Set Up | 1. Log in as an admin user.<br>2. Open the edit page for an existing book.<br>3. Input Title = Updated Book and Quantity = 10, then click Update. [TC-12-001]<br>4. Open the edit page again and change Description only, then click Update. [TC-12-007]<br>5. Open the book details or database-backed list and verify that the updated values are stored. [TC-12-010] |
| Wrap Up | 1. Restore the original book details if required. |

### Table 2.3.12.2 Edit Book Invalid Book ID Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-12-002 |
| Objective | Edit Book Alternate Flow - Invalid Book ID |
| Test Cases To Be Executed | TC-12-002 |
| Set Up | 1. Log in as an admin user.<br>2. Open the edit page using Book ID = 999. [TC-12-002] |
| Wrap Up | 1. Return to the book management list. |

### Table 2.3.12.3 Edit Book Missing Field Validation Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-12-003 |
| Objective | Edit Book Alternate Flows - Missing Required Fields |
| Test Cases To Be Executed | TC-12-003, TC-12-004, TC-12-009 |
| Set Up | 1. Log in as an admin user and open the edit page for an existing book.<br>2. Input Title = blank and Quantity = 10, then click Update. [TC-12-003]<br>3. Input Title = Updated Book and Quantity = blank, then click Update. [TC-12-004]<br>4. Verify that the correct field-specific validation error message is displayed for the missing Title scenario. [TC-12-009] |
| Wrap Up | 1. Confirm the book record remains unchanged after rejected updates. |

### Table 2.3.12.4 Edit Book Invalid Quantity Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-12-004 |
| Objective | Edit Book Alternate Flows - Invalid Quantity |
| Test Cases To Be Executed | TC-12-005, TC-12-006 |
| Set Up | 1. Log in as an admin user and open the edit page for an existing book.<br>2. Input Quantity = -5, then click Update. [TC-12-005]<br>3. Input Quantity = abc, then click Update. [TC-12-006] |
| Wrap Up | 1. Confirm the book quantity remains unchanged after rejected updates. |

### Table 2.3.12.5 Edit Book Unauthorized Access Test Procedure

| Field | Value |
|---|---|
| Test Procedure ID | TP-12-005 |
| Objective | Edit Book Alternate Flow - Unauthorized Access |
| Test Cases To Be Executed | TC-12-008 |
| Set Up | 1. Log in using a normal user account.<br>2. Attempt to access the edit function or open an edit page for a book. [TC-12-008] |
| Wrap Up | 1. Log out from the normal user account.<br>2. Confirm no book record was changed. |

## 2.3.13 Test Procedure Coverage Summary

Total test procedures designed: 35.
Total test cases covered: 68.
All identified test cases are covered by at least one test procedure.
