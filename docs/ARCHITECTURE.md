# AI Sales Insight - System Architecture

## Overview

AI Sales Insight is a multi-agent AI system designed to automate sales intelligence gathering. The system uses specialized agents to collect data from various sources and synthesize actionable insights for sales representatives.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Frontend (React + TypeScript)                 │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
│  │Dashboard  │  │ Insights  │  │Companies  │  │  Settings │  │
│  │   Page    │  │   Page    │  │   Page    │  │   Page    │  │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/REST
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Backend API (FastAPI)                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    API Endpoints                         │   │
│  │  /insights/generate  |  /companies  |  /agents/status   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                             │                                    │
│  ┌─────────────────────────▼────────────────────────────────┐  │
│  │                  Agent Orchestrator                       │  │
│  │            (Coordinates agent execution)                  │  │
│  └─────────────────────────┬────────────────────────────────┘  │
│                             │                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Multi-Agent System (LangChain)              │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │  │
│  │  │Research  │  │  News    │  │Financial │  │ Social │ │  │
│  │  │ Agent    │  │  Agent   │  │  Agent   │  │ Media  │ │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └────────┘ │  │
│  │                      │                                   │  │
│  │              ┌───────▼────────┐                         │  │
│  │              │    Insight     │                         │  │
│  │              │  Synthesizer   │                         │  │
│  │              │   (GPT-4/LLM)  │                         │  │
│  │              └────────────────┘                         │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Layer                                    │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│  │PostgreSQL  │  │   Redis    │  │  Chroma DB │               │
│  │ (Storage)  │  │  (Cache)   │  │  (Vector)  │               │
│  └────────────┘  └────────────┘  └────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                  External Data Sources                           │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  │
│  │NewsAPI │  │LinkedIn│  │ Yahoo  │  │Twitter │  │ Serper │  │
│  │        │  │   API  │  │Finance │  │   API  │  │  API   │  │
│  └────────┘  └────────┘  └────────┘  └────────┘  └────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend Layer (React + TypeScript)

**Technology Stack:**
- React 18 with TypeScript
- Vite (build tool)
- TanStack Query (data fetching)
- Tailwind CSS (styling)
- React Router (routing)

**Key Components:**
- **Dashboard**: Main entry point for company search
- **InsightsPage**: Display comprehensive insights
- **Layout**: Navigation and app structure
- **API Service**: Centralized API communication

### 2. Backend API (FastAPI)

**Technology Stack:**
- FastAPI (async web framework)
- Pydantic (data validation)
- Uvicorn (ASGI server)
- Python 3.11+

**API Endpoints:**

```
/api/v1/
├── insights/
│   ├── POST /generate          # Generate full insights
│   ├── POST /quick-brief       # Generate quick brief
│   ├── GET /history/{company}  # Get historical insights
│   └── DELETE /cache/{company} # Clear cache
├── companies/
│   ├── GET /                   # List companies
│   ├── POST /                  # Add company
│   ├── GET /{name}             # Get company
│   ├── PUT /{name}/track       # Track company
│   └── DELETE /{name}          # Delete company
├── agents/
│   ├── GET /status             # Agent status
│   ├── GET /capabilities       # Agent capabilities
│   └── GET /metrics            # Performance metrics
└── health/
    ├── GET /                   # Basic health check
    └── GET /detailed           # Detailed health info
```

### 3. Multi-Agent System

#### Agent Architecture

All agents inherit from `BaseAgent` class:

```python
class BaseAgent(ABC):
    - execute(input: AgentInput) -> AgentOutput
    - validate_input(input: AgentInput) -> bool
    - log_execution(input, output) -> None
```

#### Specialized Agents

**1. Research Agent**
- **Purpose**: Gather company background and decision-makers
- **Data Sources**: 
  - LinkedIn API
  - Clearbit
  - Company websites
  - Business directories
- **Output**: Company info, decision-makers, products/services
- **Avg Execution Time**: 1200ms

**2. News Agent**
- **Purpose**: Monitor news and announcements
- **Data Sources**:
  - NewsAPI
  - Google News
  - RSS feeds
  - Press releases
- **Output**: News articles, sentiment, relevance scores
- **Avg Execution Time**: 1300ms

**3. Financial Agent**
- **Purpose**: Collect financial metrics
- **Data Sources**:
  - Yahoo Finance
  - Alpha Vantage
  - Crunchbase
  - PitchBook
