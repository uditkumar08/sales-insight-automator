from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload
from app.config import settings, log_config
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION
)

# Log configuration at startup
log_config()

# Determine allowed origins for CORS
allowed_origins = [
    settings.FRONTEND_URL,
    "http://localhost:3000",
    "http://localhost:5173",  # Vite default
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

# Add backend URL if configured for deployment
if settings.BACKEND_URL:
    backend_host = settings.BACKEND_URL.split("://")[1].split(":")[0] if "://" in settings.BACKEND_URL else settings.BACKEND_URL
    allowed_origins.extend([
        f"https://*.{backend_host}",
        f"https://{backend_host}",
    ])

# Add all Vercel and Render deployments
allowed_origins.extend([
    "https://*.vercel.app",
    "https://*.onrender.com",
    "https://*.netlify.app",
])

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)

@app.get("/")
def home():
    return {
        "message": "API running",
        "version": settings.API_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "ready"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": settings.API_VERSION,
        "gemini_configured": bool(settings.GEMINI_API_KEY),
        "email_configured": bool(settings.EMAIL_USER)
    }

@app.get("/config")
def get_config():
    """Get public configuration (no sensitive data)"""
    return {
        "api_title": settings.API_TITLE,
        "api_version": settings.API_VERSION,
        "environment": settings.ENVIRONMENT,
        "features": {
            "ai_summaries": bool(settings.GEMINI_API_KEY),
            "email_delivery": bool(settings.EMAIL_USER)
        }
    }

# Log startup
@app.on_event("startup")
async def startup_event():
    logger.info(f"🚀 Sales Insight Automator {settings.API_VERSION} starting...")
    logger.info(f"📡 Environment: {settings.ENVIRONMENT}")
    logger.info(f"🔐 CORS Origins: {len(allowed_origins)} origins configured")
    logger.info(f"✨ Ready to accept requests")