from fastapi import FastAPI
from routes import investigation_router

app = FastAPI(
    title="LegalMind Investigador API",
    description="API para busca inteligente, análise de estratégias e captação de modelos de negócios jurídicos e administrativos lucrativos.",
    version="1.0.0"
)

app.include_router(investigation_router, prefix="/investigation")

@app.get("/")
def root():
    return {"message": "LegalMind Investigador API ativa."}