# AI Agent Workflow Prompts

**Project**: AI Sales Insight - Multi-Agent System  
**Purpose**: Generate AI agent workflow diagrams for Component 7 (Demo/Prototype - 10 Marks)

---

## Prompt 1: High-Level Architecture Flowchart

```
Create a flowchart diagram showing AI multi-agent system architecture:

START: User inputs company name

ORCHESTRATOR (center, blue rectangle):
- "Orchestrator Agent"
- Receives request
- Coordinates 4 parallel agents

4 PARALLEL BRANCHES (same level, different colors):
1. Research Agent (green) - "Company data & decision makers"
2. News Agent (orange) - "Recent news & articles"
3. Financial Agent (purple) - "Financial metrics & performance"
4. Social Media Agent (cyan) - "LinkedIn & social presence"

Each agent box shows:
- Agent icon/emoji
- Agent name
- 2-3 bullet points of tasks
- API connections (dotted lines to external services)

CONVERGENCE:
- All 4 agents flow into "Data Collection Complete"
- Arrow to "Insight Synthesizer" (gold rectangle)

INSIGHT SYNTHESIZER:
- "AI-Powered Analysis"
- Uses GPT-4/Claude
- Generates executive summary
- Creates talking points
- Identifies opportunities & risks

OUTPUT: "Comprehensive Insights Report" (green rounded box)

ERROR HANDLING (side branch, red):
- "Agent Failure?" diamond
- "Use cached data" → "Fallback mode"
- "Partial insights" output

STYLE: Clean flowchart, rounded rectangles, clear arrows, color-coded by agent type
TOOLS: Figma, Miro, Lucidchart, Whimsical
SIZE: 1920x1080px landscape
```

---

## Prompt 2: Sequence Diagram (Agent Execution Flow)

```
Create a sequence diagram showing agent execution timeline:

PARTICIPANTS (vertical lanes):
1. User/Client
2. API Gateway
3. Orchestrator
4. Research Agent
5. News Agent
6. Financial Agent
7. Social Media Agent
8. Insight Synthesizer
9. Database

SEQUENCE FLOW:
1. User → API: POST /insights {company: "Infosys"}
2. API → Orchestrator: Trigger analysis
3. Orchestrator → All 4 Agents: Parallel dispatch (simultaneous arrows)
4. Research Agent → External APIs: Fetch company data (2-3s)
5. News Agent → NewsAPI: Fetch articles (1-2s)
6. Financial Agent → Yahoo Finance: Fetch metrics (2-3s)
7. Social Media Agent → LinkedIn: Fetch presence (3-4s)
8. All Agents → Orchestrator: Return results (staggered timing)
9. Orchestrator → Insight Synthesizer: Aggregate data
10. Insight Synthesizer → LLM: Generate insights (2-3s)
11. Insight Synthesizer → Database: Cache results
12. Insight Synthesizer → API: Return insights
13. API → User: 200 OK + JSON response

TIMING LABELS: Show duration for each step (e.g., "2.8s total")
ERROR PATH: Dotted line showing timeout → fallback → cached data

STYLE: UML sequence diagram format, time axis vertical, color-coded messages
```

---

## Prompt 3: Data Flow Diagram (Information Processing)

```
Create a data flow diagram for multi-agent intelligence system:

LAYER 1 - INPUT (top):
- Circle: "User Input" containing "Company name: Infosys"

LAYER 2 - ORCHESTRATION:
- Rectangle: "Orchestrator" 
- Validates input, initiates parallel processing

LAYER 3 - AGENT LAYER (4 parallel processing units):
Each agent shows INPUT → PROCESS → OUTPUT:

1. Research Agent:
   - IN: Company name
   - PROCESS: Web scraping, company DB lookup
   - OUT: {company_overview, decision_makers[], products[]}

2. News Agent:
   - IN: Company name
   - PROCESS: NewsAPI search, article filtering
   - OUT: {news_items[], sentiment_score, recent_events[]}

3. Financial Agent:
   - IN: Company ticker/name
   - PROCESS: Yahoo Finance API, metric calculation
   - OUT: {revenue, growth_rate, market_cap, ratios}

4. Social Media Agent:
   - IN: Company domain
   - PROCESS: LinkedIn scraping, engagement metrics
   - OUT: {follower_count, recent_posts[], engagement_rate}

LAYER 4 - SYNTHESIS:
- Diamond: "Data Aggregation"
- Rectangle: "Insight Synthesizer (GPT-4)"
- Shows: Raw data → AI processing → Structured insights

LAYER 5 - OUTPUT (bottom):
- Rectangle: "Final Report" containing:
  - Executive Summary
  - Talking Points (5)
  - Opportunities (3)
  - Risks (3)
  - Confidence Score: 94%

DATA STORES (side):
- Cylinder: "Cache DB" (for failed requests)
- Cylinder: "Results DB" (for history)

STYLE: Traditional DFD notation, circles for external entities, rectangles for processes, arrows showing data flow
```

---

## Prompt 4: System Context Diagram (Agent Ecosystem)

