# Test Summary Report

Version Author: Yong Di Lun
Associated test plan reference: LMS_TP_1.0.0
Scope: Functional requirements F001 to F0012 and non-functional requirements REQ_Q001 to REQ_Q004

## Summary

- Planned test cases: 72
- Remaining test cases: 0
- Completed test cases: 72
- Passed: 41
- Failed: 31
- Not executed: 0
- Fatal defects: 12
- Major defects: 14
- Minor defects: 5

## Non-Functional Requirement Results

| Requirement ID | Category | Requirement Summary | Test Result |
|---|---|---|---|
| REQ_Q001 | Reliability & Accuracy | 100% transactional accuracy for concurrent book reservations to prevent double-booking. | Pass |
| REQ_Q002 | Reliability & Accuracy | Database foreign key constraints between User, Book, and Reservation records prevent orphaned records. | Fail |
| REQ_Q003 | Security | Passwords are securely hashed and salted before database storage; plain text passwords are never saved. | Fail |
| REQ_Q004 | Security | Client-to-server interactions use HTTPS/TLS 1.2 or higher. | Fail |

## Incidents

| Incident ID | Test Case ID | Severity | Status | Description |
|---|---|---|---|---|
| LMS_TIR_1.0/TIR-001 | TC-02-002 | Fatal | Open | Registered email with wrong password was accepted if this row fails. |
| LMS_TIR_1.0/TIR-002 | TC-04-003 | Major | Open | Empty name was submitted through the profile update form. |
| LMS_TIR_1.0/TIR-003 | TC-04-004 | Major | Open | Empty email was submitted through the profile update form. |
| LMS_TIR_1.0/TIR-004 | TC-05-003 | Minor | Open | Book list displayed title, author, and availability/count. |
| LMS_TIR_1.0/TIR-005 | TC-05-004 | Fatal | Open | Simulated BookManager.list database failure returned HTTP 500. |
| LMS_TIR_1.0/TIR-006 | TC-06-005 | Fatal | Open | Simulated BookManager.getBook database failure returned HTTP 500. |
| LMS_TIR_1.0/TIR-007 | TC-07-002 | Major | Open | Empty search input was submitted from the home search form. |
| LMS_TIR_1.0/TIR-008 | TC-07-003 | Major | Open | A 60-character keyword was submitted. |
| LMS_TIR_1.0/TIR-009 | TC-07-006 | Major | Open | Empty search validation message was checked. |
| LMS_TIR_1.0/TIR-010 | TC-08-003 | Major | Open | A user with five reservations attempted another reservation. |
| LMS_TIR_1.0/TIR-011 | TC-08-004 | Major | Open | Duplicate reservation route was invoked directly with an authenticated user session. |
| LMS_TIR_1.0/TIR-012 | TC-08-005 | Major | Open | Reservation limit message was checked after exceeding the limit. |
| LMS_TIR_1.0/TIR-013 | TC-10-001 | Fatal | Open | Admin Add Book route was submitted with valid data. |
| LMS_TIR_1.0/TIR-014 | TC-10-009 | Fatal | Open | Database insertion was checked after valid Add Book submission. |
| LMS_TIR_1.0/TIR-015 | TC-10-003 | Minor | Open | Description field was inspected for required validation. |
| LMS_TIR_1.0/TIR-016 | TC-10-004 | Major | Open | Quantity field was inspected for a minimum value rule. |
| LMS_TIR_1.0/TIR-017 | TC-10-006 | Major | Open | Duplicate book handling was checked against the real Add Book route/page. |
| LMS_TIR_1.0/TIR-018 | TC-10-008 | Minor | Open | Field-specific error message was checked for missing Description. |
| LMS_TIR_1.0/TIR-019 | TC-11-002 | Fatal | Open | Simulated BookManager.delete failure returned HTTP 500; target book still exists = True. |
| LMS_TIR_1.0/TIR-020 | TC-11-003 | Major | Open | Delete non-existing book returned HTTP 302. |
| LMS_TIR_1.0/TIR-021 | TC-11-005 | Minor | Open | Admin delete link was inspected for an explicit confirmation step. |
| LMS_TIR_1.0/TIR-022 | TC-11-006 | Minor | Open | Cancel deletion flow was checked; no confirmation dialog is implemented. |
| LMS_TIR_1.0/TIR-023 | TC-11-008 | Fatal | Open | Deletion failure message check used simulated delete failure response HTTP 500. |
| LMS_TIR_1.0/TIR-024 | TC-12-001 | Fatal | Open | Admin edit route was submitted with valid values. |
| LMS_TIR_1.0/TIR-025 | TC-12-010 | Fatal | Open | Database was checked after valid edit submission. |
| LMS_TIR_1.0/TIR-026 | TC-12-002 | Major | Open | Invalid edit Book ID returned HTTP 200. |
| LMS_TIR_1.0/TIR-027 | TC-12-005 | Major | Open | Quantity field was inspected for a positive/minimum value rule. |
| LMS_TIR_1.0/TIR-028 | TC-12-007 | Fatal | Open | Description-only edit was submitted through the edit route. |
| LMS_TIR_1.0/TIR-029 | TC-Q002 | Major | Open | Database metadata and orphan reservation insertion were checked against the live lms database. |
| LMS_TIR_1.0/TIR-030 | TC-Q003 | Fatal | Open | Password storage was inspected in the live users table for secure salted hashing behavior. |
| LMS_TIR_1.0/TIR-031 | TC-Q004 | Fatal | Open | Login route was accessed over HTTP and HTTPS to verify TLS availability. |

## Charts

![Schedule](C:\Users\dilun\Documents\SVVAssigment\library-management-system\reports\summary_charts\schedule_completion.png)
![Coverage](C:\Users\dilun\Documents\SVVAssigment\library-management-system\reports\summary_charts\test_case_coverage.png)
![Function Status](C:\Users\dilun\Documents\SVVAssigment\library-management-system\reports\summary_charts\function_status.png)
![Defect Severity](C:\Users\dilun\Documents\SVVAssigment\library-management-system\reports\summary_charts\defect_severity.png)