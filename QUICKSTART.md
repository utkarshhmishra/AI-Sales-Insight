# Quick Start Guide - AI Sales Insight

Get the AI Sales Insight system running in 10 minutes.

## Prerequisites

- Python 3.11+
- Node.js 18+
- OpenAI API Key (optional - works with demo mode)

## Installation Steps

### 1. Clone and Setup

```powershell
# Navigate to project directory
cd E:\AiSalesInsight

# Create and activate Python virtual environment
cd backend
python -m venv venv
.\venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```powershell
# Copy environment template
cp .env.example .env

# Edit .env file with your API keys
notepad .env
```

**Minimum Required Configuration:**
```env
# For demo/development, you can use Ollama (local LLM)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# OR use OpenAI (recommended for production)
OPENAI_API_KEY=sk-your-key-here

# Database URLs (use defaults for local dev)
DATABASE_URL=postgresql://salesinsight:salesinsight123@localhost:5432/ai_sales_insight
REDIS_URL=redis://localhost:6379/0
```

### 3. Start Database Services

```powershell
# Start PostgreSQL and Redis using Docker
docker-compose up -d
```

### 4. Start Backend

```powershell
# From backend directory
python main.py
```

Backend will be available at: http://localhost:8000
API Documentation: http://localhost:8000/docs

### 5. Start Frontend

Open a new PowerShell terminal:

```powershell
# Navigate to frontend
cd E:\AiSalesInsight\frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at: http://localhost:5173

## Quick Test

1. Open browser to http://localhost:5173
2. Enter a company name (e.g., "Acme Corp")
3. Click "Generate Insights"
4. View the AI-generated insights!

## API Keys Setup

### Free Tier Options

1. **NewsAPI** (Free tier: 100 requests/day)
   - https://newsapi.org/register
   - Add to `.env`: `NEWS_API_KEY=your-key`

2. **Alpha Vantage** (Free tier: 5 calls/minute)
   - https://www.alphavantage.co/support/#api-key
   - Add to `.env`: `ALPHA_VANTAGE_API_KEY=your-key`

3. **Serper** (Free tier: 2,500 searches)
   - https://serper.dev/
   - Add to `.env`: `SERPER_API_KEY=your-key`

### Using Local LLM (Ollama) - FREE!

```powershell
# Install Ollama
winget install Ollama.Ollama

# Pull a model
ollama pull llama2

# Ollama will run on http://localhost:11434
```

## Troubleshooting

### Port Already in Use
```powershell
# Check what's using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID)
taskkill /PID <PID> /F
```

### Database Connection Error
```powershell
# Check if Docker containers are running
docker ps

# Restart containers
docker-compose down
docker-compose up -d
```

## Next Steps

- Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for complete system design
- Check [docs/TESTING.md](docs/TESTING.md) for testing guide
- See [docs/DEMO_GUIDE.md](docs/DEMO_GUIDE.md) for presentation walkthrough
- Review API docs at http://localhost:8000/docs

---

**Project**: AI Sales Insight - Multi-Agent Sales Intelligence System  
**Course**: Product Management with GenAI & Agentic AI
- Check logs in `backend/logs/app.log`
