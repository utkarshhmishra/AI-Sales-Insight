"""
Financial Agent
Collects and analyzes financial data including stock performance, funding, and reports
"""

import asyncio
from typing import Dict, Any, List
import time
from datetime import datetime, timedelta
import random

from agents.base_agent import BaseAgent, AgentInput, AgentOutput
import logging

logger = logging.getLogger(__name__)


class FinancialAgent(BaseAgent):
    """Agent for collecting financial data and metrics"""
    
    def __init__(self):
        super().__init__(
            name="FinancialAgent",
            description="Gathers stock performance, funding rounds, and financial reports"
        )
    
    async def execute(self, input_data: AgentInput) -> AgentOutput:
        """Execute financial data collection"""
        start_time = time.time()
        
        try:
            await self.validate_input(input_data)
            
            self.logger.info(f"Collecting financial data for {input_data.company_name}")
            
            # Collect financial data
            stock_data = await self._fetch_stock_data(input_data.company_name)
            funding_info = await self._fetch_funding_info(input_data.company_name)
            financial_metrics = await self._fetch_financial_metrics(input_data.company_name)
            
            # Compile data
            data = {
                "stock_data": stock_data,
                "funding_info": funding_info,
                "financial_metrics": financial_metrics,
                "last_updated": datetime.now().isoformat()
            }
            
            # Generate insights
            insights = self._generate_insights(data)
            
            execution_time = int((time.time() - start_time) * 1000)
            
            output = self._create_output(
                status="success",
                data=data,
                insights=insights,
                confidence_score=0.78,
                execution_time_ms=execution_time
            )
            
            self.log_execution(input_data, output)
            return output
            
        except Exception as e:
            execution_time = int((time.time() - start_time) * 1000)
            self.logger.error(f"Error in FinancialAgent: {str(e)}")
            
            return self._create_output(
                status="error",
                data={},
                insights=[],
                confidence_score=0.0,
                execution_time_ms=execution_time,
                error_message=str(e)
            )
    
    async def _fetch_stock_data(self, company_name: str) -> Dict[str, Any]:
        """Fetch stock market data (if publicly traded)"""
        await asyncio.sleep(0.5)
        
        # In production: Use Yahoo Finance, Alpha Vantage, or similar
        # For this demo, simulate data
        is_public = random.choice([True, False])
        
        if not is_public:
            return {
                "status": "private",
                "message": "Company is privately held - no public stock data available"
            }
        
        # Simulate stock data
        current_price = round(random.uniform(500, 2000), 2)
        previous_close = round(current_price * random.uniform(0.95, 1.05), 2)
        change = round(current_price - previous_close, 2)
        change_percent = round((change / previous_close) * 100, 2)
        
        return {
            "status": "public",
            "ticker": f"{company_name[:4].upper()}",
            "exchange": "NSE",
            "current_price": current_price,
            "previous_close": previous_close,
            "change": change,
            "change_percent": change_percent,
            "day_high": round(current_price * 1.03, 2),
            "day_low": round(current_price * 0.97, 2),
            "volume": random.randint(1000000, 5000000),
            "market_cap": f"₹{random.randint(5000, 15000)} Cr",
            "52_week_high": round(current_price * 1.25, 2),
            "52_week_low": round(current_price * 0.75, 2)
        }
    
    async def _fetch_funding_info(self, company_name: str) -> Dict[str, Any]:
        """Fetch funding and investment information"""
        await asyncio.sleep(0.4)
        
        # In production: Use Crunchbase API, PitchBook, or similar
        return {
            "total_funding": "$95M",
            "last_funding_round": {
                "round": "Series B",
                "amount": "$45M",
                "date": "2024-06-15",
                "lead_investors": ["Sequoia Capital India", "Accel Partners"],
                "valuation": "$350M (estimated)"
            },
            "funding_history": [
                {
                    "round": "Series A",
                    "amount": "$15M",
                    "date": "2022-03-10",
                    "investors": ["Matrix Partners", "Nexus Venture Partners"]
                },
                {
                    "round": "Seed",
                    "amount": "$3M",
                    "date": "2020-08-20",
                    "investors": ["Blume Ventures", "India Quotient"]
                }
            ],
            "investors": [
                "Sequoia Capital India",
                "Accel Partners",
                "Matrix Partners",
                "Nexus Venture Partners",
                "Blume Ventures",
                "India Quotient"
            ]
        }
    
    async def _fetch_financial_metrics(self, company_name: str) -> Dict[str, Any]:
        """Fetch key financial metrics"""
        await asyncio.sleep(0.3)
        
        return {
            "revenue": {
                "current_year": "$65M (estimated)",
                "previous_year": "$45M",
                "growth_yoy": "44%"
            },
            "employees": {
                "current": 650,
                "previous_year": 480,
                "growth": "35%"
            },
            "burn_rate": "$3.5M/month (estimated)",
            "runway": "12+ months",
            "profitability_status": "Not yet profitable - focused on growth",
            "arr": "$60M (Annual Recurring Revenue)",
            "customer_count": "250+ enterprise customers",
            "average_deal_size": "$240K/year",
            "churn_rate": "8% (annual)"
        }
    
    def _generate_insights(self, data: Dict[str, Any]) -> List[str]:
        """Generate financial insights"""
        insights = []
        
        funding = data.get("funding_info", {})
        metrics = data.get("financial_metrics", {})
        
        insights.append(f"💰 Well-funded: {funding.get('total_funding', 'N/A')} raised with strong investor backing")
        insights.append(f"📊 Recent Series B ($45M) provides 12+ months runway - stable financial position")
        insights.append("🚀 Strong growth: 44% YoY revenue growth and 35% headcount expansion")
        insights.append("💵 High ARR: $60M indicates strong recurring revenue model")
        insights.append("📈 Healthy metrics: 250+ enterprise customers with $240K average deal size")
        insights.append("⚠️ Growth stage: Not yet profitable but investing in expansion (typical for SaaS)")
        insights.append("🎯 Low churn: 8% annual churn indicates strong customer satisfaction")
        
        return insights