```
Create a system context diagram showing AI agent ecosystem:

CENTER: Large box "AI Sales Insight System" containing 5 agent icons

EXTERNAL SYSTEMS (surrounding, with bidirectional arrows):
1. NewsAPI (top-left) ↔ News Agent
2. Yahoo Finance (top-right) ↔ Financial Agent
3. LinkedIn API (bottom-left) ↔ Social Media Agent
4. Company Websites (bottom-right) ↔ Research Agent
5. OpenAI/Claude API (right) ↔ Insight Synthesizer
6. PostgreSQL/Cache (left) ↔ All Agents
7. User Interface (top-center) ↔ Orchestrator

ANNOTATIONS:
- Show data type for each connection
- Show frequency (real-time, cached, on-demand)
- Show authentication method (API key, OAuth, public)

LEGEND:
- Solid arrow: Real-time data
- Dashed arrow: Cached/fallback data
- Dotted arrow: Optional/backup

STYLE: Clean architecture diagram, rounded boxes, clear labels, professional color scheme
```

---

## Prompt 5: Agent State Machine (Lifecycle Diagram)

```
Create a state machine diagram showing agent lifecycle:

STATES (rounded rectangles):
1. IDLE (gray) - "Waiting for trigger"
2. TRIGGERED (yellow) - "Request received"
3. FETCHING (blue) - "Calling external APIs"
4. PROCESSING (purple) - "Analyzing data"
5. COMPLETED (green) - "Results ready"
6. FAILED (red) - "Error occurred"
7. CACHED (orange) - "Using fallback data"

TRANSITIONS (arrows with conditions):
- IDLE → TRIGGERED: "New company request"
- TRIGGERED → FETCHING: "Validation passed"
- FETCHING → PROCESSING: "API response 200 OK"
- FETCHING → FAILED: "API timeout/error"
- FAILED → CACHED: "Cache exists"
- FAILED → COMPLETED: "Partial data acceptable"
- PROCESSING → COMPLETED: "Data analysis done"
- COMPLETED → IDLE: "Results sent"
- CACHED → PROCESSING: "Using cached data"

TIMING ANNOTATIONS:
- FETCHING: "Max 5s"
- PROCESSING: "Max 3s"
- FAILED → CACHED: "Retry 3x before fallback"

SHOW FOR: One agent (e.g., News Agent) as example
STYLE: UML state machine diagram, clear state transitions, timing constraints
```

---

## Prompt 6: Component Architecture Diagram

```
Create a component architecture diagram with 3 layers:

PRESENTATION LAYER (top, light blue):
- "React Frontend"
- "Dashboard Component"
- "Insights Display Component"
- HTTP/REST connection arrows downward

APPLICATION LAYER (middle, light green):
- "FastAPI Backend"
- Components:
  - "API Gateway" (entry point)
  - "Orchestrator Agent" (coordinator)
  - "Agent Manager" (lifecycle control)
- Sub-components (nested boxes):
  - Research Agent
  - News Agent
  - Financial Agent
  - Social Media Agent
  - Insight Synthesizer

DATA LAYER (bottom, light yellow):
- "Cache Service" (Redis/Memory)
- "Results Database" (PostgreSQL)
- "LLM Service" (OpenAI/Claude)

EXTERNAL SERVICES (right side, gray):
- NewsAPI
- Yahoo Finance
- LinkedIn
- Web Scraping Service

CONNECTIONS:
- Show interfaces between components
- Label with protocols (REST, HTTP, SQL)
- Show async/parallel execution paths

STYLE: Layered architecture, nested boxes for sub-components, clear boundaries
```

---

## Prompt 7: Workflow Timeline (Gantt-style Execution)

```
Create a timeline diagram showing parallel agent execution:

HORIZONTAL AXIS: Time (0s to 10s)
VERTICAL AXIS: Agents/Tasks

TASK BARS (color-coded horizontal rectangles):
1. User Request (0s-0.1s): Gray bar
2. Orchestrator Dispatch (0.1s-0.3s): Blue bar
3. Parallel Execution (0.3s-5.0s):
   - Research Agent (green): 0.3s → 3.5s (3.2s duration)
   - News Agent (orange): 0.3s → 2.1s (1.8s duration)
   - Financial Agent (purple): 0.3s → 3.8s (3.5s duration)
   - Social Media Agent (cyan): 0.3s → 4.2s (3.9s duration)
4. Data Aggregation (5.0s-5.2s): Yellow bar
5. AI Synthesis (5.2s-7.5s): Gold bar, labeled "GPT-4 processing"
6. Response Generation (7.5s-8.0s): Green bar
7. Return to User (8.0s-8.1s): Gray bar

CRITICAL PATH: Highlight longest dependency chain (red outline)
BOTTLENECK: Mark slowest agent (Social Media - 3.9s)

ANNOTATIONS:
- Show "Parallel execution saves 10.5s vs sequential"
- Mark "Total: 8.1s vs 18.6s sequential"

STYLE: Gantt chart format, color-coded bars, time markers every second
```

---

## Prompt 8: Error Handling & Retry Logic Flowchart

