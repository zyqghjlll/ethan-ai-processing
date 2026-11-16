from fastapi import FastAPI, HTTPException
import logging

from groq import GroqError, NotFoundError
from pydantic import BaseModel

from groq_client import classify_text

logger = logging.getLogger(__name__)

app = FastAPI()

class ClassificationRequest(BaseModel):
    text: str


@app.post("/classify")
async def classify(request: ClassificationRequest):
    try:
        category = await classify_text(request.text)
        return {"category": category}
    except NotFoundError as exc:
        logger.exception("Groq resource not found")
        raise HTTPException(
            status_code=502,
            detail="Groq could not find the requested resource. Check the model name and access.",
        ) from exc
    except GroqError as exc:
        logger.exception("Groq request failed")
        raise HTTPException(
            status_code=502,
            detail="The Groq request failed. Check the server traceback for details.",
        ) from exc
