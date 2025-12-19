# AI Sales Insight - Run Frontend
# Quick script to start the frontend development server

Write-Host "Starting AI Sales Insight Frontend..." -ForegroundColor Cyan
Write-Host ""

# Change to frontend directory
Set-Location frontend

# Check if node_modules exists
if (!(Test-Path "node_modules")) {
    Write-Host "node_modules not found. Installing dependencies..." -ForegroundColor Yellow
    npm install
}

# Start development server
Write-Host "Starting Vite development server..." -ForegroundColor Green
Write-Host "Frontend will be available at: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

npm run dev
