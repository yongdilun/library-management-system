# Test Log

Tester: Yong Di Lun
Execution: 2026-06-04T11:20:02 to 2026-06-04T11:20:43
Summary: Total 68, Pass 40, Fail 24, Not Executed 4

## Procedure Result

| Requirement ID | Test Design ID | Test Case ID | Test Procedure ID | Type of Testing | Tool | Pass/Fail | Incident ID | Remark |
|---|---|---|---|---|---|---|---|---|
| REQ-F001 | TDS-2.3.1 | TC-01-001 | TP-01-001 | Functional Testing | Selenium | Pass | - | Registered test account through the real Sign Up form. |
| REQ-F001 | TDS-2.3.1 | TC-01-002 | TP-01-001 | Functional Testing | Selenium | Pass | - | Blank email submitted through the Sign Up form. |
| REQ-F001 | TDS-2.3.1 | TC-01-003 | TP-01-001 | Functional Testing | Selenium | Pass | - | Invalid email was rejected by browser email-field validation. |
| REQ-F001 | TDS-2.3.1 | TC-01-004 | TP-01-002 | Functional Testing | Selenium | Pass | - | Duplicate seeded account was submitted through Sign Up. |
| REQ-F002 | TDS-2.3.2 | TC-02-001 | TP-02-001 | Functional Testing | Selenium | Pass | - | Valid user credentials opened a logged-in session. |
| REQ-F002 | TDS-2.3.2 | TC-02-002 | TP-02-002 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-001 | Registered email with wrong password was accepted if this row fails. |
| REQ-F002 | TDS-2.3.2 | TC-02-003 | TP-02-002 | Functional Testing | Selenium | Pass | - | Unregistered email was submitted with a password. |
| REQ-F002 | TDS-2.3.2 | TC-02-004 | TP-02-002 | Functional Testing | Selenium | Pass | - | Unregistered email was submitted with an incorrect password. |
| REQ-F003 | TDS-2.3.3 | TC-03-001 | TP-03-001 | Functional Testing | Selenium | Pass | - | Logout route ended the active user session. |
| REQ-F003 | TDS-2.3.3 | TC-03-002 | TP-03-002 | Functional Testing | Selenium | Pass | - | Browser Back after logout was followed by refresh to verify session protection. |
| REQ-F003 | TDS-2.3.3 | TC-03-003 | TP-03-002 | Functional Testing | Selenium | Pass | - | Protected user profile URL was opened directly after logout. |
| REQ-F004 | TDS-2.3.4 | TC-04-001 | TP-04-001 | Functional Testing | Selenium | Pass | - | Profile was updated through the real profile form. |
| REQ-F004 | TDS-2.3.4 | TC-04-002 | TP-04-002 | Functional Testing | Selenium | Pass | - | Invalid email was rejected by browser email-field validation. |
| REQ-F004 | TDS-2.3.4 | TC-04-003 | TP-04-002 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-002 | Empty name was submitted through the profile update form. |
| REQ-F004 | TDS-2.3.4 | TC-04-004 | TP-04-002 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-003 | Empty email was submitted through the profile update form. |
| REQ-F004 | TDS-2.3.4 | TC-04-005 | TP-04-003 | Functional Testing | Selenium | Pass | - | Profile page was opened without a user session. |
| REQ-F005 | TDS-2.3.5 | TC-05-001 | TP-05-001 | Functional Testing | Selenium | Pass | - | Book list page displayed seeded available books. |
| REQ-F005 | TDS-2.3.5 | TC-05-002 | TP-05-002 | Functional Testing | Selenium | Pass | - | All books were temporarily hidden to verify empty-list behavior. |
| REQ-F005 | TDS-2.3.5 | TC-05-003 | TP-05-001 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-004 | Book list displayed title, author, and availability/count. |
| REQ-F005 | TDS-2.3.5 | TC-05-004 | TP-05-002 | Functional Testing | Not executed | Not Executed | - | Database retrieval failure was not simulated to avoid changing/stopping the real database service. |
| REQ-F006 | TDS-2.3.6 | TC-06-001 | TP-06-001 | Functional Testing | Selenium | Pass | - | Existing book details page was opened. |
| REQ-F006 | TDS-2.3.6 | TC-06-002 | TP-06-003 | Functional Testing | Postman/HTTP | Pass | - | GET /books/999999 returned HTTP 200. |
| REQ-F006 | TDS-2.3.6 | TC-06-003 | TP-06-001 | Functional Testing | Selenium | Pass | - | Available book details page displayed a reserve/add option. |
| REQ-F006 | TDS-2.3.6 | TC-06-004 | TP-06-002 | Functional Testing | Selenium | Pass | - | Unavailable book details page displayed zero-count status. |
| REQ-F006 | TDS-2.3.6 | TC-06-005 | TP-06-003 | Functional Testing | Not executed | Not Executed | - | Database retrieval failure was not simulated to avoid changing/stopping the real database service. |
| REQ-F007 | TDS-2.3.7 | TC-07-001 | TP-07-001 | Functional Testing | Selenium | Pass | - | Search was executed with a valid keyword. |
| REQ-F007 | TDS-2.3.7 | TC-07-002 | TP-07-002 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-005 | Empty search input was submitted from the home search form. |
| REQ-F007 | TDS-2.3.7 | TC-07-003 | TP-07-003 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-006 | A 60-character keyword was submitted. |
| REQ-F007 | TDS-2.3.7 | TC-07-004 | TP-07-003 | Functional Testing | Selenium | Pass | - | Special-character search returned a safe no-results page. |
| REQ-F007 | TDS-2.3.7 | TC-07-005 | TP-07-001 | Functional Testing | Selenium | Pass | - | Search results contained the seeded matching book. |
| REQ-F007 | TDS-2.3.7 | TC-07-006 | TP-07-002 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-007 | Empty search validation message was checked. |
| REQ-F008 | TDS-2.3.8 | TC-08-001 | TP-08-001 | Functional Testing | Selenium | Pass | - | Available book was reserved through the UI. |
| REQ-F008 | TDS-2.3.8 | TC-08-002 | TP-08-002 | Functional Testing | Selenium | Pass | - | Unavailable book reservation was attempted through the UI. |
| REQ-F008 | TDS-2.3.8 | TC-08-003 | TP-08-003 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-008 | A user with five reservations attempted another reservation. |
| REQ-F008 | TDS-2.3.8 | TC-08-004 | TP-08-002 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-009 | Duplicate reservation route was invoked directly with an authenticated user session. |
| REQ-F008 | TDS-2.3.8 | TC-08-005 | TP-08-003 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-010 | Reservation limit message was checked after exceeding the limit. |
| REQ-F009 | TDS-2.3.9 | TC-09-001 | TP-09-001 | Functional Testing | Selenium | Pass | - | Profile page displayed reserved books for the logged-in user. |
| REQ-F009 | TDS-2.3.9 | TC-09-004 | TP-09-001 | Functional Testing | Selenium | Pass | - | Reservation list was checked for the current user's records only. |
| REQ-F009 | TDS-2.3.9 | TC-09-002 | TP-09-002 | Functional Testing | Selenium | Pass | - | User with no reservations opened the profile page. |
| REQ-F009 | TDS-2.3.9 | TC-09-005 | TP-09-002 | Functional Testing | Selenium | Pass | - | Empty reservation message was checked. |
| REQ-F009 | TDS-2.3.9 | TC-09-003 | TP-09-003 | Functional Testing | Selenium | Pass | - | Reserved-book/profile page was opened without a session. |
| REQ-F0010 | TDS-2.3.10 | TC-10-001 | TP-10-001 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-011 | Admin Add Book route was submitted with valid data. |
| REQ-F0010 | TDS-2.3.10 | TC-10-009 | TP-10-001 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-012 | Database insertion was checked after valid Add Book submission. |
| REQ-F0010 | TDS-2.3.10 | TC-10-002 | TP-10-002 | Functional Testing | Postman/HTTP | Pass | - | Add Book HTML marks title as a required field. |
| REQ-F0010 | TDS-2.3.10 | TC-10-003 | TP-10-002 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-013 | Description field was inspected for required validation. |
| REQ-F0010 | TDS-2.3.10 | TC-10-004 | TP-10-003 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-014 | Quantity field was inspected for a minimum value rule. |
| REQ-F0010 | TDS-2.3.10 | TC-10-005 | TP-10-003 | Functional Testing | Postman/HTTP | Pass | - | Quantity field uses a browser number input for non-numeric validation. |
| REQ-F0010 | TDS-2.3.10 | TC-10-006 | TP-10-003 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-015 | Duplicate book handling was checked against the real Add Book route/page. |
| REQ-F0010 | TDS-2.3.10 | TC-10-007 | TP-10-002 | Functional Testing | Postman/HTTP | Pass | - | All-empty submission is blocked partly by required fields in the HTML form. |
| REQ-F0010 | TDS-2.3.10 | TC-10-008 | TP-10-002 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-016 | Field-specific error message was checked for missing Description. |
| REQ-F0011 | TDS-2.3.11 | TC-11-001 | TP-11-001 | Functional Testing | Postman/HTTP | Pass | - | Existing book was deleted through the real admin delete route. |
| REQ-F0011 | TDS-2.3.11 | TC-11-007 | TP-11-001 | Functional Testing | Postman/HTTP | Pass | - | Inventory database was checked after deletion. |
| REQ-F0011 | TDS-2.3.11 | TC-11-002 | TP-11-003 | Functional Testing | Not executed | Not Executed | - | Database/system deletion failure was not simulated to avoid changing/stopping the real database service. |
| REQ-F0011 | TDS-2.3.11 | TC-11-003 | TP-11-003 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-017 | Delete non-existing book returned HTTP 302. |
| REQ-F0011 | TDS-2.3.11 | TC-11-004 | TP-11-004 | Functional Testing | Postman/HTTP | Pass | - | Normal user attempted the admin delete route. |
| REQ-F0011 | TDS-2.3.11 | TC-11-005 | TP-11-001 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-018 | Admin delete link was inspected for an explicit confirmation step. |
| REQ-F0011 | TDS-2.3.11 | TC-11-006 | TP-11-002 | Functional Testing | Selenium | Fail | LMS_TIR_1.0/TIR-019 | Cancel deletion flow was checked; no confirmation dialog is implemented. |
| REQ-F0011 | TDS-2.3.11 | TC-11-008 | TP-11-003 | Functional Testing | Not executed | Not Executed | - | Deletion failure message was not executed because no safe DB failure simulation was available. |
| REQ-F0012 | TDS-2.3.12 | TC-12-001 | TP-12-001 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-020 | Admin edit route was submitted with valid values. |
| REQ-F0012 | TDS-2.3.12 | TC-12-010 | TP-12-001 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-021 | Database was checked after valid edit submission. |
| REQ-F0012 | TDS-2.3.12 | TC-12-002 | TP-12-002 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-022 | Invalid edit Book ID returned HTTP 200. |
| REQ-F0012 | TDS-2.3.12 | TC-12-003 | TP-12-003 | Functional Testing | Postman/HTTP | Pass | - | Edit Book HTML marks title as a required field. |
| REQ-F0012 | TDS-2.3.12 | TC-12-009 | TP-12-003 | Functional Testing | Postman/HTTP | Pass | - | Validation feedback for missing title is provided by browser required-field validation. |
| REQ-F0012 | TDS-2.3.12 | TC-12-004 | TP-12-003 | Functional Testing | Postman/HTTP | Pass | - | Edit Book HTML marks quantity as a required field. |
| REQ-F0012 | TDS-2.3.12 | TC-12-005 | TP-12-004 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-023 | Quantity field was inspected for a positive/minimum value rule. |
| REQ-F0012 | TDS-2.3.12 | TC-12-006 | TP-12-004 | Functional Testing | Postman/HTTP | Pass | - | Quantity field uses a browser number input for non-numeric validation. |
| REQ-F0012 | TDS-2.3.12 | TC-12-007 | TP-12-001 | Functional Testing | Postman/HTTP | Fail | LMS_TIR_1.0/TIR-024 | Description-only edit was submitted through the edit route. |
| REQ-F0012 | TDS-2.3.12 | TC-12-008 | TP-12-005 | Functional Testing | Postman/HTTP | Pass | - | Normal user attempted the admin edit route. |