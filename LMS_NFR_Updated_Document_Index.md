# LMS NFR Updated Documents

Total test cases: 72
Passed: 41
Failed: 31
Non-functional requirements added: REQ_Q001, REQ_Q002, REQ_Q003, REQ_Q004

| Test Case | Requirement | Result | Incident | Actual |
|---|---|---|---|---|
| TC-Q001 | REQ_Q001 | Pass | - | HTTP statuses = [200, 200]; reservations created = 1; book count after test = 0. |
| TC-Q002 | REQ_Q002 | Fail | LMS_TIR_1.0/TIR-029 | Foreign keys found = (); orphan reservation insert succeeded = True. |
| TC-Q003 | REQ_Q003 | Fail | LMS_TIR_1.0/TIR-030 | Stored hashes = ['025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8', '025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8']; plaintext absent = True; bcrypt-like = False; unique hashes = False. |
| TC-Q004 | REQ_Q004 | Fail | LMS_TIR_1.0/TIR-031 | HTTP login URL = http://127.0.0.1:5000/signin; HTTPS endpoint available = False; HTTPS error = SSLError: HTTPSConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded with url: /signin (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1028)'))). |