```
Create a decision flowchart for agent error handling:

START: "Agent executes API call"

DECISION 1: "API responds?" (diamond)
- YES → "Status 200 OK?" 
- NO → "Timeout (5s)"

DECISION 2: "Status 200 OK?" (diamond)
- YES → "Parse response data"
- NO → "Check retry count"

DECISION 3: "Retry count < 3?" (diamond)
- YES → "Wait 1s" → "Retry API call" (loop back)
- NO → "Check cache"

DECISION 4: "Cache exists?" (diamond)
- YES → "Load cached data (orange path)" → "Mark as 'cached'"
- NO → "Generate partial insights"

DATA VALIDATION: "Valid data format?" (diamond)
- YES → "Return to orchestrator" (green)
- NO → "Use fallback template"

FALLBACK CHAIN (side branch):
1. Live API (100% fresh)
2. Cached data (85% confidence)
3. Partial data from other agents (70% confidence)
4. Template response (50% confidence)

END STATES (colored boxes):
- SUCCESS (green): "Fresh data returned"
- CACHED (orange): "Cached data returned"
- PARTIAL (yellow): "Partial insights"
- FAILED (red): "Agent skipped"

STYLE: Decision tree, diamonds for decisions, rectangles for actions, color-coded paths
```

---

## Prompt 9: Agent Communication Pattern (Pub-Sub Model)

```
Create a publish-subscribe communication diagram:

MESSAGE BROKER (center circle):
- "Event Bus / Message Queue"

PUBLISHERS (left side, sending arrows):
1. Orchestrator: Publishes "company.analyze" event
2. Each Agent: Publishes completion events
   - "research.complete"
   - "news.complete"
   - "financial.complete"
   - "socialmedia.complete"

SUBSCRIBERS (right side, receiving arrows):
1. All 4 Agents: Subscribe to "company.analyze"
2. Insight Synthesizer: Subscribes to all "*.complete" events
3. Cache Service: Subscribes to all events (for logging)
4. API Gateway: Subscribes to "synthesis.complete"

MESSAGE FLOW:
1. Orchestrator → Broker: "company.analyze" {company: "Infosys"}
2. Broker → Agents (fanout): Deliver to all 4 subscribers
3. Agents → Broker: Each publishes "agent.complete" when done
4. Broker → Synthesizer: Aggregates 4 completion events
5. Synthesizer → Broker: "synthesis.complete" with results
6. Broker → API: Deliver final response

BENEFITS ANNOTATION:
- "Decoupled agents"
- "Parallel execution"
- "Easy to add new agents"
- "Fault tolerant"

STYLE: Hub-and-spoke with central message broker, clear publish/subscribe arrows
```

---

## Prompt 10: Deployment Architecture (Production View)

```
Create a deployment/infrastructure diagram:

LAYERS (top to bottom):

1. CLIENT LAYER:
   - Browser icon
   - "React SPA" (port 5173 dev / 80 prod)

2. API LAYER:
   - "FastAPI Server" (port 8000)
   - "Load Balancer" (if scaled)

3. APPLICATION LAYER:
   - Container: "Agent Orchestrator"
   - 5 containers in parallel:
     - Research Agent service
     - News Agent service
     - Financial Agent service
     - Social Media Agent service
     - Insight Synthesizer service

4. DATA LAYER:
   - "Redis Cache" (in-memory)
   - "PostgreSQL DB" (persistent storage)

5. EXTERNAL LAYER:
   - API connections to external services
   - LLM API (OpenAI/Claude)

DEPLOYMENT INFO:
- Show: "Local: Windows PowerShell"
- Show: "Production: AWS/DigitalOcean (optional)"
- Port numbers on each service
- Environment variables indicators

SCALING NOTES:
- "Each agent can scale independently"
- "Stateless design enables horizontal scaling"

STYLE: Infrastructure diagram, server/container icons, network connections, clear layers
```

---

## Usage Instructions

### Recommended Tools:
1. **Figma/FigJam**: Use Prompts 1, 4, 6 for visual diagrams
2. **Miro AI**: Use Prompts 1, 7, 9 for collaborative workflows
3. **Lucidchart**: Use Prompts 2, 5, 8 for technical diagrams
4. **Whimsical**: Use Prompts 1, 3, 4 for quick sketches
5. **Mermaid.js**: Convert prompts to code for version control
6. **PlantUML**: Use Prompts 2, 5 for UML diagrams

### Quick Start:
1. Choose 2-3 prompts that best show your workflow (recommend 1, 2, and 7)
2. Paste into AI diagram tool
3. Refine with specific company names and metrics
4. Export as PNG/SVG for submission
5. Add to documentation with brief explanation

### Assessment Alignment:
- **Component 7 requires**: Either AI workflow OR wireframes (you have both)
- **Recommended submission**: 
  - Prompt 1: Shows overall architecture (required)
  - Prompt 7: Shows timing and parallel execution (impressive)
  - Prompt 8: Shows error handling (demonstrates robustness)

---

**Document Version**: 1.0  
**Created**: January 20, 2026  
**Purpose**: Component 7 - Demo/Prototype (10 Marks)  
**Submission**: AI Agent Workflow Diagrams
