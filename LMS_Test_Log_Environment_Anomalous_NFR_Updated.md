# Updated Test Log Sections

## Environment Information

| Requested Test Environment | Test Environment After Changes |
|---|---|
| Hardware: Local Windows workstation<br>Software: Python 3.13.5, Selenium 4, Chrome headless, Playwright browser snapshots, Python Requests/Postman-compatible HTTP automation, Python chart/report generation<br>Application URL: http://127.0.0.1:5000<br>Database: MySQL lms database<br>Reference: LMS_TPS_1.0.0, LMS_TL_1.0.0, LMS_TSR_1.0.0<br>Included NFR Scope: REQ_Q001, REQ_Q002, REQ_Q003, REQ_Q004 | No application logic was changed. Temporary functional and non-functional test records were created and cleaned up by the test runner. Controlled database-failure simulations were performed in the test harness only. NFR checks were added for concurrent reservation accuracy, foreign key integrity, password hashing/salting, and HTTPS/TLS protection. |

## Anomalous Event

| Unexpected event occurred | Test Procedure ID | Anomaly Reporter Name |
|---|---|---|
| Registered email with wrong password was accepted if this row fails. | TP-02-002 | Yong Di Lun |
| Empty name was submitted through the profile update form. | TP-04-002 | Yong Di Lun |
| Empty email was submitted through the profile update form. | TP-04-002 | Yong Di Lun |
| Book list displayed title, author, and availability/count. | TP-05-001 | Yong Di Lun |
| Simulated BookManager.list database failure returned HTTP 500. | TP-05-002 | Yong Di Lun |
| Simulated BookManager.getBook database failure returned HTTP 500. | TP-06-003 | Yong Di Lun |
| Empty search input was submitted from the home search form. | TP-07-002 | Yong Di Lun |
| A 60-character keyword was submitted. | TP-07-003 | Yong Di Lun |
| Empty search validation message was checked. | TP-07-002 | Yong Di Lun |
| A user with five reservations attempted another reservation. | TP-08-003 | Yong Di Lun |
| Duplicate reservation route was invoked directly with an authenticated user session. | TP-08-002 | Yong Di Lun |
| Reservation limit message was checked after exceeding the limit. | TP-08-003 | Yong Di Lun |
| Admin Add Book route was submitted with valid data. | TP-10-001 | Yong Di Lun |
| Database insertion was checked after valid Add Book submission. | TP-10-001 | Yong Di Lun |
| Description field was inspected for required validation. | TP-10-002 | Yong Di Lun |
| Quantity field was inspected for a minimum value rule. | TP-10-003 | Yong Di Lun |
| Duplicate book handling was checked against the real Add Book route/page. | TP-10-003 | Yong Di Lun |
| Field-specific error message was checked for missing Description. | TP-10-002 | Yong Di Lun |
| Simulated BookManager.delete failure returned HTTP 500; target book still exists = True. | TP-11-003 | Yong Di Lun |
| Delete non-existing book returned HTTP 302. | TP-11-003 | Yong Di Lun |
| Admin delete link was inspected for an explicit confirmation step. | TP-11-001 | Yong Di Lun |
| Cancel deletion flow was checked; no confirmation dialog is implemented. | TP-11-002 | Yong Di Lun |
| Deletion failure message check used simulated delete failure response HTTP 500. | TP-11-003 | Yong Di Lun |
| Admin edit route was submitted with valid values. | TP-12-001 | Yong Di Lun |
| Database was checked after valid edit submission. | TP-12-001 | Yong Di Lun |
| Invalid edit Book ID returned HTTP 200. | TP-12-002 | Yong Di Lun |
| Quantity field was inspected for a positive/minimum value rule. | TP-12-004 | Yong Di Lun |
| Description-only edit was submitted through the edit route. | TP-12-001 | Yong Di Lun |
| Database metadata and orphan reservation insertion were checked against the live lms database. Actual result: Foreign keys found = (); orphan reservation insert succeeded = True. | TP-Q-002 | Yong Di Lun |
| Password storage was inspected in the live users table for secure salted hashing behavior. Actual result: Stored hashes = ['025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8']; plaintext absent = True; bcrypt-like = False; unique hashes = False. | TP-Q-003 | Yong Di Lun |
| Login route was accessed over HTTP and HTTPS to verify TLS availability. Actual result: HTTP login URL = http://127.0.0.1:5000/signin; HTTPS endpoint available = False; HTTPS error = SSLError: HTTPSConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded with url: /signin (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1028)'))). | TP-Q-004 | Yong Di Lun |