- **Output**: Stock data, funding, financial metrics
- **Avg Execution Time**: 1100ms

**4. Social Media Agent**
- **Purpose**: Track social presence and sentiment
- **Data Sources**:
  - LinkedIn API
  - Twitter API
  - Social listening tools
- **Output**: Engagement metrics, sentiment, trending topics
- **Avg Execution Time**: 1400ms

**5. Insight Synthesizer Agent**
- **Purpose**: Combine data and generate insights
- **Technology**: OpenAI GPT-4 / Claude 3.5
- **Output**: Executive summary, talking points, opportunities
- **Avg Execution Time**: 900ms

#### Agent Orchestrator

**Responsibilities:**
- Coordinate agent execution
- Manage parallel processing
- Handle errors and retries
- Aggregate results
- Cache management

**Execution Flow:**
```
1. Receive request (company_name, context, timeframe)
2. Create AgentInput for all agents
3. Execute data collection agents in parallel:
   - ResearchAgent
   - NewsAgent
   - FinancialAgent
   - SocialMediaAgent
4. Wait for all agents to complete
5. Pass combined data to InsightSynthesizer
6. Return comprehensive results
7. Cache results (optional)
```

### 4. Data Layer

**PostgreSQL:**
- User accounts and authentication
- Company records
- Historical insights
- Analytics and metrics

**Redis:**
- Session management
- API rate limiting
- Cached insights (24-hour TTL)
- Background job queue

**Chroma DB (Vector Database):**
- Semantic search over historical insights
- Similar company recommendations
- RAG (Retrieval Augmented Generation)

### 5. Data Sources Integration

**External APIs:**
- NewsAPI: News articles (Free tier: 100 req/day)
- LinkedIn API: Professional data
- Twitter API: Social media monitoring
- Yahoo Finance: Stock data
- Alpha Vantage: Financial metrics
- Serper: Web search (Free tier: 2,500 searches)

**Authentication:**
- API keys stored in environment variables
- Secure storage in production (AWS Secrets Manager)
- Rate limiting and retry logic

## Data Flow

### Insight Generation Flow

```
1. User submits company name via frontend
   ↓
2. Frontend sends POST /api/v1/insights/generate
   ↓
3. Backend validates request
   ↓
4. Orchestrator creates agent tasks
   ↓
5. Agents execute in parallel (2-3 seconds)
   ├── ResearchAgent → Company background
   ├── NewsAgent → Recent news
   ├── FinancialAgent → Financial data
   └── SocialMediaAgent → Social presence
   ↓
6. InsightSynthesizer processes combined data
   ↓
7. LLM generates:
   - Executive summary
   - Talking points
   - Opportunities
   - Risks
   - Action items
   ↓
8. Results cached in Redis (24h TTL)
   ↓
9. Results saved to PostgreSQL
   ↓
10. Response sent to frontend
    ↓
11. Frontend displays insights
```

## Scalability Considerations

### Horizontal Scaling
- API servers can be load-balanced
- Agents can run on separate workers
- Database read replicas for queries

### Caching Strategy
- Redis for hot data (recent insights)
- CDN for static frontend assets
- Browser caching for API responses

### Performance Optimization
- Parallel agent execution
- Async I/O for API calls
- Connection pooling for databases
- Response pagination

## Security

### API Security
- CORS configuration
- Rate limiting
- Input validation (Pydantic)
- SQL injection prevention (SQLAlchemy ORM)

### Data Security
- Environment variables for secrets
- HTTPS in production
- Database encryption at rest
- API key rotation

## Monitoring & Observability

### Logging
- Structured logging (JSON format)
- Log levels: DEBUG, INFO, WARNING, ERROR
- Centralized log aggregation (ELK stack)

### Metrics
- Request latency
- Agent execution times
- Error rates
- API usage statistics

### Alerts
- High error rates
- Slow response times
- API quota exhaustion
- Database connection issues

## Future Enhancements

1. **CRM Integration**: Salesforce, HubSpot, Zoho
2. **Email Integration**: Gmail, Outlook
3. **Advanced Analytics**: Predictive insights, trend analysis
4. **Mobile App**: React Native
5. **Team Collaboration**: Shared insights, comments
6. **Custom Alerts**: Webhook notifications
7. **Multi-language**: Hindi, Tamil, Telugu support
8. **Voice Briefings**: Text-to-speech summaries
