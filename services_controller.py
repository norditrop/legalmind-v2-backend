
from fastapi import APIRouter, HTTPException
from utils import list_available_services, get_service_info

router = APIRouter()

@router.get("/services")
async def available_services():
    try:
        return {"services": list_available_services()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/services/{service_name}")
async def service_detail(service_name: str):
    try:
        return get_service_info(service_name)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
