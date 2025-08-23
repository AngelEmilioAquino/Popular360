from fastapi import APIRouter
from app.routers.utils.client import get_exchange_rate

router = APIRouter(prefix="/cambio", tags=["Tasas de Cambio"])

@router.get("/")
async def get_change():
    return await get_exchange_rate()