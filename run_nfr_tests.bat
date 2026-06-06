@echo off
setlocal
cd /d "%~dp0"

call :load_env
if not exist "reports\maintenance_evidence" mkdir "reports\maintenance_evidence"

echo Running non-functional requirement validation tests...
echo Output will be saved to reports\maintenance_evidence\test_execution_nfr_validation.txt
powershell -NoProfile -ExecutionPolicy Bypass -Command "& python 'tests\run_lms_non_functional_tests.py' 2>&1 | Tee-Object -FilePath 'reports\maintenance_evidence\test_execution_nfr_validation.txt'; exit $LASTEXITCODE"
set "EXIT_CODE=%ERRORLEVEL%"

echo.
if "%EXIT_CODE%"=="0" (
  echo Non-functional validation completed successfully.
) else (
  echo Non-functional validation failed with exit code %EXIT_CODE%.
)
pause
exit /b %EXIT_CODE%

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
