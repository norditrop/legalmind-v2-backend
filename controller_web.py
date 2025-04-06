
from fastapi import APIRouter, Request, HTTPException
from app.utils import perform_web_search
from app.config import settings

router = APIRouter()

@router.get("/web/search")
async def web_search(query: str, request: Request):
    try:
        results = await perform_web_search(query, settings.WEB_API_KEY)
        return {"success": True, "query": query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
