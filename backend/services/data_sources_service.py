"""
Data Sources Service
Integrates with external APIs for real company data
"""

import os
import aiohttp
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class DataSourcesService:
    """Service for fetching data from external APIs"""
    
    def __init__(self):
        self.newsapi_key = os.getenv("NEWSAPI_KEY")
        self.serper_key = os.getenv("SERPER_API_KEY")  # For Google Search
        self.clearbit_key = os.getenv("CLEARBIT_API_KEY")  # For company enrichment
        self.alphavantage_key = os.getenv("ALPHAVANTAGE_API_KEY")  # For financial data
        
    async def search_company_news(
        self,
        company_name: str,
        days_back: int = 30
    ) -> List[Dict[str, Any]]:
        """
        Search for company news using NewsAPI
        
        Args:
            company_name: Name of the company
            days_back: Number of days to look back
            
        Returns:
            List of news articles
        """
        if not self.newsapi_key:
            logger.warning("NewsAPI key not configured")
            return self._get_mock_news(company_name)
        
        try:
            from_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
            
            url = "https://newsapi.org/v2/everything"
            params = {
                "q": company_name,
                "from": from_date,
                "sortBy": "relevancy",
                "language": "en",
                "apiKey": self.newsapi_key,
                "pageSize": 20
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        articles = data.get("articles", [])
                        
                        return [{
                            "title": article.get("title"),
                            "description": article.get("description"),
                            "url": article.get("url"),
                            "source": article.get("source", {}).get("name"),
                            "published_at": article.get("publishedAt"),
                            "sentiment": self._analyze_sentiment(article.get("title", "") + " " + article.get("description", ""))
                        } for article in articles]
                    else:
                        logger.error(f"NewsAPI error: {response.status}")
                        return self._get_mock_news(company_name)
                        
        except Exception as e:
            logger.error(f"Error fetching news: {e}")
            return self._get_mock_news(company_name)
    
    async def search_web(
        self,
        query: str,
        num_results: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Perform web search using Serper API (Google Search)
        
        Args:
            query: Search query
            num_results: Number of results to return
            
        Returns:
            List of search results
        """
        if not self.serper_key:
            logger.warning("Serper API key not configured")
            return []
        
        try:
            url = "https://google.serper.dev/search"
            headers = {
                "X-API-KEY": self.serper_key,
                "Content-Type": "application/json"
            }
            payload = {
                "q": query,
                "num": num_results
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        results = data.get("organic", [])
                        
                        return [{
                            "title": result.get("title"),
                            "snippet": result.get("snippet"),
                            "url": result.get("link"),
                            "position": result.get("position")
                        } for result in results]
                    else:
                        logger.error(f"Serper API error: {response.status}")
                        return []
                        
        except Exception as e:
            logger.error(f"Error performing web search: {e}")
            return []
    
    async def enrich_company_data(
        self,
        company_domain: str
    ) -> Optional[Dict[str, Any]]:
        """
        Enrich company data using Clearbit API
        
        Args:
            company_domain: Company domain (e.g., "microsoft.com")
            
        Returns:
            Enriched company data
        """
        if not self.clearbit_key:
            logger.warning("Clearbit API key not configured")
            return None
        
        try:
            url = f"https://company.clearbit.com/v2/companies/find"
            headers = {"Authorization": f"Bearer {self.clearbit_key}"}
            params = {"domain": company_domain}
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, params=params) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Clearbit API error: {response.status}")
                        return None
                        
        except Exception as e:
            logger.error(f"Error enriching company data: {e}")
            return None
    
    async def get_stock_data(
        self,
        symbol: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get stock data using Alpha Vantage API
        
        Args:
            symbol: Stock ticker symbol
            
        Returns:
            Stock data
        """
        if not self.alphavantage_key:
            logger.warning("Alpha Vantage API key not configured")
            return None
        
        try:
            url = "https://www.alphavantage.co/query"
            params = {
                "function": "GLOBAL_QUOTE",
                "symbol": symbol,
                "apikey": self.alphavantage_key
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        quote = data.get("Global Quote", {})
                        
                        if quote:
                            return {
                                "symbol": symbol,
                                "price": float(quote.get("05. price", 0)),
                                "change": float(quote.get("09. change", 0)),
                                "change_percent": quote.get("10. change percent", "0%"),
                                "volume": int(quote.get("06. volume", 0)),
                                "latest_trading_day": quote.get("07. latest trading day")
                            }
                        return None
                    else:
                        logger.error(f"Alpha Vantage API error: {response.status}")
                        return None
                        
        except Exception as e:
            logger.error(f"Error fetching stock data: {e}")
            return None
    
    def _analyze_sentiment(self, text: str) -> float:
        """
        Simple sentiment analysis
        In production: Use TextBlob, VADER, or LLM-based analysis
        
        Returns:
            Sentiment score between -1 (negative) and 1 (positive)
        """
        positive_words = ['growth', 'success', 'innovation', 'partnership', 'expansion', 'award', 'achievement']
        negative_words = ['decline', 'loss', 'lawsuit', 'controversy', 'layoff', 'scandal', 'fail']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count + negative_count == 0:
            return 0.0
        
        return (positive_count - negative_count) / (positive_count + negative_count)
    
    def _get_mock_news(self, company_name: str) -> List[Dict[str, Any]]:
        """Generate mock news data for demo"""
        return [
            {
                "title": f"{company_name} Announces Major Product Launch",
                "description": f"{company_name} unveiled its latest product innovation at the annual conference",
                "url": "https://example.com/news1",
                "source": "TechCrunch",
                "published_at": (datetime.now() - timedelta(days=5)).isoformat(),
                "sentiment": 0.8
            },
            {
                "title": f"{company_name} Expands to New Markets",
                "description": f"{company_name} announced expansion plans into Southeast Asian markets",
                "url": "https://example.com/news2",
                "source": "Business Wire",
                "published_at": (datetime.now() - timedelta(days=12)).isoformat(),
                "sentiment": 0.6
            },
            {
                "title": f"{company_name} Reports Strong Q4 Results",
                "description": f"{company_name} exceeded revenue expectations with 40% YoY growth",
                "url": "https://example.com/news3",
                "source": "Reuters",
                "published_at": (datetime.now() - timedelta(days=20)).isoformat(),
                "sentiment": 0.9
            }
        ]


# Singleton instance
_data_sources_service = None


def get_data_sources_service() -> DataSourcesService:
    """Get or create data sources service singleton"""
    global _data_sources_service
    if _data_sources_service is None:
        _data_sources_service = DataSourcesService()
    return _data_sources_service
