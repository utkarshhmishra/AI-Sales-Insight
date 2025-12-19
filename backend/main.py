"""
AI Sales Insight - FastAPI Backend
Main application entry point
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from core.config import settings
from core.logging_config import setup_logging
from api.v1 import router as api_router

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    logger.info("🚀 Starting AI Sales Insight API")
    logger.info(f"Environment: {settings.APP_ENV}")
    
    # Initialize services here
    # await init_database()
    # await init_vector_store()
    
    yield
    
    logger.info("🛑 Shutting down AI Sales Insight API")
    # Cleanup here


# Create FastAPI app
app = FastAPI(
    title="AI Sales Insight API",
    description="Intelligent Sales Intelligence Agent System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "AI Sales Insight API",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "environment": settings.APP_ENV,
        "timestamp": "2025-12-19T00:00:00Z"
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.APP_ENV == "development",
        log_level="info",
    )
