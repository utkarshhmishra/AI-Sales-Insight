# Project Structure - AI Sales Insight

## Directory Tree

```
E:\AiSalesInsight\
│
├── README.md                          # Project overview and introduction
├── QUICKSTART.md                      # Quick setup guide
├── .env.example                       # Environment variables template
├── .gitignore                         # Git ignore rules
├── docker-compose.yml                 # Docker services configuration
│
├── backend\                           # Python backend
│   ├── main.py                        # FastAPI application entry point
│   ├── requirements.txt               # Python dependencies
│   │
│   ├── agents\                        # Multi-agent system
│   │   ├── __init__.py
│   │   ├── base_agent.py             # Base agent class
│   │   ├── research_agent.py         # Company research
│   │   ├── news_agent.py             # News monitoring
│   │   ├── financial_agent.py        # Financial data
│   │   ├── social_media_agent.py     # Social media tracking
│   │   ├── insight_synthesizer.py    # LLM-powered synthesis
│   │   └── orchestrator.py           # Agent coordination
│   │
│   ├── api\                           # REST API layer
│   │   ├── __init__.py
│   │   └── v1\
│   │       ├── __init__.py
│   │       └── endpoints\
│   │           ├── __init__.py
│   │           ├── insights.py       # Insights endpoints
│   │           ├── companies.py      # Company management
│   │           ├── agents.py         # Agent status
│   │           └── health.py         # Health checks
│   │
│   ├── core\                          # Core utilities
│   │   ├── __init__.py
│   │   ├── config.py                 # Configuration management
│   │   └── logging_config.py         # Logging setup
│   │
│   ├── models\                        # Database models (future)
│   │   └── __init__.py
│   │
│   ├── services\                      # Business logic (future)
│   │   └── __init__.py
│   │
│   └── logs\                          # Application logs
│       └── app.log
│
├── frontend\                          # React frontend
│   ├── package.json                   # Node dependencies
│   ├── tsconfig.json                  # TypeScript config
│   ├── vite.config.ts                 # Vite build config
│   ├── tailwind.config.js             # Tailwind CSS config
│   ├── index.html                     # HTML entry point
│   │
│   ├── src\
│   │   ├── main.tsx                   # React entry point
│   │   ├── App.tsx                    # Main App component
│   │   ├── index.css                  # Global styles
│   │   │
│   │   ├── components\                # Reusable components
│   │   │   └── Layout.tsx             # App layout
│   │   │
│   │   ├── pages\                     # Page components
│   │   │   ├── Dashboard.tsx          # Main dashboard
│   │   │   └── InsightsPage.tsx       # Insights display
│   │   │
│   │   └── services\                  # API services
│   │       └── api.ts                 # API client
│   │
│   └── public\                        # Static assets
│
├── data\                              # Data storage (future)
│   ├── raw\                           # Raw collected data
│   └── processed\                     # Processed data
│
├── docs\                              # Documentation
│   ├── ARCHITECTURE.md                # System architecture
│   ├── TESTING.md                     # Testing guide
│   └── PRESENTATION_GUIDE.md          # Course presentation
│
├── tests\                             # Test suites (future)
│   ├── test_agents.py
│   ├── test_api.py
│   └── test_integration.py
│
└── scripts\                           # Utility scripts (future)
    ├── setup.ps1                      # Windows setup script
    └── deploy.sh                      # Deployment script
```

## Key Files Explained

### Root Level

**README.md**
- Project overview
- Architecture diagram
- Setup instructions
- Feature list
- Success metrics

**QUICKSTART.md**
- Step-by-step setup
- Quick test instructions
- Troubleshooting tips

**docker-compose.yml**
- PostgreSQL service
- Redis service
- Backend service (optional)
- Network configuration

**.env.example**
- Template for environment variables
- API key placeholders
- Configuration examples

### Backend (/backend)

**main.py** - FastAPI application
```python
- Creates FastAPI app
- Configures CORS
- Sets up routes
- Health checks
- Startup/shutdown logic
```

**agents/base_agent.py** - Agent foundation
```python
class BaseAgent(ABC):
    - execute() method (abstract)
    - validate_input()
    - log_execution()
    - create_output()
```

**agents/orchestrator.py** - Agent coordination
```python
class AgentOrchestrator:
    - gather_insights() - Full insights
    - quick_brief() - Fast mode
    - Parallel execution
    - Error handling
```

**api/v1/endpoints/insights.py** - Main API
```python
POST /insights/generate
POST /insights/quick-brief
GET /insights/history/{company}
DELETE /insights/cache/{company}
```

### Frontend (/frontend)

**src/App.tsx** - React router setup
```tsx
- Routes configuration
- Layout wrapper
- Navigation
```

**src/pages/Dashboard.tsx** - Main interface
```tsx
- Company search form
- Demo companies
- Feature cards
- Success metrics
```

**src/pages/InsightsPage.tsx** - Results display
```tsx
- Executive summary
- Agent outputs
- Talking points
- Opportunities
- Risks
```

