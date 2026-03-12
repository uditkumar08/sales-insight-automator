from pydantic_settings import BaseSettings
from typing import Optional
import os
from pathlib import Path

# Load .env file explicitly
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

class Settings(BaseSettings):
    """Application configuration from environment variables"""
    
    # API Configuration
    API_TITLE: str = "Sales Insight Automator"
    API_DESCRIPTION: str = "AI powered sales report generator"
    API_VERSION: str = "1.0.0"
    
    # LLM Configuration
    GEMINI_API_KEY: Optional[str] = None
    
    # Email Configuration
    EMAIL_USER: Optional[str] = None
    EMAIL_PASS: Optional[str] = None
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    
    # Frontend Configuration (for CORS)
    FRONTEND_URL: str = "http://localhost:3000"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # Deployment URLs
    BACKEND_URL: Optional[str] = None
    API_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# Log configuration on startup
import logging
logger = logging.getLogger(__name__)

def log_config():
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Frontend URL: {settings.FRONTEND_URL}")
    logger.info(f"Gemini API: {'Configured' if settings.GEMINI_API_KEY else 'Not Configured'}")
    logger.info(f"Email Service: {'Configured' if settings.EMAIL_USER else 'Not Configured'}")

