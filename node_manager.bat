@echo off
setlocal
title ComfyUI Manager - Pro Suite
cd /d "%~dp0"

:: Auto-detect venv
set "V_NAME=venv"
if not exist "venv\Scripts\activate.bat" set "V_NAME=.venv"

if exist "%V_NAME%\Scripts\activate.bat" (
    call "%V_NAME%\Scripts\activate.bat"
    :: Starting Python
    python manager.py
) else (
    echo [!] ERROR: Could not find venv.
    echo Ensure this file is in the root ComfyUI folder.
    pause
)