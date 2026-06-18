# Worktree Run and Test Commands

This project is currently used with two Git worktrees so the baseline and improved versions can run side by side.

| Version | Branch | Folder | URL | Database |
|---|---|---|---|---|
| Improved version | `codex/software-maintainability-assignment` | `C:\Users\dilun\Documents\SVVAssigment\library-management-system` | `http://127.0.0.1:5000` | `lms_improved` |
| Baseline version | `main` | `C:\Users\dilun\Documents\SVVAssigment\library-management-system-main` | `http://127.0.0.1:5001` | `lms_main` |

## Start The Improved Server

Open PowerShell:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system
.\start_server.bat
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Start The Baseline Main Server

Open another PowerShell terminal:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system-main
$env:FLASK_APP='app.py'
python -m flask run --host 127.0.0.1 --port 5001
```

Open in browser:

```text
http://127.0.0.1:5001
```

## Run Tests On The Improved Version

Make sure the improved server is running on port `5000`, then open another PowerShell terminal:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system
$env:LMS_BASE_URL='http://127.0.0.1:5000'

python tests\lms_test_system_runner.py
python tests\run_lms_non_functional_tests.py
python tests\run_maintenance_validation.py
```

Alternative batch commands:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system

.\run_full_pipeline_tests.bat
.\run_nfr_tests.bat
.\run_maintenance_validation_tests.bat
```

Expected improved results:

| Test Set | Expected Result |
|---|---:|
| Full functional pipeline | `68/68 pass` |
| Non-functional validation | `4/4 pass` |
| Maintainability validation | `14/14 pass` |

## Run Tests On The Baseline Main Version

Make sure the baseline `main` server is running on port `5001`, then open another PowerShell terminal:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system-main
$env:LMS_BASE_URL='http://127.0.0.1:5001'

python tests\lms_test_system_runner.py
python tests\run_lms_non_functional_tests.py
```

The `main` branch does not include `tests\run_maintenance_validation.py`. That test exists only in the improved branch because it verifies the maintenance enhancements.

The baseline is expected to have failures. Use the generated JSON files to record the exact result:

```powershell
@'
import json
from pathlib import Path

functional = json.loads(Path("LMS_Test_Log_Results.json").read_text())["summary"]
nfr = json.loads(Path("LMS_Non_Functional_Test_Results.json").read_text())["summary"]

total = functional["total"] + nfr["total"]
passed = functional["pass"] + nfr["pass"]
failed = functional["fail"] + nfr["fail"]
not_executed = functional["not_executed"] + nfr["not_executed"]

print(f"Functional: {functional['pass']}/{functional['total']} passed, {functional['fail']} failed")
print(f"Non-functional: {nfr['pass']}/{nfr['total']} passed, {nfr['fail']} failed")
print(f"Combined: Total {total}; Pass {passed}; Fail {failed}; Not Executed {not_executed}")
'@ | python -
```

## Reset Separate Databases

Use this only when you want a clean comparison. PowerShell does not support MySQL `<` input redirection directly, so use `Get-Content`.

Create or reset the databases:

```powershell
mysql -u root -p -e "DROP DATABASE IF EXISTS lms_main; CREATE DATABASE lms_main;"
mysql -u root -p -e "DROP DATABASE IF EXISTS lms_improved; CREATE DATABASE lms_improved;"
```

Import baseline SQL:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system-main
Get-Content db\lms.sql | mysql -u root -p lms_main
```

Import improved SQL:

```powershell
cd C:\Users\dilun\Documents\SVVAssigment\library-management-system
Get-Content db\lms.sql | mysql -u root -p lms_improved
```

Confirm each `.env` file points to the correct database:

```text
library-management-system\.env       MYSQL_DATABASE_DB=lms_improved
library-management-system-main\.env  MYSQL_DATABASE_DB=lms_main
```

## Stop Servers

If the server is running in an open terminal, press `Ctrl + C`.

To stop by port:

```powershell
$server = Get-NetTCPConnection -LocalPort 5000 -State Listen -ErrorAction SilentlyContinue
if ($server) { Stop-Process -Id $server.OwningProcess -Force }

$server = Get-NetTCPConnection -LocalPort 5001 -State Listen -ErrorAction SilentlyContinue
if ($server) { Stop-Process -Id $server.OwningProcess -Force }
```

