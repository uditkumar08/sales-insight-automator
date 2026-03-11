import pandas as pd

def analyze_sales(df):

    total_revenue = df["Revenue"].sum()

    top_region = df.groupby("Region")["Revenue"].sum().idxmax()

    top_product = df.groupby("Product_Category")["Revenue"].sum().idxmax()

    return {
        "total_revenue": total_revenue,
        "top_region": top_region,
        "top_product": top_product
    }