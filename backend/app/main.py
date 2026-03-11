from fastapi import FastAPI
from app.routes import upload

app = FastAPI(
    title="Sales Insight Automator",
    description="AI powered sales report generator"
)

app.include_router(upload.router)

@app.get("/")
def home():
    return {"message": "API running"}