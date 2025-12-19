"""
Insights API Endpoints
Main endpoint for generating company insights
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
import logging

from agents.orchestrator import AgentOrchestrator

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize orchestrator
orchestrator = AgentOrchestrator()


class InsightRequest(BaseModel):
    """Request model for generating insights"""
    company_name: str = Field(..., description="Name of the target company", min_length=2, max_length=200)
    timeframe_days: int = Field(default=30, description="Data collection timeframe in days", ge=1, le=90)
    priority: str = Field(default="medium", description="Priority level", pattern="^(low|medium|high)$")
    context: Optional[Dict[str, Any]] = Field(default=None, description="Additional context")


class QuickBriefRequest(BaseModel):
    """Request model for quick brief"""
    company_name: str = Field(..., description="Name of the target company", min_length=2, max_length=200)


@router.post("/generate")
async def generate_insights(request: InsightRequest):
    """
    Generate comprehensive insights for a company
    
    This endpoint orchestrates multiple AI agents to gather:
    - Company research and background
    - Recent news and announcements
    - Financial data and metrics
    - Social media presence and sentiment
    - Synthesized actionable insights
    
    **Example Request:**
    ```json
    {
        "company_name": "Acme Corp",
        "timeframe_days": 30,
        "priority": "high"
    }
    ```
    """
    try:
        logger.info(f"Generating insights for {request.company_name}")
        
        result = await orchestrator.gather_insights(
            company_name=request.company_name,
            context=request.context or {},
            timeframe_days=request.timeframe_days,
            priority=request.priority
        )
        
        if result.get("status") == "error":
            raise HTTPException(status_code=500, detail=result.get("error", "Unknown error"))
        
        return {
            "success": True,
            "data": result,
            "message": f"Successfully generated insights for {request.company_name}"
        }
        
    except Exception as e:
        logger.error(f"Error generating insights: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/quick-brief")
async def generate_quick_brief(request: QuickBriefRequest):
    """
    Generate a quick brief (faster, less comprehensive)
    
    Returns essential company information and recent news only.
    Useful for quick pre-call preparation.
    
    **Example Request:**
    ```json
    {
        "company_name": "Acme Corp"
    }
    ```
    """
    try:
        logger.info(f"Generating quick brief for {request.company_name}")
        
        result = await orchestrator.quick_brief(company_name=request.company_name)
        
        if result.get("status") == "error":
            raise HTTPException(status_code=500, detail=result.get("error", "Unknown error"))
        
        return {
            "success": True,
            "data": result,
            "message": f"Successfully generated quick brief for {request.company_name}"
        }
        
    except Exception as e:
        logger.error(f"Error generating quick brief: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{company_name}")
async def get_insight_history(company_name: str, limit: int = 10):
    """
    Get historical insights for a company
    
    Returns previously generated insights to avoid redundant API calls
    """
    # TODO: Implement database storage and retrieval
    return {
        "success": True,
        "data": {
            "company_name": company_name,
            "history": [],
            "message": "History feature coming soon - requires database implementation"
        }
    }


@router.delete("/cache/{company_name}")
async def clear_cache(company_name: str):
    """
    Clear cached insights for a company
    
    Forces fresh data collection on next request
    """
    # TODO: Implement cache clearing
    return {
        "success": True,
        "message": f"Cache cleared for {company_name} (when caching is implemented)"
    }
