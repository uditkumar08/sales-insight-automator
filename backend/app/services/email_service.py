import smtplib
from email.mime.text import MIMEText
import logging
from app.config import settings

logger = logging.getLogger(__name__)

async def send_email(to_email: str, summary: str) -> bool:
    """Send email with AI-generated summary
    
    Supports multiple modes:
    1. SMTP (Gmail with app password)
    2. Mock mode (EMAIL_PASS=mock) - for testing
    
    Args:
        to_email: Recipient email address (ANY email works!)
        summary: Email body content
        
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        if not settings.EMAIL_USER or not settings.EMAIL_PASS:
            logger.error("Email credentials not configured")
            return False
        
        # Mock mode for testing (any recipient email works!)
        if settings.EMAIL_PASS.lower() == "mock":
            logger.info(f"📧 [MOCK EMAIL] Sent to: {to_email}")
            logger.info(f"   From: {settings.EMAIL_USER}")
            logger.info(f"   Subject: AI Data Report")
            logger.info(f"   Body: {summary[:100]}...")
            return True
        
        # Real SMTP mode
        msg = MIMEText(summary)
        msg["Subject"] = "AI Data Report"
        msg["From"] = settings.EMAIL_USER
        msg["To"] = to_email
        
        server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
        
        server.send_message(msg)
        server.quit()
        
        logger.info(f"✅ Email sent successfully to {to_email}")
        return True
        
    except smtplib.SMTPAuthenticationError:
        logger.error("SMTP authentication failed - check EMAIL_USER and EMAIL_PASS")
        logger.info("💡 Tip: Use EMAIL_PASS=mock for testing, or get Gmail app password")
        return False
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False