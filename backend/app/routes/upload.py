from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pandas as pd
import logging
import io
from email_validator import validate_email, EmailNotValidError
from app.services.llm_service import generate_summary
from app.services.email_service import send_email
from app.services.csv_service import analyze_sales

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["upload"])

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), email: str = Form(...)):
    """Upload CSV file and send AI-generated summary to email
    
    Args:
        file: CSV file to upload
        email: Email address to send summary to
        
    Returns:
        dict: Result message and analysis data
    """
    try:
        # Validate email
        try:
            valid_email = validate_email(email).email
        except EmailNotValidError as e:
            logger.warning(f"Invalid email provided: {email}")
            raise HTTPException(status_code=400, detail=f"Invalid email: {str(e)}")
        
        # Validate file extension
        if not file.filename or not file.filename.endswith(".csv"):
            logger.warning(f"Invalid file type: {file.filename}")
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        # Read file content
        try:
            content = await file.read()
        except Exception as e:
            logger.error(f"Failed to read file: {str(e)}")
            raise HTTPException(status_code=400, detail="Failed to read file")
        
        # Validate file size (max 10MB)
        file_size = len(content)
        if file_size > 10 * 1024 * 1024:
            logger.warning(f"File too large: {file_size} bytes")
            raise HTTPException(status_code=413, detail="File size exceeds 10MB limit")
        
        # Reset file pointer and read CSV
        try:
            df = pd.read_csv(io.BytesIO(content))
        except Exception as e:
            logger.error(f"Failed to parse CSV: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Invalid CSV file: {str(e)}")
        
        if df.empty:
            raise HTTPException(status_code=400, detail="CSV file is empty")
        
        # Analyze sales data
        analysis = analyze_sales(df)
        
        # Check if analysis failed
        if "error" in analysis:
            logger.error(f"Sales analysis failed: {analysis.get('error')}")
            raise HTTPException(status_code=400, detail=analysis.get('error'))
        
        # Generate AI summary
        summary = generate_summary(df)
        
        # Check if summary generation failed
        if summary.startswith("Error"):
            logger.error(f"Summary generation failed: {summary}")
            raise HTTPException(status_code=500, detail=summary)
        
        # Send email
        email_sent = await send_email(valid_email, summary)
        
        logger.info(f"File processed successfully for {valid_email}")
        
        return {
            "message": "AI summary generated",
            "email_sent": email_sent,
            "analysis": analysis,
            "summary_preview": summary[:200] + "..." if len(summary) > 200 else summary
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in upload: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")