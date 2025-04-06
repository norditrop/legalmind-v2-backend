from fastapi import APIRouter
from fastapi.responses import JSONResponse

investigation_router = APIRouter()

@investigation_router.get("/status")
def investigation_status():
    return JSONResponse(content={"status": "Investigador pronto para executar buscas estratégicas."})

@investigation_router.get("/simulador-modelo")
def simular_modelo_basico():
    return {
        "modelo": "Simulação de captação para serviço de revisão contratual",
        "publico_alvo": "Pessoas físicas endividadas ou com contratos bancários",
        "canal": "Facebook/Instagram Ads com CTA para WhatsApp",
        "fluxo": [
            "Anúncio com dor + benefício + urgência",
            "Conversa automática no WhatsApp (Chatbot ou Resposta Rápida)",
            "Coleta de documentos e qualificação do lead",
            "Fechamento e entrega digital ou presencial"
        ],
        "ticket_medio_estimado": "R$ 250 a R$ 600 por serviço"
    }
