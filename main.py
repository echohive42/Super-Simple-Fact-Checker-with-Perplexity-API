from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from config import print_status
from services.perplexity_service import PerplexityService

# Initialize FastAPI app
app = FastAPI(title="Fact Checker")

# Mount templates and static files
templates = Jinja2Templates(directory="templates")

# Initialize services
try:
    perplexity_service = PerplexityService()
    print_status("Services initialized successfully", "success")
except Exception as e:
    print_status(f"Error initializing services: {str(e)}", "error")
    raise

class ContentRequest(BaseModel):
    content: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main page"""
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        print_status(f"Error serving main page: {str(e)}", "error")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/fact-check")
async def fact_check(content_request: ContentRequest):
    """Handle fact checking requests"""
    try:
        print_status(f"Received fact-check request", "info")
        result = await perplexity_service.fact_check(content_request.content)
        return result
    except Exception as e:
        print_status(f"Error processing fact-check request: {str(e)}", "error")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print_status("Starting Fact Checker application", "info")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) 