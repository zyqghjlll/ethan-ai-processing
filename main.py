from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class ClassificationRequest(BaseModel):
    text: str


@app.post("/classify")
async def classify(request: ClassificationRequest):
    return {"category": "billing", "mock": True}
