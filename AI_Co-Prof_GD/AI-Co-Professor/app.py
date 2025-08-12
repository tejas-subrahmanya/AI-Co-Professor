from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_dashboard():
    with open("AI_Co_Professor_Dashboard.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
