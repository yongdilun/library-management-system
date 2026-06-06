@echo off
setlocal
cd /d "%~dp0"

call :load_env
if not exist "reports\maintenance_evidence" mkdir "reports\maintenance_evidence"

set "STARTED_SERVER=0"
call :server_alive
if errorlevel 1 (
  echo Server is not running. Starting temporary test server...
  start "LMS Temporary Test Server" /min cmd /c "start_server.bat"
  set "STARTED_SERVER=1"
  call :wait_for_server
  if errorlevel 1 (
    echo Server did not become reachable on http://127.0.0.1:5000.
    pause
    exit /b 1
  )
)

echo Running focused maintenance validation tests...
echo Output will be saved to reports\maintenance_evidence\test_execution_maintenance_validation.txt
powershell -NoProfile -ExecutionPolicy Bypass -Command "& python 'tests\run_maintenance_validation.py' 2>&1 | Tee-Object -FilePath 'reports\maintenance_evidence\test_execution_maintenance_validation.txt'; exit $LASTEXITCODE"
set "EXIT_CODE=%ERRORLEVEL%"

if "%STARTED_SERVER%"=="1" (
  echo Stopping temporary test server...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-CimInstance Win32_Process | Where-Object { ($_.Name -like 'python*.exe') -and ($_.CommandLine -like '*flask*run*') -and ($_.CommandLine -like '*5000*') } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
)

echo.
if "%EXIT_CODE%"=="0" (
  echo Focused maintenance validation completed successfully.
) else (
  echo Focused maintenance validation failed with exit code %EXIT_CODE%.
)
pause
exit /b %EXIT_CODE%

:server_alive
powershell -NoProfile -ExecutionPolicy Bypass -Command "try { Invoke-WebRequest 'http://127.0.0.1:5000/' -UseBasicParsing -TimeoutSec 3 | Out-Null; exit 0 } catch { exit 1 }"
exit /b %ERRORLEVEL%

:wait_for_server
for /l %%I in (1,1,15) do (
  call :server_alive
  if not errorlevel 1 exit /b 0
  timeout /t 1 /nobreak >nul
)
exit /b 1

:load_env
if exist ".env" (
  for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    call :set_env "%%A" "%%B"
  )
)
exit /b 0

:set_env
set "env_key=%~1"
set "env_val=%~2"
if "%env_key%"=="" exit /b 0
if "%env_key:~0,1%"=="#" exit /b 0
set "%env_key%=%env_val%"
exit /b 0
