from fastapi import FastAPI

from src.api.repository import router as repository_router
from src.api.parser import router as parser_router

app = FastAPI(
    title="CodeMind AI",
    description="AI-powered Codebase Knowledge Assistant",
    version="1.0.0"
)

app.include_router(repository_router)
app.include_router(parser_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CodeMind AI",
        "status": "Running"
    }