@echo off
REM Usage:  run.bat upload "C:\path\02_Plants" --channel happy
REM         run.bat queue --channel happy
REM First run creates .venv and installs requirements.
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  echo Creating Python environment...
  py -3 -m venv .venv || python -m venv .venv
  .venv\Scripts\python.exe -m pip install --upgrade pip
  .venv\Scripts\python.exe -m pip install -r requirements.txt
)
if not exist logs mkdir logs
.venv\Scripts\python.exe yt_upload.py %*
