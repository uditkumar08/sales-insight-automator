import pandas as pd
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def analyze_sales(df: pd.DataFrame) -> Dict[str, Any]:
    """Analyze any dataset and extract key metrics
    
    Args:
        df: Pandas DataFrame with data
        
    Returns:
        dict: Metrics and insights
    """
    try:
        # Handle empty dataframe
        if df.empty:
            return {"error": "CSV file is empty"}
        
        # Normalize column names
        df.columns = df.columns.str.lower().str.strip()
        available_cols = df.columns.tolist()
        
        logger.info(f"Analyzing dataset with columns: {available_cols}")
        
        # Identify numeric and categorical columns
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        logger.info(f"Numeric columns: {numeric_cols}, Categorical: {categorical_cols}")
        
        result = {
            "total_rows": len(df),
            "numeric_columns": numeric_cols,
            "categorical_columns": categorical_cols,
            "data_summary": {}
        }
        
        # If we have numeric columns, calculate statistics
        if numeric_cols:
            for col in numeric_cols[:3]:  # Top 3 numeric columns
                stats = {
                    "mean": float(df[col].mean()),
                    "min": float(df[col].min()),
                    "max": float(df[col].max()),
                    "std": float(df[col].std())
                }
                result["data_summary"][col] = stats
        
        # If we have a column that looks like a target/quality/rating
        target_col = None
        for col in numeric_cols:
            if 'quality' in col or 'rating' in col or 'score' in col or 'target' in col:
                target_col = col
                break
        
        if target_col and len(categorical_cols) > 0:
            # Get average target by first categorical column
            group_col = categorical_cols[0]
            result["top_category"] = str(df.groupby(group_col)[target_col].mean().idxmax())
        elif len(numeric_cols) > 0:
            result["primary_metric"] = numeric_cols[0]
            result["average"] = float(df[numeric_cols[0]].mean())
        
        logger.info(f"Analysis completed for dataset with {len(df)} rows")
        return result
        
    except Exception as e:
        logger.error(f"Error analyzing data: {str(e)}", exc_info=True)
        return {
            "error": f"Failed to analyze data: {str(e)}"
        }