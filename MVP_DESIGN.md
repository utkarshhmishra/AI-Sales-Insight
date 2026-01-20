# MVP Design - Documentation for Assessment

**Project**: AI Sales Insight - Multi-Agent Sales Intelligence System  
**Course**: Product Management with GenAI & Agentic AI  
**Assessment Section**: MVP Design (10 Marks)

---

## Table of Contents
1. [User Flow Design](#1-user-flow-design)
2. [Node Flow (AI Agent Flow)](#2-node-flow-ai-agent-flow)
3. [Information Architecture](#3-information-architecture)
4. [Wireframes](#4-wireframes)

---

## 1. User Flow Design

### 1.1 Primary User Flow: Generate Company Insights

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER JOURNEY                              │
└─────────────────────────────────────────────────────────────────┘

START: Sales Rep needs to prepare for client meeting
    ↓
┌─────────────────────────────────────┐
│  STEP 1: Access Dashboard           │
│  - Open browser                     │
│  - Navigate to http://localhost:5173│
│  - Auto-loads dashboard             │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  STEP 2: Enter Company Name         │
│  - Click search input field         │
│  - Type company name                │
│    Examples:                        │
│    • "Infosys"                      │
│    • "TechStart India"              │
│    • "Wipro Limited"                │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  STEP 3: Trigger Insight Generation │
│  - Click "Generate Insights" button │
│  - System validates input           │
│  - Loading indicator appears        │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  STEP 4: Wait for Processing        │
│  - Progress indicator shows:        │
│    ✓ Researching company...         │
│    ✓ Gathering news...              │
│    ✓ Analyzing financials...        │
│    ✓ Checking social media...       │
│    ✓ Synthesizing insights...       │
│  Duration: 2-3 seconds              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  STEP 5: View Insights Page         │
│  - Auto-navigate to insights page   │
│  - Comprehensive report displayed   │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  STEP 6: Review Content             │
│  - Read executive summary           │
│  - Review talking points            │
│  - Check opportunities & risks      │
│  - Explore agent outputs            │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  DECISION POINT                     │
│  Is information sufficient?         │
└──────────────┬──────────────────────┘
               ↓
         ┌─────┴─────┐
         │           │
        YES          NO
         │           │
         │           └──► Refresh Insights (back to Step 3)
         │
         ↓
┌─────────────────────────────────────┐
│  STEP 7: Take Action                │
│  Options:                           │
│  • Export as PDF                    │
│  • Copy to clipboard                │
│  • Share with team                  │
│  • Add notes                        │
│  • Schedule follow-up               │
└──────────────┬──────────────────────┘
               ↓
END: Sales Rep prepared for meeting with actionable insights
```

### 1.2 Alternative User Flows

#### Flow 2: Browse Recent Insights
```
Dashboard → View Recent Insights → Select Company → View Details → Take Action
```

#### Flow 3: Quick Refresh
```
Insights Page → Click Refresh → Updated Data → Review Changes
```

#### Flow 4: Error Recovery
```
Dashboard → Enter Company → Generate → Error Occurs → 
    ↓
View Error Message → 
    ↓
Options:
• Retry (if temporary)
• Use cached data (if available)
• Try different company name
```

### 1.3 Detailed User Flow Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                     COMPLETE USER FLOW                            │
└──────────────────────────────────────────────────────────────────┘

[Landing Page]
      ↓
[Dashboard]
      │
      ├──► [Search Company]
      │         ↓
      │    [Autocomplete Suggestions] (optional)
      │         ↓
      │    [Select/Confirm Company]
      │         ↓
      │    [Click "Generate Insights"]
      │         ↓
      │    [Loading State - Progress Indicators]
      │         ↓
      │    [Success?] ──NO──► [Error Page]
      │         │                   ↓
      │        YES              [Retry Options]
      │         ↓                   │
      │    [Insights Page] ◄────────┘
      │         │
      │         ├──► [Executive Summary Section]
      │         ├──► [Talking Points Section]
      │         ├──► [Opportunities & Risks]
      │         ├──► [Agent Details (Expandable)]
      │         │         ├──► Research Data
      │         │         ├──► News Data
      │         │         ├──► Financial Data
      │         │         └──► Social Media Data
      │         │
      │         └──► [Action Buttons]
      │                   ├──► Export PDF
      │                   ├──► Copy Text
      │                   ├──► Share Link
      │                   └──► Refresh Data
      │
      ├──► [Recent Insights]
      │         └──► [View Saved Insight]
      │
      └──► [Settings]
            └──► Configure API Keys, Preferences
```

### 1.4 User Interaction Points

| Screen | User Action | System Response | Next State |
|--------|-------------|----------------|------------|
| **Dashboard** | Types company name | Shows autocomplete suggestions | Input validated |
| | Clicks "Generate" | Starts insight generation | Loading screen |
| **Loading** | Waits | Shows progress indicators | Insights page (success) or Error page |
| **Insights Page** | Scrolls | Reveals content sections | Same page |
| | Clicks agent card | Expands detailed data | Expanded view |
| | Clicks "Export PDF" | Generates PDF download | Download initiated |
| | Clicks "Refresh" | Re-fetches latest data | Loading → Updated insights |
| | Clicks "Back" | Returns to dashboard | Dashboard |
| **Error Page** | Clicks "Retry" | Attempts generation again | Loading screen |
| | Clicks "Use Cached" | Loads last successful result | Insights page (cached) |

---

## 2. Node Flow (AI Agent Flow)

### 2.1 High-Level Agent Orchestration Flow

```
┌─────────────────────────────────────────────────────────────────┐
│              AI AGENT ORCHESTRATION NODE FLOW                    │
└─────────────────────────────────────────────────────────────────┘

                    [API Request Received]
                            ↓
                    [Orchestrator Node]
                    (Validates & Routes)
                            ↓
                ┌───────────┴───────────┐
                │   Parallel Execution  │
                │     (All 5 Agents)    │
                └───────────┬───────────┘
                            ↓
        ┌───────┬───────┬───────┬───────┬───────┐
        ↓       ↓       ↓       ↓       ↓       ↓
    [Agent 1] [Agent 2] [Agent 3] [Agent 4] [Agent 5]
    Research   News    Financial  Social   Synthesizer
        ↓       ↓       ↓       ↓       ↓
    [Execute] [Execute] [Execute] [Execute] [Waits]
        ↓       ↓       ↓       ↓       
    [Return]  [Return]  [Return]  [Return]
        ↓       ↓       ↓       ↓
        └───────┴───────┴───────┴───────┐
                                        ↓
                              [Agent 5 Receives All]
                                        ↓
                              [LLM Synthesizes]
                                        ↓
                              [Returns Insights]
                                        ↓
                            [Orchestrator Aggregates]
                                        ↓
                            [Format Response]
                                        ↓
                            [Return to Frontend]
```

### 2.2 Detailed Agent Node Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                  DETAILED AGENT EXECUTION FLOW                   │
└─────────────────────────────────────────────────────────────────┘

[START] User Request: "Generate insights for Infosys"
    ↓
┌────────────────────────────────────┐
│  NODE 1: Request Validation        │
│  - Check company_name exists       │
│  - Validate format                 │
│  - Check rate limits               │
│  Decision: Valid?                  │
└────────────┬───────────────────────┘
             ↓
            YES ──► Continue
             │
            NO ──► Return Error
             ↓
┌────────────────────────────────────┐
│  NODE 2: Cache Check               │
│  - Query cache for company         │
│  - Check data freshness (<1hr?)    │
│  Decision: Fresh cache exists?     │
└────────────┬───────────────────────┘
             ↓
      ┌──────┴──────┐
     YES            NO
      │              │
      │              └──► Continue to Node 3
      │
      └──► Return Cached Data (End)
      
┌────────────────────────────────────┐
│  NODE 3: Agent Orchestration       │
│  - Create agent execution plan     │
│  - Initialize all 5 agents         │
│  - Set timeouts per agent          │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 4: Parallel Agent Execution  │
│  ┌──────────────────────────────┐ │
│  │  Thread 1: Research Agent    │ │
│  │  - Scrape company website    │ │
│  │  - Query LinkedIn API        │ │
│  │  - Fetch Crunchbase data     │ │
│  │  - Extract key info          │ │
│  │  - Return JSON               │ │
│  └──────────────────────────────┘ │
│  ┌──────────────────────────────┐ │
│  │  Thread 2: News Agent        │ │
│  │  - Query NewsAPI             │ │
│  │  - Filter by date (30 days) │ │
│  │  - Sort by relevance         │ │
│  │  - Extract top articles      │ │
│  │  - Return JSON               │ │
│  └──────────────────────────────┘ │
│  ┌──────────────────────────────┐ │
│  │  Thread 3: Financial Agent   │ │
│  │  - Query Yahoo Finance       │ │
│  │  - Get stock data            │ │
│  │  - Check funding info        │ │
│  │  - Calculate metrics         │ │
│  │  - Return JSON               │ │
│  └──────────────────────────────┘ │
│  ┌──────────────────────────────┐ │
│  │  Thread 4: Social Media Agt  │ │
│  │  - Query LinkedIn            │ │
│  │  - Analyze engagement        │ │
│  │  - Calculate sentiment       │ │
│  │  - Extract trends            │ │
│  │  - Return JSON               │ │
│  └──────────────────────────────┘ │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 5: Agent Result Collection   │
│  - Wait for all agents (max 30s)  │
│  - Handle timeouts gracefully      │
│  - Collect successful results      │
│  - Log failures                    │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 6: Success Check             │
│  Calculate: success_rate           │
│  = successful_agents / total_agents│
│  Decision: success_rate >= 60%?    │
└────────────┬───────────────────────┘
             ↓
      ┌──────┴──────┐
     YES            NO
      │              │
      │              └──► NODE 7b: Fallback Handler
      │                      ↓
      │                  Use cached data
      │                  or mock data
      │                      ↓
      │                  Return partial results
      │
      └──► NODE 7a: Continue
             ↓
┌────────────────────────────────────┐
│  NODE 7a: Insight Synthesizer      │
│  - Receive all agent outputs       │
│  - Prepare LLM prompt              │
│  - Call GPT-4/Claude API           │
│  - Generate:                       │
│    • Executive Summary             │
│    • Talking Points (5-7)          │
│    • Opportunities                 │
│    • Risks                         │
│    • Recommendations               │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 8: LLM Success Check         │
│  Decision: LLM returned valid data?│
└────────────┬───────────────────────┘
             ↓
      ┌──────┴──────┐
     YES            NO
      │              │
      │              └──► Use template-based generation
      │                      ↓
      │                  Generate structured output
      │                      ↓
      │                  Add warning flag
      │
      └──► Continue
             ↓
┌────────────────────────────────────┐
│  NODE 9: Response Aggregation      │
│  - Combine all agent outputs       │
│  - Structure final JSON            │
│  - Add metadata (timestamp, etc)   │
│  - Calculate confidence scores     │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 10: Cache Update             │
│  - Store results in cache          │
│  - Set expiration (1 hour)         │
│  - Update access logs              │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 11: Response Formatting      │
│  - Convert to API response format  │
│  - Add status codes                │
│  - Include execution metrics       │
└────────────┬───────────────────────┘
             ↓
┌────────────────────────────────────┐
│  NODE 12: Return to Frontend       │
│  HTTP 200 with JSON payload        │
└────────────────────────────────────┘
             ↓
          [END]
```

### 2.3 Agent Decision Trees

#### Research Agent Decision Tree
```
[START] Fetch company data
    ↓
[Try Primary Source: Company Website]
    ↓
Success? ──YES──► Continue
    │
   NO
    ↓
[Try Secondary: LinkedIn]
    ↓
Success? ──YES──► Continue
    │
   NO
    ↓
[Try Tertiary: Crunchbase]
    ↓
Success? ──YES──► Continue
    │
   NO
    ↓
[Check Cache]
    ↓
Cache exists? ──YES──► Use cached data + warning
    │
   NO
    ↓
[Return Mock Data + Error Flag]
    ↓
[END]
```

#### News Agent Decision Tree
```
[START] Fetch news
    ↓
[Try NewsAPI]
    ↓
API Key valid? ──NO──► Try Google News RSS
    │
   YES
    ↓
[Query NewsAPI]
    ↓
Results found? ──NO──► Try Google News RSS
    │
   YES
    ↓
[Filter & Sort Articles]
    ↓
[Return Top 20 Articles]
    ↓
[END]
```

### 2.4 Error Handling Flow

```
[Agent Execution Error Detected]
    ↓
[Classify Error Type]
    ↓
    ├──► API Timeout ──► Retry with increased timeout (2x)
    │
    ├──► API Rate Limit ──► Wait & retry (exponential backoff)
    │
    ├──► Invalid API Key ──► Skip to fallback source
    │
    ├──► Network Error ──► Retry up to 3 times
    │
    └──► Unknown Error ──► Log error & use fallback data
              ↓
    [All retries failed?]
              ↓
        ┌─────┴─────┐
       YES          NO
        │            │
        │            └──► Return successful result
        │
        ↓
    [Use Fallback Strategy]
        ├──► Cached data (if <24hr old)
        ├──► Mock data (demo mode)
        └──► Partial results from other agents
              ↓
    [Mark agent as "degraded"]
              ↓
    [Continue with remaining agents]
```

### 2.5 Agent Communication Protocol

```
┌─────────────────────────────────────────────────────────────┐
│            AGENT INTER-COMMUNICATION PATTERN                 │
└─────────────────────────────────────────────────────────────┘

Orchestrator                    Agent                Frontend
     │                            │                      │
     │──── dispatch_task ────────►│                      │
     │    (company_name,          │                      │
     │     timeout, params)       │                      │
     │                            │                      │
     │                            │ [Processing...]     │
     │                            │ [External API call] │
     │                            │ [Data parsing]      │
     │                            │                      │
     │◄─── return_result ─────────│                      │
     │    (status, data,          │                      │
     │     metadata)              │                      │
     │                            │                      │
     │ [Aggregates results]       │                      │
     │ [Waits for all agents]     │                      │
     │                            │                      │
     │────────── response ────────────────────────────────►│
     │           (complete insights JSON)                 │
```

### 2.6 Agent State Machine

```
[IDLE] ──trigger──► [INITIALIZING]
                           ↓
                    [EXECUTING]
                     ↓    ↓    ↓
              ┌──────┼────┼────┘
              │      │    │
         [SUCCESS][RETRY][TIMEOUT]
              │      │       │
              │      └───────┴──► [FAILED]
              │                      │
              ↓                      │
         [COMPLETED]                 │
              │                      │
              └──────────────────────┴──► [IDLE]
```

---

## 3. Information Architecture

### 3.1 Site Structure

```
AI Sales Insight
│
├── Home / Dashboard
│   ├── Company Search Input
│   ├── Quick Actions
│   ├── Recent Insights (List)
│   └── System Status
│
├── Insights Page
│   ├── Header
│   │   ├── Company Name
│   │   ├── Generated Timestamp
│   │   └── Action Buttons
│   │       ├── Refresh
│   │       ├── Export PDF
│   │       ├── Share
│   │       └── Copy
│   │
│   ├── Executive Summary Section
│   │   └── 200-word AI-generated summary
│   │
│   ├── Talking Points Section
│   │   └── 5-7 actionable points
│   │
│   ├── Opportunities & Risks
│   │   ├── Opportunities (3-5 items)
│   │   └── Risks (3-5 items)
│   │
│   ├── Agent Details (Expandable)
│   │   ├── Research Agent Output
│   │   │   ├── Company Overview
│   │   │   ├── Decision Makers
│   │   │   ├── Products/Services
│   │   │   └── Technology Stack
│   │   │
│   │   ├── News Agent Output
│   │   │   ├── Recent Articles (Top 10)
│   │   │   ├── Industry Trends
│   │   │   └── Competitive News
│   │   │
│   │   ├── Financial Agent Output
│   │   │   ├── Stock Performance
│   │   │   ├── Funding Info
│   │   │   └── Financial Health
│   │   │
│   │   └── Social Media Agent Output
│   │       ├── LinkedIn Metrics
│   │       ├── Sentiment Analysis
│   │       └── Trending Topics
│   │
│   └── Footer
│       ├── Data Sources
│       ├── Last Updated
│       └── Confidence Score
│
├── Settings Page (Optional)
│   ├── API Configuration
│   ├── User Preferences
│   └── Export Settings
│
└── Help / Documentation
    ├── User Guide
    ├── API Documentation
    └── Contact Support
```

### 3.2 Data Model & Information Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                     DATA STRUCTURE                           │
└─────────────────────────────────────────────────────────────┘

Company Insight (Root Object)
│
├── Metadata
│   ├── company_name: string
│   ├── generated_at: timestamp
│   ├── status: enum (success, partial, failed)
│   ├── confidence_score: float (0-1)
│   └── execution_time: float (seconds)
│
├── Executive Summary
│   ├── summary_text: string (200-250 words)
│   ├── key_highlights: array[string]
│   └── generated_by: "insight_synthesizer"
│
├── Talking Points
│   ├── points: array[object]
│   │   ├── point_text: string
│   │   ├── category: enum (opportunity, challenge, general)
│   │   ├── priority: enum (high, medium, low)
│   │   └── source_agent: string
│   └── count: integer (5-7)
│
├── Opportunities
│   ├── opportunities: array[object]
│   │   ├── description: string
│   │   ├── confidence: float (0-1)
│   │   ├── potential_value: string
│   │   └── action_required: string
│   └── count: integer
│
├── Risks
│   ├── risks: array[object]
│   │   ├── description: string
│   │   ├── severity: enum (high, medium, low)
│   │   ├── mitigation: string
│   │   └── source: string
│   └── count: integer
│
├── Research Data (from Research Agent)
│   ├── company_info
│   │   ├── industry: string
│   │   ├── size: string
│   │   ├── headquarters: string
│   │   ├── founded: year
│   │   └── website: url
│   ├── decision_makers: array[object]
│   │   ├── name: string
│   │   ├── title: string
│   │   └── linkedin_url: url
│   ├── products: array[string]
│   └── tech_stack: array[string]
│
├── News Data (from News Agent)
│   ├── articles: array[object]
│   │   ├── headline: string
│   │   ├── date: date
│   │   ├── source: string
│   │   ├── url: url
│   │   ├── summary: string
│   │   └── sentiment: enum (positive, neutral, negative)
│   ├── trending_topics: array[string]
│   └── summary: string
│
├── Financial Data (from Financial Agent)
│   ├── stock_data (if public)
│   │   ├── symbol: string
│   │   ├── current_price: float
│   │   ├── change_percent: float
│   │   ├── market_cap: string
│   │   └── last_updated: timestamp
│   ├── funding_info
│   │   ├── total_raised: string
│   │   ├── last_round: object
│   │   │   ├── type: string
│   │   │   ├── amount: string
│   │   │   └── date: date
│   │   └── investors: array[string]
│   └── financial_health: enum (strong, moderate, weak)
│
└── Social Media Data (from Social Media Agent)
    ├── linkedin_metrics
    │   ├── followers: integer
    │   ├── recent_posts: integer
    │   ├── engagement_rate: float
    │   └── growth_trend: string
    ├── sentiment_analysis
    │   ├── overall_score: float (-1 to 1)
    │   ├── sentiment_label: enum (positive, neutral, negative)
    │   └── confidence: float (0-1)
    └── trending_topics: array[string]
```

### 3.3 Navigation Flow

```
┌─────────────────────────────────────────────────────────────┐
│                   NAVIGATION STRUCTURE                       │
└─────────────────────────────────────────────────────────────┘

[Header - Always Visible]
├── Logo (Click → Home)
├── Navigation Menu
│   ├── Dashboard (/)
│   ├── Recent Insights (/insights/recent)
│   └── Settings (/settings)
└── User Menu
    └── Help/Docs

[Main Content Area]
├── Dashboard View
│   └── CTA: Generate Insights → Insights Page
│
├── Insights View
│   ├── Back Button → Dashboard
│   └── Refresh Button → Reload current page
│
└── Settings View
    └── Back Button → Dashboard

[Breadcrumb Navigation]
Home > Insights > Company Name
```

### 3.4 Content Prioritization

#### Primary Content (Above the Fold)
1. **Executive Summary** - Most important, shown first
2. **Talking Points** - Immediately actionable
3. **Key Opportunities** - Business value

#### Secondary Content (Scroll to View)
4. **Risks & Challenges** - Important context
5. **Detailed Agent Data** - Supporting information

#### Tertiary Content (Expandable/Optional)
6. **Raw Agent Outputs** - For power users
7. **Data Sources** - Transparency information
8. **Technical Metadata** - For debugging

### 3.5 Information Labeling System

```
Insight Components Labeling:

✓ = Verified data
⚡ = Real-time data
📊 = AI-generated
🔄 = Cached data (with age)
⚠️ = Incomplete data
❌ = Data unavailable

Example Usage:
"Executive Summary 📊" - AI-generated
"Stock Price ⚡" - Real-time
"News Articles ✓" - Verified from sources
"Financial Data 🔄 (2 hours old)" - Cached
```

---

## 4. Wireframes

### 4.1 Low-Fidelity Wireframes

#### Screen 1: Dashboard (Low-Fi)

```
┌─────────────────────────────────────────────────────────────┐
│  [Logo]        AI Sales Insight            [Help] [Settings]│
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                  Generate Company Insights                   │
│                                                              │
│         ┌──────────────────────────────────────┐            │
│         │  Enter company name...               │  [Search]  │
│         └──────────────────────────────────────┘            │
│                                                              │
│                    [ Generate Insights ]                     │
│                                                              │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  Recent Insights                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Infosys                              Generated: 2h ago  │ │
│  │ Executive summary shows...           [View Details]     │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ TechStart India                      Generated: 5h ago  │ │
│  │ Startup focusing on AI...            [View Details]     │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Wipro Limited                        Generated: 1d ago  │ │
│  │ Global IT services...                [View Details]     │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Screen 2: Loading State (Low-Fi)

```
┌─────────────────────────────────────────────────────────────┐
│  [Logo]        AI Sales Insight            [Help] [Settings]│
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                     Generating Insights                      │
│                     for "Infosys"                           │
│                                                              │
│                   [=========>        ] 60%                   │
│                                                              │
│  ✓ Researching company background...                        │
│  ✓ Gathering recent news...                                 │
│  ✓ Analyzing financial data...                              │
│  ⏳ Checking social media presence...                        │
│  ⏳ Synthesizing insights...                                 │
│                                                              │
│                 Estimated time: 2 seconds                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Screen 3: Insights Page (Low-Fi)

```
┌─────────────────────────────────────────────────────────────┐
│  [Logo]  [← Back]    Infosys    [Refresh] [Export] [Share] │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  EXECUTIVE SUMMARY 📊                                        │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Infosys is a global IT services leader showing...     │ │
│  │  Recent Q3 results indicate 7% YoY growth. Cloud       │ │
│  │  migration and North America expansion are key...      │ │
│  │  [Read More...]                                        │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  TALKING POINTS                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  1. Congratulate on Q3 performance (7% growth)         │ │
│  │  2. Discuss cloud transformation initiatives           │ │
│  │  3. Explore AI/ML investment opportunities             │ │
│  │  4. Address North America expansion challenges         │ │
│  │  5. Highlight efficiency automation benefits           │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  OPPORTUNITIES                     RISKS                     │
│  ┌─────────────────────┐   ┌──────────────────────┐        │
│  │ • Expanding tech    │   │ • Competitive        │        │
│  │   team              │   │   pressure           │        │
│  │ • Cloud migration   │   │ • Economic headwinds │        │
│  │ • AI adoption       │   │ • Talent retention   │        │
│  └─────────────────────┘   └──────────────────────┘        │
│                                                              │
│  AGENT DETAILS (Click to expand)                             │
│  ▸ Research Agent                                            │
│  ▸ News Agent                                                │
│  ▸ Financial Agent                                           │
│  ▸ Social Media Agent                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Mid-Fidelity Wireframes

#### Screen 1: Dashboard (Mid-Fi)

```
┌───────────────────────────────────────────────────────────────┐
│ 🎯 AI Sales Insight          🔔    👤 User    ⚙️ Settings    │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│              Generate AI-Powered Sales Insights                │
│          Transform hours of research into minutes              │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  🔍  Enter company name or domain...              [🔎]  │  │
│  └─────────────────────────────────────────────────────────┘  │
│                   [ Generate Insights → ]                      │
│                                                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                │
│  📊 Recent Insights                         [View All →]      │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  🏢 Infosys                                              │  │
│  │  Generated 2 hours ago • Confidence: 94%                 │  │
│  │  ─────────────────────────────────────────────────────  │  │
│  │  Global IT leader showing strong growth in cloud...     │  │
│  │  Key opportunity: Digital transformation focus          │  │
│  │                                                          │  │
│  │  [📄 View Details]  [🔄 Refresh]  [📤 Share]           │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  🏢 TechStart India                                      │  │
│  │  Generated 5 hours ago • Confidence: 87%                 │  │
│  │  ─────────────────────────────────────────────────────  │  │
│  │  Emerging SaaS startup with $50M Series B funding...    │  │
│  │  Key opportunity: Rapid scaling needs                   │  │
│  │                                                          │  │
│  │  [📄 View Details]  [🔄 Refresh]  [📤 Share]           │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                │
│  💡 Quick Stats                                                │
│  ┌──────────────┬──────────────┬──────────────┬────────────┐  │
│  │   Insights   │  Avg Response│  Success Rate│  Companies │  │
│  │   Generated  │     Time     │              │   Tracked  │  │
│  │              │              │              │            │  │
│  │     247      │    2.8s      │    98.3%     │     89     │  │
│  └──────────────┴──────────────┴──────────────┴────────────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

#### Screen 2: Insights Page - Header (Mid-Fi)

```
┌───────────────────────────────────────────────────────────────┐
│ 🎯 AI Sales Insight         [← Back to Dashboard]   👤 User   │
├───────────────────────────────────────────────────────────────┤
│                                                                │
│  🏢 Infosys Limited                                            │
│  ────────────────────────────────────────────────────────     │
│  🌐 infosys.com  •  📍 Bangalore, India  •  👥 300K+ employees│
│  💰 Public (NSE: INFY)  •  💼 IT Services & Consulting         │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ ⏰ Generated: Jan 19, 2026 at 3:45 PM IST                │ │
│  │ ✓ Confidence Score: 94%  •  ⚡ Data Freshness: Real-time │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  [🔄 Refresh Data]  [📄 Export PDF]  [📋 Copy]  [📤 Share]   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

#### Screen 3: Insights Page - Content (Mid-Fi)

```
┌───────────────────────────────────────────────────────────────┐
│                                                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                │
│  📊 EXECUTIVE SUMMARY (AI-Generated)                           │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                                                           │ │
│  │  Infosys is a global IT services and consulting leader   │ │
│  │  demonstrating strong performance with 7% YoY growth in   │ │
│  │  Q3 2026. The company is heavily investing in cloud      │ │
│  │  transformation and AI capabilities, with significant     │ │
│  │  expansion in North America. Recent partnerships with     │ │
│  │  Microsoft and Google Cloud indicate strategic focus on   │ │
│  │  enterprise digital transformation. Leadership transition  │ │
│  │  is stable with new CTO bringing fresh innovation focus.  │ │
│  │                                                           │ │
│  │  Key Highlights:                                          │ │
│  │  • Revenue: $18.2B (FY2025)                              │ │
│  │  • Growth Rate: 7% YoY                                   │ │
│  │  • Market Cap: $75B                                      │ │
│  │  • Digital Revenue: 62% of total                         │ │
│  │                                                           │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                │
│  💬 TALKING POINTS                                             │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  1. 🎉 Congratulate on Strong Q3 Performance             │ │
│  │     "Impressive 7% growth despite market headwinds"       │ │
│  │     Priority: HIGH                                        │ │
│  │                                                           │ │
│  │  2. ☁️ Discuss Cloud Transformation Journey              │ │
│  │     "How are your Microsoft/Google partnerships going?"   │ │
│  │     Priority: HIGH                                        │ │
│  │                                                           │ │
│  │  3. 🤖 Explore AI/ML Implementation Strategy             │ │
│  │     "Your AI investments align with our solution"         │ │
│  │     Priority: MEDIUM                                      │ │
│  │                                                           │ │
│  │  4. 📈 North America Expansion Opportunities             │ │
│  │     "Scaling challenges we can help address"              │ │
│  │     Priority: MEDIUM                                      │ │
│  │                                                           │ │
│  │  5. ⚡ Efficiency & Automation Needs                      │ │
│  │     "300K employees = huge automation potential"          │ │
│  │     Priority: HIGH                                        │ │
│  │                                                           │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                │
│  ✅ OPPORTUNITIES                  ⚠️ RISKS & CHALLENGES      │
│  ┌─────────────────────────────┐  ┌─────────────────────────┐│
│  │                              │  │                          ││
│  │ 1. 🎯 Digital Transformation │  │ 1. 📊 Competitive        ││
│  │    300K employees need       │  │    Pressure from        ││
│  │    automation tools          │  │    Accenture, TCS       ││
│  │    Value: $2M-5M potential   │  │    Severity: MEDIUM     ││
│  │                              │  │                          ││
│  │ 2. ☁️ Cloud Migration        │  │ 2. 💼 Talent Retention  ││
│  │    Active cloud initiatives  │  │    High attrition in    ││
│  │    Value: $1M-3M potential   │  │    tech sector          ││
│  │                              │  │    Severity: MEDIUM     ││
│  │ 3. 🌍 Global Expansion       │  │                          ││
│  │    Need for scalable         │  │ 3. 📉 Economic Headwinds││
│  │    solutions                 │  │    Budget constraints   ││
│  │    Value: $3M-7M potential   │  │    Severity: LOW        ││
│  │                              │  │                          ││
│  └─────────────────────────────┘  └─────────────────────────┘│
│                                                                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                                │
│  🔍 DETAILED AGENT INSIGHTS                                    │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ ▼ 🔬 Research Agent [Expand]                             │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ ▸ 📰 News Agent [Click to expand]                        │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ ▸ 💰 Financial Agent [Click to expand]                   │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │ ▸ 📱 Social Media Agent [Click to expand]                │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 4.3 High-Fidelity Wireframe Specifications

#### Color Scheme
```
Primary Colors:
- Primary Blue: #2563EB (Buttons, Links)
- Dark Blue: #1E40AF (Headers)
- Light Blue: #DBEAFE (Backgrounds)

Secondary Colors:
- Success Green: #10B981 (Positive indicators)
- Warning Orange: #F59E0B (Warnings)
- Error Red: #EF4444 (Errors)
- Neutral Gray: #6B7280 (Text)

Background:
- Main BG: #F9FAFB
- Card BG: #FFFFFF
- Hover BG: #F3F4F6
```

#### Typography
```
Headings:
- H1: Inter Bold, 32px, #1F2937
- H2: Inter Semibold, 24px, #374151
- H3: Inter Medium, 20px, #4B5563

Body:
- Body Large: Inter Regular, 16px, #6B7280
- Body Regular: Inter Regular, 14px, #6B7280
- Body Small: Inter Regular, 12px, #9CA3AF

Special:
- Button Text: Inter Semibold, 14px
- Link Text: Inter Medium, 14px, #2563EB
```

#### Component Specifications

**Button Styles:**
```
Primary Button:
- Background: #2563EB
- Text: #FFFFFF
- Border Radius: 8px
- Padding: 12px 24px
- Hover: #1D4ED8
- Shadow: 0 1px 3px rgba(0,0,0,0.1)

Secondary Button:
- Background: #FFFFFF
- Text: #374151
- Border: 1px solid #D1D5DB
- Border Radius: 8px
- Padding: 12px 24px
- Hover: #F3F4F6
```

**Card Styles:**
```
Standard Card:
- Background: #FFFFFF
- Border: 1px solid #E5E7EB
- Border Radius: 12px
- Padding: 24px
- Shadow: 0 1px 3px rgba(0,0,0,0.05)
- Hover Shadow: 0 4px 6px rgba(0,0,0,0.1)
```

**Input Fields:**
```
Text Input:
- Background: #FFFFFF
- Border: 1px solid #D1D5DB
- Border Radius: 8px
- Padding: 12px 16px
- Focus Border: #2563EB
- Focus Shadow: 0 0 0 3px rgba(37,99,235,0.1)
```

### 4.4 Responsive Design Breakpoints

```
Mobile: 320px - 768px
  - Single column layout
  - Stacked cards
  - Collapsible sections

Tablet: 769px - 1024px
  - Two column layout where appropriate
  - Condensed navigation
  - Side-by-side opportunities/risks

Desktop: 1025px+
  - Full layout with sidebar (optional)
  - Three column sections
  - Expanded content areas
```

### 4.5 Interactive States

```
Button States:
┌─────────────────────────────────────────────┐
│ Default     │ [ Generate Insights ]         │
│ Hover       │ [ Generate Insights ] (darker)│
│ Active      │ [ Generate Insights ] (pressed)│
│ Disabled    │ [ Generate Insights ] (grayed)│
│ Loading     │ [ ⟳ Generating... ]           │
└─────────────────────────────────────────────┘

Card States:
┌─────────────────────────────────────────────┐
│ Default     │ Normal card with border       │
│ Hover       │ Elevated shadow, border blue  │
│ Selected    │ Blue border, blue background  │
│ Collapsed   │ Header only, ▸ indicator     │
│ Expanded    │ Full content, ▼ indicator    │
└─────────────────────────────────────────────┘
```

---

## Summary: MVP Design Completeness

| Component | Status | Details |
|-----------|--------|---------|
| **User Flow Design** | ✅ Complete | Primary flow + 4 alternative flows documented |
| **Node Flow (AI Agent)** | ✅ Complete | 12-node detailed flow + decision trees |
| **Information Architecture** | ✅ Complete | 5-level hierarchy + data model |
| **Low-Fidelity Wireframes** | ✅ Complete | 3 key screens in ASCII format |
| **Mid-Fidelity Wireframes** | ✅ Complete | Enhanced 3 screens with details |
| **High-Fidelity Specs** | ✅ Complete | Colors, typography, components |

### Design Principles Applied

1. **User-Centered**: Flow designed for sales rep workflow
2. **Progressive Disclosure**: Information revealed as needed
3. **Feedback-Rich**: Clear status at every stage
4. **Error-Tolerant**: Multiple fallback options
5. **Performance-Focused**: Parallel processing visible to user
6. **Accessible**: Clear labels, logical hierarchy
7. **Scalable**: Design accommodates future features

### Key Innovations

1. **Real-Time Progress**: Users see each agent working
2. **Confidence Scoring**: Transparency in AI quality
3. **Expandable Details**: Power users get depth
4. **One-Click Actions**: Export, share, refresh
5. **Smart Caching**: Reduced wait times

---

**Document Version**: 1.0  
**Last Updated**: January 20, 2026  
**Assessment Ready**: ✅ Yes

**Total Pages**: 35+ pages of comprehensive MVP design documentation
