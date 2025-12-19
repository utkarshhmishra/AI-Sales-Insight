"""
Research Agent
Gathers general company information, background, and key decision-makers
"""

import asyncio
from typing import Dict, Any, List
import time
from datetime import datetime

from agents.base_agent import BaseAgent, AgentInput, AgentOutput
import logging

logger = logging.getLogger(__name__)


class ResearchAgent(BaseAgent):
    """Agent for researching company background and decision-makers"""
    
    def __init__(self):
        super().__init__(
            name="ResearchAgent",
            description="Gathers company background, products, services, and key personnel"
        )
    
    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """Execute research on target company"""
        start_time = time.time()
        
        try:
            await self.validate_input(input_data)
            
            self.logger.info(f"Starting research for {input_data.company_name}")
            
            # Simulate API calls and web scraping
            company_info = await self._gather_company_info(input_data.company_name)
            decision_makers = await self._identify_decision_makers(input_data.company_name)
            products_services = await self._research_offerings(input_data.company_name)
            
            # Compile data
            data = {
                "company_info": company_info,
                "decision_makers": decision_makers,
                "products_services": products_services,
                "last_updated": datetime.now().isoformat()
            }
            
            # Generate insights
            insights = self._generate_insights(data)
            
            execution_time = int((time.time() - start_time) * 1000)
            
            output = self._create_output(
                status="success",
                data=data,
                insights=insights,
                confidence_score=0.85,
                execution_time_ms=execution_time
            )
            
            self.log_execution(input_data, output)
            return output
            
        except Exception as e:
            execution_time = int((time.time() - start_time) * 1000)
            self.logger.error(f"Error in ResearchAgent: {str(e)}")
            
            return self._create_output(
                status="error",
                data={},
                insights=[],
                confidence_score=0.0,
                execution_time_ms=execution_time,
                error_message=str(e)
            )
    
    async def _gather_company_info(self, company_name: str) -> Dict[str, Any]:
        """Gather basic company information"""
        # Simulate API call delay
        await asyncio.sleep(0.5)
        
        # In production, this would use APIs like Clearbit, LinkedIn, etc.
        return {
            "name": company_name,
            "industry": "Technology / SaaS",
            "size": "500-1000 employees",
            "headquarters": "Bangalore, India",
            "founded": "2018",
            "website": f"www.{company_name.lower().replace(' ', '')}.com",
            "description": f"{company_name} is a leading provider of enterprise software solutions focused on digital transformation and business intelligence.",
            "revenue_range": "$50M - $100M (estimated)",
            "funding": "Series B - $45M raised"
        }
    
    async def _identify_decision_makers(self, company_name: str) -> List[Dict[str, Any]]:
        """Identify key decision-makers"""
        await asyncio.sleep(0.3)
        
        # In production, scrape LinkedIn or use Apollo.io API
        return [
            {
                "name": "Rajesh Kumar",
                "title": "VP of Sales",
                "linkedin": "linkedin.com/in/rajeshkumar",
                "email": "rajesh.kumar@example.com",
                "phone": "+91-98765-43210",
                "tenure": "2 years",
                "previous_company": "Salesforce"
            },
            {
                "name": "Priya Sharma",
                "title": "CTO",
                "linkedin": "linkedin.com/in/priyasharma",
                "email": "priya.sharma@example.com",
                "tenure": "3 years",
                "previous_company": "Microsoft"
            },
            {
                "name": "Amit Patel",
                "title": "Head of Procurement",
                "linkedin": "linkedin.com/in/amitpatel",
                "email": "amit.patel@example.com",
                "tenure": "1 year",
                "previous_company": "TCS"
            }
        ]
    
    async def _research_offerings(self, company_name: str) -> Dict[str, Any]:
        """Research company's products and services"""
        await asyncio.sleep(0.4)
        
        return {
            "main_products": [
                "Enterprise Analytics Platform",
                "AI-powered Business Intelligence Suite",
                "Data Visualization Tools"
            ],
            "services": [
                "Consulting and Implementation",
                "24/7 Technical Support",
                "Training and Certification"
            ],
            "target_market": "Mid to large enterprises in BFSI, Retail, and Manufacturing",
            "competitive_advantages": [
                "AI-native architecture",
                "Easy integration with existing systems",
                "Strong customer support in Indian market"
            ],
            "pricing_model": "Subscription-based (Annual contracts)"
        }
    
    def _generate_insights(self, data: Dict[str, Any]) -> List[str]:
        """Generate actionable insights from collected data"""
        insights = []
        
        company_info = data.get("company_info", {})
        decision_makers = data.get("decision_makers", [])
        
        insights.append(f"Company is in growth phase with recent Series B funding of $45M")
        insights.append(f"Decision-making team includes {len(decision_makers)} key contacts across Sales, Technology, and Procurement")
        insights.append(f"VP of Sales has Salesforce background - potential familiarity with CRM solutions")
        insights.append(f"Target market alignment: Enterprise focus with strong presence in BFSI sector")
        insights.append(f"Technology stack emphasis on AI/ML indicates progressive tech adoption")
        
        return insights
