from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import os

app = FastAPI(
    title="ASIN-HHC-HARMONYOS",
    description="Sovereign Harmony OS Heartbeat & Core Service",
    version="0.1.0"
)

@app.get("/")
async def root():
    return JSONResponse({
        "status": "alive",
        "service": "ASIN-HHC-HARMONYOS",
        "message": "Cathedral-OS Resonance Layer Online",
        "evidence_level": "E1"
    })

@app.get("/health")
async def health():
    return JSONResponse({
        "status": "healthy",
        "uptime": "active",
        "coherence": "nominal"
    })

@app.get("/status")
async def status():
    return JSONResponse({
        "service_id": os.getenv("RENDER_SERVICE_ID", "unknown"),
        "commit": os.getenv("RENDER_GIT_COMMIT", "unknown"),
        "status": "operational"
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))