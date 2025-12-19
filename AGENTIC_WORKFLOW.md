# AI-Powered Agentic Workflow Setup Guide

This guide explains how to set up the enhanced agentic workflow with real AI capabilities, including LLM integration and external data sources.

## 🚀 Architecture Overview

### Multi-Agent System

```
┌─────────────────────────────────────────────┐
│          Agent Orchestrator                 │
│  (Coordinates parallel agent execution)     │
└────────────┬────────────────────────────────┘
             │
             ├──► Research Agent ──► Company data, decision makers
             │
             ├──► News Agent ──────► NewsAPI, web search
             │
             ├──► Financial Agent ─► Stock data, funding info
             │
             ├──► Social Agent ────► LinkedIn, Twitter sentiment
             │
             └──► Synthesizer ─────► LLM (GPT-4/Claude)
                       │
                       ▼
              Actionable Insights
```

### Key Components

1. **LLM Service** (`services/llm_service.py`)
   - Unified interface for OpenAI, Anthropic, and Ollama
   - Automatic provider selection based on available API keys
   - Fallback to templates when no LLM is configured

2. **Data Sources Service** (`services/data_sources_service.py`)
   - NewsAPI integration for company news
   - Serper API for web search
   - Clearbit API for company enrichment
   - Alpha Vantage for stock data

3. **Enhanced Agents**
   - Real-time data fetching
   - LLM-powered analysis
   - Graceful fallbacks to mock data

## 🔧 Setup Instructions

### Level 1: Basic Setup (Demo Mode)

**No API keys required** - Uses mock data and templates

```bash
# Just run the application
cd backend
python main.py
```

**What you get:**
- ✅ Full UI/UX
- ✅ Mock company data
- ✅ Template-based insights
- ❌ Not personalized to actual companies

### Level 2: LLM-Powered Insights (Recommended)

**Add ONE LLM provider** - Get AI-powered synthesis

#### Option A: OpenAI (Best Quality)

1. Get API key: https://platform.openai.com/api-keys
2. Add to `.env`:
```env
OPENAI_API_KEY=sk-proj-...
OPENAI_MODEL=gpt-4o
```

**Cost:** ~$0.01-0.05 per company analysis

#### Option B: Anthropic Claude (Great Alternative)

1. Get API key: https://console.anthropic.com/
2. Add to `.env`:
```env
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

**Cost:** ~$0.02-0.06 per company analysis

#### Option C: Ollama (Free, Local)

1. Install Ollama: https://ollama.ai/download
2. Pull model:
```bash
ollama pull llama3.2
```
3. Add to `.env`:
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

**Cost:** FREE (runs on your machine)
**Trade-off:** Slower, lower quality than GPT-4/Claude

**What you get:**
- ✅ AI-powered executive summaries
- ✅ Personalized talking points
- ✅ Context-aware recommendations
- ⚠️ Still uses mock data for research

### Level 3: Real Data Sources (Production-Ready)

**Add external APIs** - Get real company intelligence

#### NewsAPI (News Articles)

1. Get free key: https://newsapi.org/ (500 requests/day)
2. Add to `.env`:
```env
NEWSAPI_KEY=your-key-here
```

#### Serper API (Web Search)

1. Get free key: https://serper.dev/ (2500 searches free)
2. Add to `.env`:
```env
SERPER_API_KEY=your-key-here
```

#### Alpha Vantage (Stock Data)

1. Get free key: https://www.alphavantage.co/support/#api-key (25 requests/day)
2. Add to `.env`:
```env
ALPHAVANTAGE_API_KEY=your-key-here
```

#### Clearbit (Company Enrichment)

1. Get key: https://clearbit.com/ (Paid - ~$99/month)
2. Add to `.env`:
```env
CLEARBIT_API_KEY=your-key-here
```

**What you get:**
- ✅ Real company news and announcements
- ✅ Actual stock prices and financial data
- ✅ Company size, industry, tech stack
- ✅ Decision maker information

### Level 4: Full Production Setup

**All APIs configured** - Maximum intelligence

```env
# LLM
OPENAI_API_KEY=sk-proj-...

# Data Sources
NEWSAPI_KEY=...
SERPER_API_KEY=...
ALPHAVANTAGE_API_KEY=...
CLEARBIT_API_KEY=...

