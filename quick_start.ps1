# Tukey Backend - Quick Start Script (PowerShell)
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Tukey Backend - Quick Start Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "[1/4] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Install dependencies
Write-Host "[2/4] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ ERROR: Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
Write-Host ""

# Check for .env file
Write-Host "[3/4] Checking for .env file..." -ForegroundColor Yellow
if (-not (Test-Path .env)) {
    Write-Host "⚠ WARNING: .env file not found!" -ForegroundColor Yellow
    Write-Host "Creating .env file template..." -ForegroundColor Yellow
    
    @"
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
"@ | Out-File -FilePath .env -Encoding utf8NoBOM
    
    Write-Host "✓ .env file created" -ForegroundColor Green
    Write-Host ""
    Write-Host "Please edit .env file and add your OpenAI API key!" -ForegroundColor Yellow
    $response = Read-Host "Press Enter to open .env file in notepad (or 'n' to skip)"
    if ($response -ne 'n') {
        notepad .env
    }
} else {
    Write-Host "✓ .env file found!" -ForegroundColor Green
}
Write-Host ""

# Start server
Write-Host "[4/4] Starting server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Server will start at http://localhost:8000" -ForegroundColor Green
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

uvicorn app.main:app --reload




