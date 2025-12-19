"""
Agent Orchestrator
Coordinates multiple agents and manages their execution
"""

import asyncio
from typing import Dict, Any, List, Optional
import time
from datetime import datetime
import logging

from agents.base_agent import AgentInput, AgentOutput
from agents.research_agent import ResearchAgent
from agents.news_agent import NewsAgent
from agents.financial_agent import FinancialAgent
from agents.social_media_agent import SocialMediaAgent
from agents.insight_synthesizer import InsightSynthesizerAgent

logger = logging.getLogger(__name__)


class AgentOrchestrator:
    """Orchestrates multiple agents to gather and synthesize insights"""
    
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.news_agent = NewsAgent()
        self.financial_agent = FinancialAgent()
        self.social_media_agent = SocialMediaAgent()
        self.insight_synthesizer = InsightSynthesizerAgent()
        
        self.logger = logging.getLogger("orchestrator")
    
    async def gather_insights(
        self,
        company_name: str,
        context: Optional[Dict[str, Any]] = None,
        timeframe_days: int = 30,
        priority: str = "medium"
    ) -> Dict[str, Any]:
        """
        Orchestrate all agents to gather comprehensive insights
        
        Args:
            company_name: Name of the target company
            context: Additional context for agents
            timeframe_days: Data collection timeframe
            priority: Priority level (low, medium, high)
            
        Returns:
            Dict containing all agent outputs and synthesized insights
        """
        start_time = time.time()
        self.logger.info(f"🚀 Starting insight gathering for {company_name}")
        
        try:
            # Create input for agents
            agent_input = AgentInput(
                company_name=company_name,
                context=context or {},
                timeframe_days=timeframe_days,
                priority=priority
            )
            
            # Execute data collection agents in parallel
            self.logger.info("[DATA] Executing data collection agents...")
            research_output, news_output, financial_output, social_output = await asyncio.gather(
                self.research_agent.execute(agent_input),
                self.news_agent.execute(agent_input),
                self.financial_agent.execute(agent_input),
                self.social_media_agent.execute(agent_input),
                return_exceptions=True
            )
            
            # Handle any exceptions
            agent_outputs = {}
            for name, output in [
                ("research", research_output),
                ("news", news_output),
                ("financial", financial_output),
                ("social_media", social_output)
            ]:
                if isinstance(output, Exception):
                    self.logger.error(f"Error in {name} agent: {str(output)}")
                    agent_outputs[name] = None
                elif output and isinstance(output, AgentOutput):
                    # Use model_dump for Pydantic v2, dict for v1
                    agent_outputs[name] = output.model_dump() if hasattr(output, 'model_dump') else output.dict()
                else:
                    agent_outputs[name] = None
            
            # Synthesize insights
            self.logger.info("[SYNTHESIS] Synthesizing insights...")
            synthesis_input = AgentInput(
                company_name=company_name,
                context={"agent_outputs": agent_outputs},
                timeframe_days=timeframe_days,
                priority=priority
            )
            
            synthesis_output = await self.insight_synthesizer.execute(synthesis_input)
            
            # Calculate total execution time
            total_time = int((time.time() - start_time) * 1000)
            
            # Compile final result
            result = {
                "company_name": company_name,
                "status": "success",
                "timestamp": datetime.now().isoformat(),
                "execution_time_ms": total_time,
                "agent_outputs": agent_outputs,
                "synthesis": synthesis_output.dict() if hasattr(synthesis_output, 'dict') else synthesis_output,
                "summary": self._create_summary(agent_outputs, synthesis_output)
            }
            
            self.logger.info(f"[SUCCESS] Insight gathering completed in {total_time}ms")
            return result
            
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self.logger.error(f"❌ Error in orchestration: {str(e)}")
            
            return {
                "company_name": company_name,
                "status": "error",
                "timestamp": datetime.now().isoformat(),
                "execution_time_ms": total_time,
                "error": str(e)
            }
    
    async def quick_brief(self, company_name: str) -> Dict[str, Any]:
        """
        Generate a quick brief (faster, less comprehensive)
        Only runs essential agents
        """
        start_time = time.time()
        self.logger.info(f"⚡ Generating quick brief for {company_name}")
        
        try:
            agent_input = AgentInput(
                company_name=company_name,
                timeframe_days=7,
                priority="high"
            )
            
            # Run only essential agents
            research_output, news_output = await asyncio.gather(
                self.research_agent.execute(agent_input),
                self.news_agent.execute(agent_input)
            )
            
            total_time = int((time.time() - start_time) * 1000)
            
            return {
                "company_name": company_name,
                "status": "success",
                "type": "quick_brief",
                "timestamp": datetime.now().isoformat(),
                "execution_time_ms": total_time,
                "research": research_output.dict() if hasattr(research_output, 'dict') else research_output,
                "news": news_output.dict() if hasattr(news_output, 'dict') else news_output
            }
            
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self.logger.error(f"Error in quick brief: {str(e)}")
            return {
                "company_name": company_name,
                "status": "error",
                "execution_time_ms": total_time,
                "error": str(e)
            }
    
    def _create_summary(self, agent_outputs: Dict[str, Any], synthesis: Any) -> Dict[str, Any]:
        """Create a high-level summary of results"""
        
        # Count successful agents
        successful_agents = sum(1 for output in agent_outputs.values() if output and output.get("status") == "success")
        total_agents = len(agent_outputs)
        
        # Extract key insights
        all_insights = []
        for output in agent_outputs.values():
            if output and output.get("insights"):
                all_insights.extend(output["insights"][:2])  # Top 2 from each
        
        synthesis_data = synthesis.dict() if hasattr(synthesis, 'dict') else synthesis
        
        return {
            "data_completeness": f"{successful_agents}/{total_agents} agents successful",
            "top_insights": all_insights[:5],
            "preparation_score": synthesis_data.get("data", {}).get("meeting_preparation_score", {}),
            "ready_for_meeting": successful_agents >= 3
        }
    
    async def get_agent_status(self) -> Dict[str, Any]:
        """Get status of all agents"""
        return {
            "available_agents": [
                {
                    "name": self.research_agent.name,
                    "description": self.research_agent.description,
                    "status": "active"
                },
                {
                    "name": self.news_agent.name,
                    "description": self.news_agent.description,
                    "status": "active"
                },
                {
                    "name": self.financial_agent.name,
                    "description": self.financial_agent.description,
                    "status": "active"
                },
                {
                    "name": self.social_media_agent.name,
                    "description": self.social_media_agent.description,
                    "status": "active"
                },
                {
                    "name": self.insight_synthesizer.name,
                    "description": self.insight_synthesizer.description,
                    "status": "active"
                }
            ],
            "total_agents": 5,
            "orchestrator_version": "1.0.0"
        }
