from fastapi import FastAPI

app = FastAPI(
    title="CodeMind AI",
    description="AI-powered Codebase Knowledge Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CodeMind AI",
        "status": "Running"
    }