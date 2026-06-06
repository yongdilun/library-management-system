@echo off
setlocal
cd /d "%~dp0"

call :load_env

if not defined FLASK_APP set "FLASK_APP=app.py"
if not defined FLASK_ENV set "FLASK_ENV=development"

echo Starting Library Management System on http://127.0.0.1:5000
echo Press Ctrl+C to stop the server.
python -m flask run --host 127.0.0.1 --port 5000
exit /b %ERRORLEVEL%

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
