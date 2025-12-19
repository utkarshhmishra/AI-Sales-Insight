"""
API v1 Router
"""

from fastapi import APIRouter

from .endpoints import insights, companies, agents, health

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["Health"])
router.include_router(insights.router, prefix="/insights", tags=["Insights"])
router.include_router(companies.router, prefix="/companies", tags=["Companies"])
router.include_router(agents.router, prefix="/agents", tags=["Agents"])
