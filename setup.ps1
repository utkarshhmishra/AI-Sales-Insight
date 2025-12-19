# AI Sales Insight - Automated Setup Script for Windows
# Run with: .\setup.ps1

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "AI Sales Insight - Automated Setup" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Python not found. Please install Python 3.11+" -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host "Checking Node.js..." -ForegroundColor Yellow
$nodeVersion = node --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Node.js found: $nodeVersion" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Node.js not found. Please install Node.js 18+" -ForegroundColor Red
    exit 1
}

# Check Docker
Write-Host "Checking Docker..." -ForegroundColor Yellow
$dockerVersion = docker --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Docker found: $dockerVersion" -ForegroundColor Green
} else {
    Write-Host "Docker not found. You'll need to install PostgreSQL and Redis manually" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Setting up Backend..." -ForegroundColor Cyan
Write-Host "===================" -ForegroundColor Cyan

# Setup backend
Set-Location backend

# Create virtual environment
if (!(Test-Path "venv")) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install --upgrade pip
pip install -r requirements.txt
Write-Host "[OK] Python dependencies installed" -ForegroundColor Green

# Setup environment file
Set-Location ..
if (!(Test-Path ".env")) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "[OK] .env file created (please configure with your API keys)" -ForegroundColor Green
} else {
    Write-Host "[OK] .env file already exists" -ForegroundColor Green
}

Write-Host ""
Write-Host "Setting up Frontend..." -ForegroundColor Cyan
Write-Host "====================" -ForegroundColor Cyan

# Setup frontend
Set-Location frontend

Write-Host "Installing Node.js dependencies..." -ForegroundColor Yellow
npm install
Write-Host "[OK] Node.js dependencies installed" -ForegroundColor Green

Set-Location ..

Write-Host ""
Write-Host "Starting Docker Services..." -ForegroundColor Cyan
Write-Host "===========================" -ForegroundColor Cyan

# Start Docker services
if ($dockerVersion) {
    Write-Host "Starting PostgreSQL and Redis..." -ForegroundColor Yellow
    docker-compose up -d
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Database services started" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] Failed to start database services" -ForegroundColor Yellow
    }
} else {
    Write-Host "[WARNING] Skipping Docker services (Docker not installed)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "[SUCCESS] Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "----------" -ForegroundColor Cyan
Write-Host "1. Configure API keys in .env file:" -ForegroundColor White
Write-Host "   notepad .env" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Start the backend:" -ForegroundColor White
Write-Host "   cd backend" -ForegroundColor Gray
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "   python main.py" -ForegroundColor Gray
Write-Host ""
Write-Host "3. In a new terminal, start the frontend:" -ForegroundColor White
Write-Host "   cd frontend" -ForegroundColor Gray
Write-Host "   npm run dev" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Open your browser:" -ForegroundColor White
Write-Host "   Frontend: http://localhost:5173" -ForegroundColor Gray
Write-Host "   API Docs: http://localhost:8000/docs" -ForegroundColor Gray
Write-Host ""
Write-Host "For detailed instructions, see QUICKSTART.md" -ForegroundColor Yellow
Write-Host ""
