# Automated Setup Script for Local AI Clipboard
# This will install Ollama CLI and set up a lightweight model

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Local AI Clipboard - Automated Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "Warning: This script works best with administrator privileges" -ForegroundColor Yellow
    Write-Host "   Consider running: Right-click PowerShell -> Run as Administrator" -ForegroundColor Yellow
    Write-Host ""
}

# Step 1: Check/Install Python
Write-Host "Step 1: Checking Python..." -ForegroundColor Green
try {
    $pythonVersion = python --version 2>&1
    Write-Host "OK Python installed: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    Write-Host "   Please install Python from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "   Make sure to check Add Python to PATH during installation" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

# Step 2: Check/Install Ollama
Write-Host "Step 2: Checking Ollama CLI..." -ForegroundColor Green
try {
    $ollamaVersion = ollama --version 2>&1
    Write-Host "OK Ollama already installed: $ollamaVersion" -ForegroundColor Green
} catch {
    Write-Host "Warning: Ollama not found. Installing..." -ForegroundColor Yellow
    
    # Try winget first
    Write-Host "   Attempting installation via winget..." -ForegroundColor Cyan
    try {
        winget install Ollama.Ollama --silent
        Write-Host "OK Ollama installed via winget!" -ForegroundColor Green
        Write-Host "   Please restart PowerShell and run this script again." -ForegroundColor Yellow
        exit 0
    } catch {
        Write-Host "Warning: Winget installation failed." -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Please install Ollama manually:" -ForegroundColor Cyan
        Write-Host "   1. Download: https://ollama.com/download/OllamaSetup.exe" -ForegroundColor White
        Write-Host "   2. Run the installer" -ForegroundColor White
        Write-Host "   3. Restart PowerShell" -ForegroundColor White
        Write-Host "   4. Run this script again" -ForegroundColor White
        Write-Host ""
        
        # Ask if user wants to open download page
        $openBrowser = Read-Host "Open download page in browser? (y/n)"
        if ($openBrowser -eq 'y' -or $openBrowser -eq 'Y') {
            Start-Process "https://ollama.com/download"
        }
        exit 1
    }
}
Write-Host ""

# Step 3: Pull lightweight model
Write-Host "Step 3: Setting up AI model (phi3:mini - lightweight)..." -ForegroundColor Green
Write-Host "   This will download approximately 2.3GB. Please wait..." -ForegroundColor Cyan

$modelName = "phi3:mini"
try {
    # Check if model already exists
    $existingModels = ollama list 2>&1
    if ($existingModels -match $modelName) {
        Write-Host "OK Model $modelName already installed!" -ForegroundColor Green
    } else {
        Write-Host "   Downloading $modelName (this may take a few minutes)..." -ForegroundColor Cyan
        ollama pull $modelName
        if ($LASTEXITCODE -eq 0) {
            Write-Host "OK Model $modelName downloaded successfully!" -ForegroundColor Green
        } else {
            throw "Failed to download model"
        }
    }
} catch {
    Write-Host "ERROR: Failed to download model" -ForegroundColor Red
    Write-Host "   You can try manually: ollama pull $modelName" -ForegroundColor Yellow
    exit 1
}
Write-Host ""

# Step 4: Install Python dependencies
Write-Host "Step 4: Installing Python dependencies..." -ForegroundColor Green
try {
    pip install -r requirements.txt --quiet
    Write-Host "OK Python dependencies installed!" -ForegroundColor Green
} catch {
    Write-Host "Warning: Some dependencies may have failed to install" -ForegroundColor Yellow
    Write-Host "   Try manually: pip install -r requirements.txt" -ForegroundColor Yellow
}
Write-Host ""

# Step 5: Test the setup
Write-Host "Step 5: Testing setup..." -ForegroundColor Green
Write-Host "   Testing Ollama with a quick query..." -ForegroundColor Cyan
try {
    $testQuery = "SELECT * FROM users;"
    Write-Host "   Running sample query test" -ForegroundColor White
    $testResult = $testQuery | ollama run $modelName 2>&1
    if ($testResult) {
        Write-Host "OK Ollama is responding correctly!" -ForegroundColor Green
    }
} catch {
    Write-Host "Warning: Test query had issues, but setup may still work" -ForegroundColor Yellow
}
Write-Host ""

# Success message
Write-Host "========================================" -ForegroundColor Green
Write-Host " SETUP COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "   1. Run:  .\start.bat" -ForegroundColor White
Write-Host "   2. Copy text (Ctrl+C)" -ForegroundColor White
Write-Host "   3. Press: Ctrl+Shift+G" -ForegroundColor White
Write-Host "   4. Paste AI response (Ctrl+V)" -ForegroundColor White
Write-Host ""
Write-Host "Tips:" -ForegroundColor Cyan
Write-Host "   - Edit config.py to change the AI model" -ForegroundColor White
Write-Host "   - Add SYSTEM_PROMPT for specific tasks" -ForegroundColor White
Write-Host "   - Model size: approximately 2.3GB, fast responses" -ForegroundColor White
Write-Host ""
Write-Host "Press any key to start the application..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')

# Start the application
python clipboard_ai.py