**src/services/api.ts** - API client
```typescript
- Axios configuration
- API endpoints
- Type definitions
- Error handling
```

## File Sizes (Approximate)

```
Backend (Python):
├── main.py                    ~3 KB
├── agents/base_agent.py       ~5 KB
├── agents/research_agent.py   ~8 KB
├── agents/news_agent.py       ~7 KB
├── agents/financial_agent.py  ~7 KB
├── agents/social_media_agent.py ~7 KB
├── agents/insight_synthesizer.py ~9 KB
├── agents/orchestrator.py     ~6 KB
└── api/v1/endpoints/*.py      ~15 KB total

Frontend (TypeScript):
├── src/App.tsx                ~1 KB
├── src/pages/Dashboard.tsx    ~7 KB
├── src/pages/InsightsPage.tsx ~9 KB
├── src/components/Layout.tsx  ~3 KB
└── src/services/api.ts        ~4 KB

Documentation:
├── README.md                  ~6 KB
├── QUICKSTART.md              ~4 KB
├── ARCHITECTURE.md            ~15 KB
├── TESTING.md                 ~8 KB
└── PRESENTATION_GUIDE.md      ~12 KB

Total: ~135 KB of code + documentation
```

## Code Statistics

```
Backend Python:
- Total Lines: ~1,800
- Files: 15
- Classes: 7 (6 agents + 1 orchestrator)
- Functions: ~40
- API Endpoints: 13

Frontend TypeScript:
- Total Lines: ~800
- Files: 8
- Components: 5
- Services: 1
- Pages: 2

Documentation:
- Total Lines: ~1,200
- Files: 5
- Words: ~15,000
```

## Technology Breakdown

### Backend Dependencies (requirements.txt)
```
Core Framework:
- fastapi==0.109.0
- uvicorn==0.27.0
- pydantic==2.5.3

AI/LLM:
- langchain==0.1.4
- langchain-openai==0.0.5
- openai==1.10.0
- anthropic==0.8.1

Database:
- sqlalchemy==2.0.25
- psycopg2-binary==2.9.9
- redis==5.0.1

Total: 40+ packages
```

### Frontend Dependencies (package.json)
```
Core:
- react==18.2.0
- react-router-dom==6.21.0
- vite==5.0.8

UI:
- tailwindcss==3.4.0
- lucide-react==0.303.0

Data:
- @tanstack/react-query==5.17.0
- axios==1.6.5

Total: 20+ packages
```

## Deployment Structure (Future)

```
Production:
├── AWS/Azure/GCP
│   ├── ECS/App Service/Cloud Run (API)
│   ├── RDS/Azure SQL (PostgreSQL)
│   ├── ElastiCache/Redis Cache (Redis)
│   ├── S3/Blob Storage (Static files)
│   ├── CloudFront/CDN (Frontend)
│   └── CloudWatch/Monitor (Logging)
│
├── Domain
│   ├── api.aisalesinsight.com
│   └── app.aisalesinsight.com
│
└── CI/CD
    ├── GitHub Actions
    ├── Docker Hub
    └── Automated tests
```

## Development Workflow

```
1. Feature Development
   ├── Create feature branch
   ├── Implement backend (Python)
   ├── Implement frontend (React)
   ├── Write tests
   ├── Update docs
   └── Submit PR

2. Testing
   ├── Unit tests (pytest)
   ├── Integration tests
   ├── API tests (Postman)
   └── E2E tests (Playwright)

3. Deployment
   ├── Build Docker images
   ├── Push to registry
   ├── Deploy to staging
   ├── Run smoke tests
   └── Deploy to production
```

## Configuration Files

**Backend Config (.env)**
```env
- API keys (OpenAI, NewsAPI, etc.)
- Database URLs
- Redis URL
- Log levels
- Feature flags
```

**Frontend Config (vite.config.ts)**
```typescript
- Build settings
- Proxy configuration
- Path aliases
- Environment variables
```

**Docker Config (docker-compose.yml)**
```yaml
- Service definitions
- Network configuration
- Volume mounts
- Environment variables
```

## Best Practices Applied

1. **Separation of Concerns**
   - Backend: API, Agents, Core separated
   - Frontend: Components, Pages, Services separated

2. **Code Organization**
   - Clear directory structure
   - Logical grouping
   - Easy navigation

3. **Documentation**
   - README for overview
   - QUICKSTART for setup
   - ARCHITECTURE for design
   - Inline comments in code

4. **Configuration**
   - Environment variables
   - Config files
   - No hardcoded values

5. **Scalability**
   - Modular architecture
   - Easy to add new agents
   - Horizontal scaling ready

## Next Steps for Expansion

```
Add to project:
├── tests/                     # Comprehensive testing
├── scripts/                   # Automation scripts
├── migrations/                # Database migrations
├── monitoring/                # Grafana dashboards
├── ci-cd/                     # GitHub Actions workflows
└── terraform/                 # Infrastructure as code
```
