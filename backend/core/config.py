"""
Core configuration module
Loads environment variables and application settings
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    SECRET_KEY: str = "change-this-in-production"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # LLM APIs
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama2"
    
    # Data Source APIs
    NEWS_API_KEY: Optional[str] = None
    GOOGLE_NEWS_API_KEY: Optional[str] = None
    ALPHA_VANTAGE_API_KEY: Optional[str] = None
    FINANCIAL_MODELING_PREP_API_KEY: Optional[str] = None
    TWITTER_API_KEY: Optional[str] = None
    TWITTER_API_SECRET: Optional[str] = None
    TWITTER_BEARER_TOKEN: Optional[str] = None
    LINKEDIN_ACCESS_TOKEN: Optional[str] = None
    SERPER_API_KEY: Optional[str] = None
    BRAVE_SEARCH_API_KEY: Optional[str] = None
    
    # Database
    DATABASE_URL: str = "postgresql://salesinsight:salesinsight123@localhost:5432/ai_sales_insight"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Agent Configuration
    MAX_CONCURRENT_AGENTS: int = 5
    AGENT_TIMEOUT_SECONDS: int = 120
    ENABLE_CACHING: bool = True
    CACHE_TTL_HOURS: int = 24
    
    # Logging
    LOG_LEVEL: str = "INFO"
    ENABLE_TELEMETRY: bool = True
    SENTRY_DSN: Optional[str] = None
    
    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: str = "noreply@aisalesinsight.com"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow"
    )


# Create settings instance
settings = Settings()
