from fastapi import APIRouter
from app.routers.utils.client import get_interest_rate
from fastapi import HTTPException

rates_router = APIRouter(prefix="/rates", tags=["Rates"])

@rates_router.get("/interest")
async def get_rates():
    try:
        data = await get_interest_rate()
        return {"interest_rate": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

