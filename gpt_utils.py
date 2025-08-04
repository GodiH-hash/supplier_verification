import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_supplier_risk(comment):
    prompt = (
        f"Rate the risk level of this supplier comment from 1 (low) to 10 (high):\n"
        f"{comment}\n"
        f"Only return the number."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
