# AI Sales Insight - Run Backend
# Quick script to start the backend server

Write-Host "Starting AI Sales Insight Backend..." -ForegroundColor Cyan
Write-Host ""

# Change to backend directory
Set-Location backend

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & ".\venv\Scripts\Activate.ps1"
} else {
    Write-Host "Virtual environment not found. Run setup.ps1 first." -ForegroundColor Red
    exit 1
}

# Check if .env exists
if (!(Test-Path "..\env")) {
    Write-Host "Warning: .env file not found. Using defaults." -ForegroundColor Yellow
}

# Start server
Write-Host "Starting FastAPI server..." -ForegroundColor Green
Write-Host "API will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python main.py
