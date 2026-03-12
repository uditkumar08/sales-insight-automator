import google.generativeai as genai
import logging
from app.config import settings
from typing import Optional
import pandas as pd

logger = logging.getLogger(__name__)

# Configure Gemini API
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)

    try:
        # Primary model
        model = genai.GenerativeModel("models/gemini-2.5-flash")
    except Exception:
        # Fallback model
        model = genai.GenerativeModel("models/gemini-2.0-flash")

else:
    model = None
    logger.warning("GEMINI_API_KEY not configured")


def generate_summary(df: pd.DataFrame) -> Optional[str]:
    """
    Generate AI-powered insight using Gemini for any dataset

    Args:
        df: Pandas DataFrame with data

    Returns:
        str: Generated summary text
    """

    try:

        if model is None:
            return "Error: Gemini API key not configured."

        if df.empty:
            return "Dataset is empty. Unable to generate insights."

        # Normalize column names
        df.columns = df.columns.str.lower().str.strip()

        # Limit dataset preview (to avoid token overflow)
        preview_rows = min(30, len(df))

        sample_data = df.head(preview_rows).to_string()

        # Detect column types
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

        # Dataset context
        data_context = f"""
Dataset Overview
----------------
Total Rows: {len(df)}
Total Columns: {len(df.columns)}

Numeric Columns:
{", ".join(numeric_cols[:8]) if numeric_cols else "None"}

Categorical Columns:
{", ".join(categorical_cols[:8]) if categorical_cols else "None"}

Sample Data (first {preview_rows} rows):
{sample_data}
"""

        prompt = f"""
You are a professional data analyst.

Analyze the dataset below and provide a concise analytical report.

Provide the answer in this format:

1️⃣ **Dataset Summary**
- What type of dataset is this?
- What information does it contain?

2️⃣ **Key Insights**
- Identify 3 important patterns or observations.

3️⃣ **Trends / Patterns**
- Mention any relationships, increases, decreases, or anomalies.

4️⃣ **Recommendations**
- Suggest 2 actionable recommendations.

Keep the explanation simple and professional.

{data_context}
"""

        response = model.generate_content(prompt)

        if not response or not response.text:
            return "AI could not generate insights for this dataset."

        logger.info("AI insight generated successfully")

        return response.text

    except Exception as e:

        logger.error(f"Failed to generate summary: {str(e)}", exc_info=True)

        return f"Error generating summary: {str(e)}"