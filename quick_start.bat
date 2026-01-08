@echo off
echo ========================================
echo Tukey Backend - Quick Start Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

echo [2/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo [3/4] Checking for .env file...
if not exist .env (
    echo WARNING: .env file not found!
    echo Creating .env file template...
    (
        echo OPENAI_API_KEY=your_openai_api_key_here
        echo OPENAI_MODEL=gpt-3.5-turbo
    ) > .env
    echo.
    echo Please edit .env file and add your OpenAI API key!
    echo Press any key to open .env file in notepad...
    pause >nul
    notepad .env
) else (
    echo .env file found!
)
echo.

echo [4/4] Starting server...
echo.
echo ========================================
echo Server will start at http://localhost:8000
echo Press Ctrl+C to stop the server
echo ========================================
echo.

uvicorn app.main:app --reload

pause




