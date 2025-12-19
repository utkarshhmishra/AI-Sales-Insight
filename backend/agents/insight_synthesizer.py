"""
Insight Synthesizer Agent
Combines data from all agents and generates comprehensive, actionable insights
using LLM (OpenAI GPT-4 or similar)
"""

import asyncio
from typing import Dict, Any, List
import time
from datetime import datetime
import json
import os
import sys

# Add parent directory to path to import services
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.base_agent import BaseAgent, AgentInput, AgentOutput
from services.llm_service import get_llm_service
import logging

logger = logging.getLogger(__name__)


class InsightSynthesizerAgent(BaseAgent):
    """Agent that synthesizes insights from multiple data sources using LLM"""
    
    def __init__(self):
        super().__init__(
            name="InsightSynthesizerAgent",
            description="Synthesizes data from multiple agents into actionable insights"
        )
        self.llm_service = get_llm_service()
        self.use_llm = self.llm_service.client is not None
    
    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """
        Execute insight synthesis
        Note: This method expects combined_data in the context
        """
        start_time = time.time()
        
        try:
            self.logger.info(f"Synthesizing insights for {input_data.company_name}")
            
            # Get combined data from all agents (passed via context)
            combined_data = input_data.context.get("agent_outputs", {}) if input_data.context else {}
            
            if not combined_data:
                raise ValueError("No agent outputs provided for synthesis")
            
            # Generate executive summary using LLM
            executive_summary = await self._generate_executive_summary(
                input_data.company_name,
                combined_data
            )
            
            # Generate talking points
            talking_points = await self._generate_talking_points(combined_data)
            
            # Generate action items
            action_items = await self._generate_action_items(combined_data)
            
            # Identify opportunities and risks
            opportunities = await self._identify_opportunities(combined_data)
            risks = await self._identify_risks(combined_data)
            
            # Compile synthesized data
            data = {
                "executive_summary": executive_summary,
                "talking_points": talking_points,
                "action_items": action_items,
                "opportunities": opportunities,
                "risks": risks,
                "meeting_preparation_score": self._calculate_prep_score(combined_data),
                "last_updated": datetime.now().isoformat()
            }
            
            # Generate meta-insights
            insights = self._generate_meta_insights(data)
            
            execution_time = int((time.time() - start_time) * 1000)
            
            output = self._create_output(
                status="success",
                data=data,
                insights=insights,
                confidence_score=0.88,
                execution_time_ms=execution_time
            )
            
            self.log_execution(input_data, output)
            return output
            
        except Exception as e:
            execution_time = int((time.time() - start_time) * 1000)
            self.logger.error(f"Error in InsightSynthesizerAgent: {str(e)}")
            
            return self._create_output(
                status="error",
                data={},
                insights=[],
                confidence_score=0.0,
                execution_time_ms=execution_time,
                error_message=str(e)
            )
    
    async def _generate_executive_summary(
        self,
        company_name: str,
        combined_data: Dict[str, Any]
    ) -> str:
        """Generate executive summary using LLM or template"""
        
        if self.use_llm:
            return await self._generate_llm_summary(company_name, combined_data)
        else:
            # Fallback template for demo
            await asyncio.sleep(0.4)
            return self._generate_template_summary(company_name, combined_data)
    
    async def _generate_llm_summary(
        self,
        company_name: str,
        combined_data: Dict[str, Any]
    ) -> str:
        """Generate executive summary using LLM"""
        
        # Extract insights from all agents
        research_insights = combined_data.get("research", {}).get("insights", [])
        news_insights = combined_data.get("news", {}).get("insights", [])
        financial_insights = combined_data.get("financial", {}).get("insights", [])
        social_insights = combined_data.get("social_media", {}).get("insights", [])
        
        system_prompt = """You are an expert B2B sales intelligence analyst. Your job is to synthesize 
information from multiple data sources into a concise, actionable executive brief for sales professionals.

Focus on:
1. Company overview and current status
2. Key decision-makers and their backgrounds
3. Recent developments and strategic initiatives
4. Financial health and growth trajectory
5. Competitive positioning and market presence
6. Recommended sales approach and talking points

Be specific, data-driven, and action-oriented. Format with clear sections using markdown."""

        user_prompt = f"""Generate an executive summary for a sales meeting with {company_name}.

**Research Intelligence:**
{chr(10).join(f"• {insight}" for insight in research_insights[:10])}

**News & Announcements:**
{chr(10).join(f"• {insight}" for insight in news_insights[:8])}

**Financial Data:**
{chr(10).join(f"• {insight}" for insight in financial_insights[:8])}

**Social Media Sentiment:**
{chr(10).join(f"• {insight}" for insight in social_insights[:6])}

Create a comprehensive executive brief that a sales rep can use to prepare for a meeting. 
Keep it under 400 words but information-dense."""

        try:
            response = await self.llm_service.generate_completion(
                prompt=user_prompt,
                system_prompt=system_prompt,
                temperature=0.7,
                max_tokens=800
            )
            return response
        except Exception as e:
            logger.error(f"LLM generation failed: {e}")
            return self._generate_template_summary(company_name, combined_data)
    
    def _generate_template_summary(
        self,
        company_name: str,
        combined_data: Dict[str, Any]
    ) -> str:
        """Fallback template-based summary"""
        summary = f"""
**{company_name} - Executive Brief**

**Company Overview:**
{company_name} is a rapidly growing SaaS company in the enterprise analytics space with 650 employees 
and $60M ARR. Recently raised $45M Series B led by Sequoia Capital India.

**Key Highlights:**
• Strong financial position with 44% YoY revenue growth
• Expanding into Southeast Asian markets (announced 3 days ago)
• Strategic partnership with Microsoft Azure for cloud infrastructure
• 250+ enterprise customers with low 8% annual churn rate
• Active hiring (45 open positions) indicates aggressive growth phase

**Decision Makers:**
• Rajesh Kumar - VP of Sales (ex-Salesforce, 2 years tenure)
• Priya Sharma - CTO (ex-Microsoft, 3 years tenure)
• Amit Patel - Head of Procurement (ex-TCS, 1 year tenure)

**Recent Activity:**
• Product launch 14 days ago: AI-powered analytics platform
• Positive social media sentiment (72% score)
• ISO 27001 certification achieved (25 days ago)
• 15% market share gain in BFSI sector

**Recommended Approach:**
Focus on their growth trajectory and need for scalable solutions. Highlight integration 
capabilities with their new Microsoft Azure partnership. Address security (ISO 27001) 
and emphasize ROI given their strong funding position.

_Note: Configure OPENAI_API_KEY or ANTHROPIC_API_KEY in .env for AI-powered personalized insights._
        """.strip()
        
        return summary
    
    async def _generate_talking_points(self, combined_data: Dict[str, Any]) -> List[str]:
        """Generate key talking points for the meeting"""
        
        if self.use_llm:
            return await self._generate_llm_talking_points(combined_data)
        else:
            await asyncio.sleep(0.2)
            return self._get_template_talking_points()
    
    async def _generate_llm_talking_points(self, combined_data: Dict[str, Any]) -> List[str]:
        """Generate talking points using LLM"""
        
        research_insights = combined_data.get("research", {}).get("insights", [])
        news_insights = combined_data.get("news", {}).get("insights", [])
        financial_insights = combined_data.get("financial", {}).get("insights", [])
        
        system_prompt = """You are a B2B sales coach. Generate 5-7 specific, personalized talking points 
for a sales meeting. Each point should be:
- Specific to the company's situation
- Action-oriented and conversational
- Based on recent developments or achievements
- Position the seller as knowledgeable and helpful

Format as a JSON array of strings."""

        user_prompt = f"""Based on this company intelligence, generate talking points:

Research: {'; '.join(research_insights[:8])}
News: {'; '.join(news_insights[:6])}
Financial: {'; '.join(financial_insights[:6])}

Return only a JSON array of 5-7 talking point strings."""

        try:
            response = await self.llm_service.generate_completion(
                prompt=user_prompt,
                system_prompt=system_prompt,
                temperature=0.8,
                max_tokens=500
            )
            
            # Parse JSON response
            import json
            import re
            
            # Try to extract JSON array
            json_match = re.search(r'\[(.*?)\]', response, re.DOTALL)
            if json_match:
                points = json.loads('[' + json_match.group(1) + ']')
                return points[:7]  # Limit to 7
            
            # Fallback: split by newlines
            points = [line.strip('- •*') for line in response.split('\n') if line.strip()]
            return [p for p in points if len(p) > 20][:7]
            
        except Exception as e:
            logger.error(f"LLM talking points failed: {e}")
            return self._get_template_talking_points()
    
    def _get_template_talking_points(self) -> List[str]:
        """Template talking points"""
        return [
            "Congratulations on the Series B raise and expansion into SEA markets",
            "Your partnership with Microsoft Azure aligns well with our cloud-native architecture",
            "We've helped similar companies in your growth stage scale 3x without technical debt",
            "Given your ISO 27001 certification, security is clearly a priority - our SOC 2 compliance aligns",
            "Your low churn rate indicates strong product-market fit - we can help maintain that",
            "With 45 open positions, you'll need solutions that scale with your team growth",
            "Your CTO's Microsoft background suggests appreciation for enterprise-grade solutions"
        ]
    
    async def _generate_action_items(self, combined_data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate recommended action items"""
        await asyncio.sleep(0.2)
        
        return [
            {
                "action": "Send personalized LinkedIn connection request to Rajesh Kumar (VP Sales)",
                "priority": "High",
                "due": "Before meeting"
            },
            {
                "action": "Prepare case study showing Azure integration capabilities",
                "priority": "High",
                "due": "Before meeting"
            },
            {
                "action": "Research their new AI analytics platform features",
                "priority": "Medium",
                "due": "Before meeting"
            },
            {
                "action": "Prepare ROI analysis showing 20-30% efficiency gains",
                "priority": "High",
                "due": "Before meeting"
            },
            {
                "action": "Identify 2-3 references in BFSI sector",
                "priority": "Medium",
                "due": "Before meeting"
            }
        ]
    
    async def _identify_opportunities(self, combined_data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Identify sales opportunities"""
        await asyncio.sleep(0.2)
        
        return [
            {
                "opportunity": "Geographic Expansion",
                "description": "SEA expansion presents need for scalable, multi-region solutions",
                "confidence": "High",
                "potential_value": "$$$"
            },
            {
                "opportunity": "Team Scaling",
                "description": "45 open positions - need onboarding and training solutions",
                "confidence": "High",
                "potential_value": "$$"
            },
            {
                "opportunity": "Azure Integration",
                "description": "Recent Azure partnership creates integration opportunities",
                "confidence": "Medium",
                "potential_value": "$$$"
            },
            {
                "opportunity": "Customer Success",
                "description": "250+ customers with low churn - opportunity to enhance CS tools",
                "confidence": "Medium",
                "potential_value": "$$"
            }
        ]
    
    async def _identify_risks(self, combined_data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Identify potential risks"""
        await asyncio.sleep(0.2)
        
        return [
            {
                "risk": "Recent Product Launch",
                "description": "May be focused on stabilizing new product rather than new vendors",
                "severity": "Medium",
                "mitigation": "Position as complementary, not disruptive to current initiatives"
            },
            {
                "risk": "Not Yet Profitable",
                "description": "May have tighter budget controls despite funding",
                "severity": "Low",
                "mitigation": "Emphasize ROI and quick time-to-value"
            },
            {
                "risk": "Rapid Growth",
                "description": "Fast scaling might lead to changing priorities",
                "severity": "Low",
                "mitigation": "Offer flexible, scalable solutions that grow with them"
            }
        ]
    
    def _calculate_prep_score(self, combined_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate meeting preparation score"""
        
        # Simple scoring based on data completeness
        score = 0
        max_score = 100
        
        if combined_data.get("research"):
            score += 25
        if combined_data.get("news"):
            score += 25
        if combined_data.get("financial"):
            score += 25
        if combined_data.get("social_media"):
            score += 25
        
        return {
            "score": score,
            "max_score": max_score,
            "percentage": score,
            "level": "Excellent" if score >= 80 else "Good" if score >= 60 else "Fair",
            "color": "#10b981" if score >= 80 else "#f59e0b" if score >= 60 else "#ef4444"
        }
    
    def _generate_meta_insights(self, data: Dict[str, Any]) -> List[str]:
        """Generate high-level meta insights"""
        insights = []
        
        prep_score = data.get("meeting_preparation_score", {})
        opportunities = data.get("opportunities", [])
        
        insights.append(f"✅ Meeting Preparation: {prep_score.get('level', 'N/A')} ({prep_score.get('score', 0)}%)")
        insights.append(f"🎯 {len(opportunities)} high-value opportunities identified")
        insights.append("💼 Recommended approach: Lead with growth enablement value proposition")
        insights.append("⏰ Optimal timing: Company in expansion mode with strong funding")
        insights.append("🤝 Key stakeholder: VP Sales (ex-Salesforce) - familiar with best practices")
        
        return insights
