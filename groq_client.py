from pathlib import Path

from dotenv import load_dotenv
from groq import AsyncGroq

# Load the .env file next to this Python file.
load_dotenv(Path(__file__).with_name(".env"))


PROMPT = """Classify the user's message as billing, technical_support, or other.
Return only the category name."""


async def classify_text(text: str):
    # Reads GROQ_API_KEY loaded from .env or your terminal.
    async with AsyncGroq() as client:
        response = await client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content
