from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="ASIN-HHC-HARMONYOS",
    description="Sovereign Harmony OS Hub - Cathedral-OS Gateway",
    version="0.3.0"
)

templates = Jinja2Templates(directory="templates")

class ResonanceRequest(BaseModel):
    glyph1: str
    glyph2: str
    description: Optional[str] = "Compute coherence between two glyphs"

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "ASIN-HHC-HARMONYOS Hub"})

@app.get("/cp8-workflow", response_class=HTMLResponse)
async def cp8_workflow(request: Request):
    return templates.TemplateResponse("cp8_workflow.html", {"request": request})

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "ASIN-HHC-HARMONYOS", "version": "0.3.0"}

@app.get("/status")
async def status():
    return {"service_id": os.getenv("RENDER_SERVICE_ID", "unknown"), "commit": os.getenv("RENDER_GIT_COMMIT", "unknown"), "status": "operational"}

@app.post("/resonance/coherence")
async def compute_coherence(req: ResonanceRequest):
    # Placeholder - integrate real math next
    score = 0.78
    return {"coherence": score, "glyph1": req.glyph1, "glyph2": req.glyph2, "message": "Resonance calculated (placeholder - real math coming)"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))