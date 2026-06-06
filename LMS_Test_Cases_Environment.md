# 2.0 Test Cases

## 2.1 Environment

LMS tests will be run using dummy accounts and dummy book records where tested operations will not affect production users, real library inventory, or real reservation records. Tests shall be performed on the Library Management System with the following specification:

### Table 2.1.1 LMS Test Environment Requirements

| Item | Specification |
|---|---|
| Hardware Name | Local Windows workstation |
| Operating System | Windows environment |
| Web Browser | Google Chrome / Chrome Headless for Selenium and Playwright execution |
| Application Runtime | Python 3.13.5 with Flask development server |
| Database Server | MySQL database named lms |
| Automation Tools | Selenium 4, Playwright browser snapshots, Python Requests/Postman-compatible HTTP checks |

The following dummy LMS accounts and records are needed for testing purposes:

### Table 2.1.2 Required Dummy LMS Accounts and Test Records

| Test Data ID | Type / Role | Purpose | Credential / Test Data |
|---|---|---|---|
| TD-01 | Admin Account | Admin login, add book, edit book, delete book, and manage users testing | Email = hamza@gmail.com<br>Password = password |
| TD-02 | Valid Member Account | Member login, logout, profile, reservation, and reserved-book testing | Email = svv_user@example.test<br>Password = password |
| TD-03 | Duplicate Member Account | Sign Up duplicate-account validation | Email = svv_duplicate@example.test<br>Password = password |
| TD-04 | Profile Test Account | Manage Profile valid and invalid update testing | Email = svv_profile@example.test<br>Password = password |
| TD-05 | No Reservation Account | View Reserved Books empty-list testing | Email = svv_empty@example.test<br>Password = password |
| TD-06 | Reservation Limit Account | Reservation limit exceeded testing | User has 5 existing reservation records |
| TD-07 | Available Book Record | Book list, book details, and successful reservation testing | Book = SVV Test Book Available<br>Count > 0<br>Availability = Available |
| TD-08 | Unavailable Book Record | Unavailable book and reservation failure testing | Book = SVV Test Book Unavailable<br>Count = 0 |
| TD-09 | Search Book Record | Search Book valid-keyword result testing | Book = SVV Test Harry Potter Automation<br>Keyword = Harry Potter |
| TD-10 | Invalid IDs / Failure Data | Invalid book ID, database failure, and negative-flow testing | Book ID = 999999<br>Simulated DB failure through test harness |