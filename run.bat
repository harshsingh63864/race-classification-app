@echo off
REM Flask Web Application Startup Script for Windows

echo ==========================================
echo Race Classification Web Application
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Check if requirements are installed
echo Checking dependencies...
pip freeze | findstr /i "flask torch clip" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Installing required packages...
    echo This may take a few minutes...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo ✓ All dependencies are installed
echo.

REM Check if model file exists
if not exist "clip_lvm_model.pt" (
    echo ERROR: clip_lvm_model.pt not found in current directory
    echo Please ensure the model file is in: %cd%
    pause
    exit /b 1
)

echo ✓ Model file found
echo.

REM Start the Flask application
echo Starting Flask application...
echo.
echo ==========================================
echo Open your browser and go to:
echo http://localhost:5000
echo ==========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause
