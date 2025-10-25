@echo off
echo ========================================
echo  Local AI Clipboard - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if Ollama is installed
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: Ollama is not installed or not in PATH
    echo Please install Ollama from https://ollama.ai/download
    echo.
    pause
)

REM Check if requirements are installed
echo Checking dependencies...
pip show pyperclip >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Python dependencies...
    pip install -r requirements.txt
)

echo.
echo ========================================
echo  Starting Local AI Clipboard...
echo ========================================
echo.
echo Press Ctrl+Shift+G to process clipboard
echo Press Ctrl+Shift+Q to exit
echo.
echo NOTE: First request might be slow (10-30s)
echo       as Ollama loads the model into memory.
echo       Subsequent requests will be faster!
echo.

python clipboard_ai.py

pause
