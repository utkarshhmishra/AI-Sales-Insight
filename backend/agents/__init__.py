"""Agents module initialization"""

from .base_agent import BaseAgent, AgentInput, AgentOutput
from .research_agent import ResearchAgent
from .news_agent import NewsAgent
from .financial_agent import FinancialAgent
from .social_media_agent import SocialMediaAgent
from .insight_synthesizer import InsightSynthesizerAgent
from .orchestrator import AgentOrchestrator

__all__ = [
    "BaseAgent",
    "AgentInput",
    "AgentOutput",
    "ResearchAgent",
    "NewsAgent",
    "FinancialAgent",
    "SocialMediaAgent",
    "InsightSynthesizerAgent",
    "AgentOrchestrator"
]
