
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from services.investigation_service import run_investigation

router = APIRouter()

@router.post("/investigate")
async def investigate(data: Dict[str, Any]):
    try:
        result = run_investigation(data)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
