"""Send a standalone sample message to Groq through LiteLLM."""

import os
from pathlib import Path

from dotenv import load_dotenv
from litellm import completion


def main():
    load_dotenv(Path(__file__).with_name(".env"))
    if not os.getenv("GROQ_API_KEY", "").strip():
        raise SystemExit("Set GROQ_API_KEY in .env or your environment before running.")

    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b").strip()
    if not model:
        raise SystemExit("GROQ_MODEL must contain a Groq model ID.")

    response = completion(
        model=f"groq/{model}",
        messages=[{"role": "user", "content": "Say something in one short sentence."}],
        timeout=30,
    )
    content = response.choices[0].message.content
    if not content or not content.strip():
        raise SystemExit("Groq returned no text response.")
    print(content)


if __name__ == "__main__":
    main()
