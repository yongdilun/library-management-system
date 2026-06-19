# Test Documentation

This document explains the test strategy, tools, commands, and results used to validate the Library Management System maintenance work.

## 1. Test Objective

The objective of testing is to compare the baseline LMS against the improved LMS and verify that the implemented maintenance enhancements improve security, validation, admin workflows, reservation reliability, UI behavior, and documentation quality.

## 2. Test Scope

Testing covers:

- User sign up, login, logout, and profile update.
- Book browsing, details, search, and reservation.
- Admin add, edit, and delete book workflows.
- Database integrity and reservation correctness.
- Password hashing and security configuration.
- UI evidence through before/after screenshots.

## 3. Test Tools

| Tool | Usage |
|---|---|
| Selenium | Browser-based functional workflow testing. |
| Python Requests | Route-level and Postman-style HTTP validation. |
| PyMySQL | Database validation and data integrity checks. |
| Playwright | Browser screenshot evidence for before/after comparison. |
| Batch files | Simple Windows commands for starting servers and running test suites. |

The test suite is not Selenium-only. Selenium is used for browser workflows, while Requests and PyMySQL validate backend and database behavior.

## 4. Test Environment

| Version | Branch | URL | Database |
|---|---|---|---|
| Baseline | `main` | `http://127.0.0.1:5001` | `lms_main` |
| Improved | `software-maintainability-assignment` | `http://127.0.0.1:5000` | `lms_improved` |

## 5. Test Commands

### 5.1 Start Improved Server

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system
.\start_server.bat
```

Manual command:

```powershell
python -m flask run --host 127.0.0.1 --port 5000
```

### 5.2 Run Improved Functional Tests

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system
$env:LMS_BASE_URL='http://127.0.0.1:5000'
python tests\lms_test_system_runner.py
```

### 5.3 Run Improved Non-Functional Tests

```powershell
python tests\run_lms_non_functional_tests.py
```

### 5.4 Run Maintainability Validation Tests

```powershell
python tests\run_maintenance_validation.py
```

### 5.5 Batch File Shortcuts

```powershell
.\run_full_pipeline_tests.bat
.\run_nfr_tests.bat
.\run_maintenance_validation_tests.bat
```

## 6. Test Results Summary

Latest validated improved branch results:

| Test Suite | Result |
|---|---:|
| Functional pipeline | `68/68 passed` |
| Non-functional requirements | `4/4 passed` |
| Maintainability validation | `14/14 passed` |

Baseline branch comparison result:

| Test Suite | Result |
|---|---:|
| Functional pipeline | `40/68 passed`, `28 failed` |
| Non-functional requirements | `0/4 passed`, `4 failed` |

The baseline failures were used to justify and verify the maintenance improvements.

## 7. Important Test Cases for Presentation

| Presenter | Test Case | Focus |
|---|---|---|
| Wayman | TC-02-002 | Wrong password login validation. |
| Wayman | TC-04-003 | Empty profile name validation. |
| Wayman | TC-07-002 | Empty search keyword validation. |
| Seow Jiun Wen | TC-10-001 | Valid admin Add Book. |
| Seow Jiun Wen | TC-10-003 | Missing description validation. |
| Seow Jiun Wen | TC-12-001 | Valid admin Edit Book. |

Screenshot evidence for these cases is stored under:

```text
reports/presentation_day_evidence
```

## 8. Result Files

The test runners generate JSON evidence files:

```text
LMS_Test_Log_Results.json
LMS_Non_Functional_Test_Results.json
reports/maintenance_evidence/maintenance_validation_results.json
```

These generated files are ignored by Git because they are local test artifacts.

## 9. Test Data Notes

Seed users:

| Role | Email | Password |
|---|---|---|
| User/Admin seed account | `hamza@gmail.com` | `password` |
| User seed account | `naveed@gmail.com` | `password` |

Temporary presentation users and books with the `DAYDEMO` prefix are created only for screenshot evidence and are not part of the original seed SQL.

## 10. Interpretation

The improved branch passes the full functional pipeline, non-functional tests, and maintainability validation tests. This indicates that the enhancement work fixed the selected issues without breaking the existing tested workflows.
