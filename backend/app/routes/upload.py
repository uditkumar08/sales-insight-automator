from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pandas as pd
from app.services.llm_service import generate_summary
from app.services.email_service import send_email

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), email: str = Form(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV allowed")

    df = pd.read_csv(file.file)

    summary = generate_summary(df)

    send_email(email, summary)

    return {"message": "AI summary sent to email"}