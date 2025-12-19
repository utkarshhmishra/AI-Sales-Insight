"""
Health Check Endpoints
"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/")
async def health_check():
    """Basic health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "AI Sales Insight API"
    }


@router.get("/detailed")
async def detailed_health():
    """Detailed health check with system status"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "AI Sales Insight API",
        "version": "1.0.0",
        "components": {
            "api": "operational",
            "agents": "operational",
            "database": "not_configured",
            "cache": "not_configured",
            "llm": "not_configured"
        },
        "uptime": "N/A"
    }
