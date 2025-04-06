import uvicorn
from fastapi import FastAPI
from config import settings
from routes_investigation import router as investigation_router
from routes_web import router as web_router
import logging

app = FastAPI(title="LegalMind V2 - GPT Estratégico")

app.include_router(investigation_router, prefix="/investigation", tags=["Investigation"])
app.include_router(web_router, prefix="/web", tags=["Web Access"])

@app.on_event("startup")
async def startup_event():
    logging.basicConfig(level=logging.INFO)
    logging.info("Application startup: LegalMind V2 ready to investigate and deploy.")

@app.get("/")
def root():
    return {"message": "LegalMind V2 backend is running."}

if __name__ == "__main__":
    uvicorn.run("startup:app", host="0.0.0.0", port=8000, reload=True)