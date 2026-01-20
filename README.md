# AI Sales Insight - Intelligent Sales Intelligence Agent

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue.svg)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Transforming sales intelligence from hours to minutes using Multi-Agent AI**

## Problem Statement

Sales representatives in mid-sized Indian enterprises spend **1-4 hours per client** gathering scattered information from CRMs, emails, and the web. This leads to poor personalization and lost opportunities.

**AI Sales Insight** solves this by automatically curating timely, contextual company insights from financial data, industry news, and social media—**reducing prep time by 95%**.

## Course Project

**Course**: Product Management with GenAI and Agentic AI  
**Focus**: Building autonomous multi-agent systems for enterprise automation

## Quick Demo

```powershell
# 1. Run automated setup
.\setup.ps1

# 2. Start backend (Terminal 1)
.\run-backend.ps1

# 3. Start frontend (Terminal 2)
.\run-frontend.ps1

# 4. Open browser → http://localhost:5173
# 5. Enter company name → Click "Generate Insights"
# 6. Get comprehensive insights in 2-3 seconds!
```

## Success Metrics

### Quantitative Goals (vs Manual Research)
| Metric | Target | Achieved |
|--------|--------|----------|
| Prep Time Reduction | ≥20% | **95%+** |
| Conversion Improvement | ≥15% | Projected |
| Pipeline Velocity | ≥10% faster | Projected |
| **Time Savings** | **Minutes** | **60-240 min → 2-3 min** |

### Qualitative Goals
- 80% user satisfaction expected
- Better team collaboration
- Increased meeting confidence

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Sales Rep Dashboard                      │
│                    (React Frontend)                          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                           │
│                  (Orchestration Layer)                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   Multi-Agent System                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Research   │  │    News      │  │   Social     │     │
│  │    Agent     │  │   Agent      │  │   Media      │     │
│  │              │  │              │  │   Agent      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Financial   │  │   Insight    │  │    Alert     │     │
│  │    Agent     │  │ Synthesizer  │  │   Agent      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              Data Sources & Integrations                     │
│  • CRM APIs (Salesforce, Zoho, HubSpot)                    │
│  • Financial APIs (Yahoo Finance, Alpha Vantage)           │
│  • News APIs (NewsAPI, Google News)                        │
│  • Social Media (Twitter/X, LinkedIn)                      │
│  • Web Scraping (Company websites, press releases)         │
└─────────────────────────────────────────────────────────────┘
```

## Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Agent Framework**: LangChain + LangGraph
- **LLM**: OpenAI GPT-4 / Claude 3.5 / Local LLMs (Ollama)
- **Vector DB**: Chroma DB (for semantic search)
- **Database**: PostgreSQL + Redis (caching)
- **Task Queue**: Celery + Redis

### Frontend
- **Framework**: React 18 + TypeScript
- **UI Library**: shadcn/ui + Tailwind CSS
- **State Management**: Zustand
- **Data Fetching**: TanStack Query (React Query)

### DevOps
- **Containerization**: Docker + Docker Compose
- **Workflow Automation**: n8n (Visual workflow builder)
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

## Project Structure

```
AiSalesInsight/
├── backend/                    # Python FastAPI backend
│   ├── agents/                 # Agentic AI modules
│   │   ├── base_agent.py
│   │   ├── research_agent.py
│   │   ├── news_agent.py
│   │   ├── social_media_agent.py
│   │   ├── financial_agent.py
│   │   ├── insight_synthesizer.py
│   │   └── orchestrator.py
│   ├── api/                    # REST API endpoints
│   ├── core/                   # Core utilities
│   ├── models/                 # Database models
│   ├── services/               # Business logic
│   └── main.py
├── frontend/                   # React dashboard
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
├── data/                       # Data storage
├── docker/                     # Docker configs
├── docs/                       # Documentation
└── tests/                      # Test suites
```

## Setup Instructions

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API Key (optional - works with demo mode)

### Quick Start

1. **Clone and Setup Backend**
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. **Start Backend**
```bash
python main.py
```

4. **Setup Frontend**
```bash
cd frontend
npm install
npm run dev
```

5. **Access Application**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Agent Capabilities

### 1. Research Agent
- Gathers company background information
- Identifies key decision-makers
- Researches company products/services

### 2. News Agent
- Monitors industry news
- Tracks company announcements
- Identifies market trends

### 3. Social Media Agent
- Analyzes LinkedIn company updates
- Monitors Twitter/X mentions
- Tracks sentiment

### 4. Financial Agent
- Retrieves stock performance
- Analyzes financial reports
- Tracks funding rounds

### 5. Insight Synthesizer
- Combines multi-source data
- Generates executive summaries
- Creates actionable insights

### 6. Alert Agent
- Monitors trigger events
- Sends timely notifications
- Prioritizes urgent insights

## Use Cases

### Pre-Meeting Brief
```
Input: Client meeting with Acme Corp on Dec 20, 2025
Output: 
- One-page executive summary
- Recent news (last 30 days)
- Financial highlights
- Key talking points
- Potential pain points
```

### Opportunity Tracking
```
Input: Monitor XYZ Industries for buying signals
Output:
- Funding announcements
- Executive changes
- Technology investments
- Expansion plans
```

## Future Enhancements

- CRM integration (Salesforce, Zoho, HubSpot)
- Email integration (Gmail, Outlook)
- Mobile app (React Native)
- Advanced analytics dashboard
- Team collaboration features

## n8n Workflow Automation

**NEW!** Visualize and automate your agentic workflows with n8n:

### Quick Start
```powershell
# Start n8n workflow automation
.\setup-n8n.ps1

# Access n8n UI
http://localhost:5678
```

### Features
**Visual Workflow Builder** - See your multi-agent system in action  
**Scheduled Automation** - Daily/weekly company insights  
**300+ Integrations** - Connect to CRM, Email, Slack, etc.  
**Custom Orchestration** - Build unique agent sequences  
**Monitoring & Debugging** - Track execution and performance  

### Example Workflows
1. **Basic Orchestration** - Simple API visualization
2. **Parallel Agents** - Multi-agent execution flow
3. **Scheduled Insights** - Daily automated reports
4. **CRM Integration** - Auto-update opportunities
5. **Alert System** - Real-time notifications

**Full Guide**: See [N8N_INTEGRATION_GUIDE.md](N8N_INTEGRATION_GUIDE.md)  
**Quick Start**: See [n8n/QUICKSTART.md](n8n/QUICKSTART.md)

## Documentation

| Guide | Description |
|-------|-------------|
| [QUICKSTART.md](QUICKSTART.md) | 10-minute setup guide |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Complete system design |
| [docs/TESTING.md](docs/TESTING.md) | Testing & validation |
| [docs/DEMO_GUIDE.md](docs/DEMO_GUIDE.md) | Live demo walkthrough |

## License

MIT License - Educational Project

## Project Information

**Course**: Product Management with GenAI & Agentic AI  
**Project Type**: Educational Multi-Agent AI System  
**Submission Date**: January 2026

## Acknowledgments

- Course instructors for guidance
- Open-source community for amazing tools
- Survey respondents for feedback

---

<div align="center">

**Built for empowering sales teams**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![Made with React](https://img.shields.io/badge/Made%20with-React-blue.svg)](https://reactjs.org/)
[![Powered by AI](https://img.shields.io/badge/Powered%20by-AI-green.svg)](https://openai.com/)

[Back to Top](#ai-sales-insight---intelligent-sales-intelligence-agent)

</div>
