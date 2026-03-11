from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_summary(df):

    data = df.to_string()

    prompt = f"""
    Analyze this sales dataset and produce an executive summary.

    {data}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content