# Optional: CRM Integration
SALESFORCE_CLIENT_ID=...
HUBSPOT_API_KEY=...
```

**What you get:**
- ✅ Complete AI-powered insights
- ✅ Real-time data from multiple sources
- ✅ Personalized for every company
- ✅ CRM integration (optional)

## 💰 Cost Breakdown

### Minimal Setup (Recommended for Demo)
- **LLM:** OpenAI GPT-4o - $0.02/analysis
- **News:** NewsAPI Free - 500/day
- **Search:** Serper Free - 2500 total
- **Total:** ~$2-5/month for 100-250 analyses

### Production Setup
- **LLM:** OpenAI GPT-4 - $0.05/analysis
- **News:** NewsAPI Business - $449/month
- **Company Data:** Clearbit - $99-299/month
- **Financial:** Alpha Vantage Premium - $50/month
- **Total:** ~$600-900/month for unlimited use

## 📊 Performance Comparison

| Configuration | Speed | Quality | Cost | Best For |
|--------------|-------|---------|------|----------|
| Demo (No APIs) | ⚡⚡⚡ | ⭐⭐ | 💰 Free | Presentation |
| LLM Only | ⚡⚡ | ⭐⭐⭐⭐ | 💰💰 | MVP/Testing |
| LLM + Free APIs | ⚡⚡ | ⭐⭐⭐⭐⭐ | 💰💰 | Small Teams |
| Full Production | ⚡ | ⭐⭐⭐⭐⭐ | 💰💰💰 | Enterprise |

## 🎯 Testing Your Setup

### 1. Check LLM Connection

```python
# Test script
from services.llm_service import get_llm_service
import asyncio

async def test_llm():
    llm = get_llm_service()
    response = await llm.generate_completion("Say hello!")
    print(response)

asyncio.run(test_llm())
```

### 2. Check Data Sources

```python
from services.data_sources_service import get_data_sources_service
import asyncio

async def test_news():
    ds = get_data_sources_service()
    news = await ds.search_company_news("Microsoft", days_back=7)
    print(f"Found {len(news)} articles")

asyncio.run(test_news())
```

### 3. Run Full Analysis

```bash
# Start backend
cd backend
python main.py

# Start frontend
cd frontend
npm run dev

# Test with a real company: Microsoft, Salesforce, Adobe
```

## 🔍 How It Works

### Agent Execution Flow

```python
# 1. User submits company name "Microsoft"

# 2. Orchestrator spawns agents in parallel
agents = [ResearchAgent(), NewsAgent(), FinancialAgent(), SocialAgent()]
results = await asyncio.gather(*[agent.execute(input) for agent in agents])

# 3. Each agent:
#    - Fetches data from APIs (or uses mock data)
#    - Processes and structures the data
#    - Returns insights with confidence scores

# 4. Synthesizer Agent:
#    - Receives all agent outputs
#    - Constructs LLM prompt with context
#    - Generates personalized summary
#    - Extracts talking points, opportunities, risks

# 5. Results returned to frontend (2-3 seconds total)
```

### LLM Synthesis Process

```python
# System Prompt
"You are a B2B sales intelligence analyst. Synthesize this data..."

# User Prompt
"Generate executive summary for Microsoft based on:
- Research: [employee count, decision makers, tech stack]
- News: [3 recent articles with sentiment]
- Financial: [stock price, revenue growth, funding]
- Social: [LinkedIn activity, brand sentiment]

Create a 400-word brief for a sales rep..."

# LLM Response
"Microsoft - Executive Brief
**Company Overview:** Microsoft is a $3T cloud computing..."
```

## 🚨 Common Issues

### "LLM client not available"
- ✅ Add `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` to `.env`
- ✅ Restart the backend server
- ✅ Check API key is valid

### "Using fallback generation"
- ⚠️ No LLM configured - add API key
- ⚠️ Or install Ollama for local LLM

### "NewsAPI error: 401"
- ✅ Check `NEWSAPI_KEY` in `.env`
- ✅ Verify key at https://newsapi.org/account

### Slow responses
- ⚠️ Using Ollama (local LLM) - expect 10-30s
- ✅ Switch to OpenAI/Claude for 2-3s response

## 📈 Optimization Tips

1. **Caching:** Implement Redis caching for repeated queries
2. **Batch Processing:** Process multiple companies together
3. **Async Execution:** Already implemented - agents run in parallel
4. **Rate Limiting:** Add request throttling for API limits
5. **CDN:** Cache static company data (logo, industry, size)

## 🎓 Learn More

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic Claude](https://docs.anthropic.com/)
- [LangChain Guide](https://python.langchain.com/)
- [Agentic AI Patterns](https://www.anthropic.com/research/agents)

## 🤝 Support

Having issues? Check:
1. `.env` file is in project root
2. Backend logs for error messages
3. API keys are valid and not expired
4. Network can reach external APIs

For course presentation: Use Level 1 (Demo Mode) or Level 2 (OpenAI) for best results.
