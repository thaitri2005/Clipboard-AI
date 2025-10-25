@echo off
echo ============================================
echo  Warming up Ollama...
echo ============================================
echo.

echo This will start the Ollama model so the first
echo request in the app will be faster.
echo.

echo Loading phi3:mini model...
echo Please wait, this might take 10-30 seconds...
echo.

echo Hello, test | ollama run phi3:mini > nul 2>&1

if %errorlevel% equ 0 (
    echo ✅ Ollama is ready!
    echo ✅ Model loaded into memory
    echo.
    echo You can now use the app without delays.
) else (
    echo ⚠️  Warning: Ollama might not be ready
    echo Please make sure:
    echo   1. Ollama is installed
    echo   2. Model is pulled: ollama pull phi3:mini
    echo   3. Ollama service is running
    echo.
)

echo.
echo Press any key to continue...
pause > nul
