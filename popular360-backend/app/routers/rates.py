from fastapi import APIRouter
from app.routers.utils.client import get_interest_rate, get_exchange_rate

router = APIRouter(prefix="/tasas", tags=["Tasas de Interés"])

@router.get("/")
async def get_rates():
    return await get_interest_rate()

