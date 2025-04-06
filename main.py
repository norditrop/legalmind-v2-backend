from fastapi import FastAPI
from routes_investigation import investigation_router
from routes_web import web_router
from middleware import setup_middleware

app = FastAPI(title="LegalMind V2 - Backend")

setup_middleware(app)

app.include_router(investigation_router, prefix="/investigation", tags=["Investigation"])
app.include_router(web_router, prefix="/web", tags=["Web Search"])

@app.get("/")
def root():
    return {"message": "LegalMind V2 API is running"}
