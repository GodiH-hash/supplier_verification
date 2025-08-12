import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_risk(comment):
    prompt = f"Rate the business risk of the following supplier comment from 1 (very low) to 10 (very high):\n\n'{comment}'\n\nOnly return the number."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10
    )
    return response.choices[0].message.content.strip()
