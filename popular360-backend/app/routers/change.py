from fastapi import APIRouter
from app.routers.utils.client import get_exchange_rate
from fastapi import HTTPException
from db_utils import save_exchange_rates

changes_router = APIRouter(prefix="/changes", tags=["Changes"])

@changes_router.get("/exchange")
async def get_change():
    try:
        data = await get_exchange_rate()
        await save_exchange_rates(data)
        return {"exchange_rate": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


