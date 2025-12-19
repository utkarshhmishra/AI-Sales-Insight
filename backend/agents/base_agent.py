"""
Base Agent Class
All specialized agents inherit from this base class
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from datetime import datetime
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class AgentInput(BaseModel):
    """Standard input for agents"""
    company_name: str = Field(..., description="Target company name")
    context: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional context")
    timeframe_days: int = Field(default=30, description="Data collection timeframe in days")
    priority: str = Field(default="medium", description="Priority level: low, medium, high")


class AgentOutput(BaseModel):
    """Standard output from agents"""
    agent_name: str = Field(..., description="Name of the agent")
    status: str = Field(..., description="Status: success, partial, error")
    data: Dict[str, Any] = Field(default_factory=dict, description="Collected data")
    insights: List[str] = Field(default_factory=list, description="Key insights")
    confidence_score: float = Field(default=0.0, ge=0.0, le=1.0, description="Confidence in data quality")
    execution_time_ms: int = Field(..., description="Execution time in milliseconds")
    timestamp: datetime = Field(default_factory=datetime.now)
    error_message: Optional[str] = None


class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.logger = logging.getLogger(f"agent.{name}")
    
    @abstractmethod
    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """
        Execute the agent's main task
        
        Args:
            input_data: Standardized input data
            
        Returns:
            AgentOutput: Standardized output with results
        """
        pass
    
    def _create_output(
        self,
        status: str,
        data: Dict[str, Any],
        insights: List[str],
        confidence_score: float,
        execution_time_ms: int,
        error_message: Optional[str] = None
    ) -> AgentOutput:
        """Helper to create standardized output"""
        return AgentOutput(
            agent_name=self.name,
            status=status,
            data=data,
            insights=insights,
            confidence_score=confidence_score,
            execution_time_ms=execution_time_ms,
            error_message=error_message
        )
    
    async def validate_input(self, input_data: AgentInput) -> bool:
        """Validate input data"""
        if not input_data.company_name:
            raise ValueError("Company name is required")
        return True
    
    def log_execution(self, input_data: AgentInput, output: AgentOutput):
        """Log agent execution"""
        self.logger.info(
            f"Agent '{self.name}' executed for {input_data.company_name} "
            f"- Status: {output.status}, Time: {output.execution_time_ms}ms, "
            f"Confidence: {output.confidence_score:.2f}"
        )
