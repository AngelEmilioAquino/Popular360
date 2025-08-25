from fastapi import APIRouter
from app.routers.utils.client import get_exchange_rate
from fastapi import HTTPException

changes_router = APIRouter(prefix="/changes", tags=["Changes"])

@changes_router.get("/exchange")
async def get_change():
    try:
        data = await get_exchange_rate()
        return {"exchange_rate": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


