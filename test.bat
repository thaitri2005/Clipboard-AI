@echo off
echo ============================================
echo  Testing Local AI Clipboard Setup
echo ============================================
echo.

echo [1/4] Testing Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)
echo OK: Python found
echo.

echo [2/4] Testing Ollama...
ollama --version
if %errorlevel% neq 0 (
    echo ERROR: Ollama not found!
    echo Please close and reopen PowerShell, or install Ollama
    pause
    exit /b 1
)
echo OK: Ollama found
echo.

echo [3/4] Checking if model exists...
ollama list | findstr "phi3:mini"
if %errorlevel% neq 0 (
    echo WARNING: phi3:mini model not found
    echo Please run: ollama pull phi3:mini
    pause
    exit /b 1
)
echo OK: Model found
echo.

echo [4/4] Testing Python packages...
python -c "import pyperclip; import pynput; print('OK: All packages installed')"
if %errorlevel% neq 0 (
    echo ERROR: Python packages missing
    echo Installing now...
    pip install -r requirements.txt
)
echo.

echo ============================================
echo  All checks passed!
echo ============================================
echo.
echo Ready to run! Press any key to start the app...
pause > nul

python clipboard_ai.py
