from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": ""})

@app.post("/", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text in **3 bullet points**:\n\n{text}",
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            summary = response.json().get("response", "No summary generated.")
        else:
            summary = f"Error: {response.text}"
    except requests.exceptions.ConnectionError:
        summary = "Error: Could not connect to Ollama server. Make sure it's running at localhost:11434"
    
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "original_text": text})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7860)
