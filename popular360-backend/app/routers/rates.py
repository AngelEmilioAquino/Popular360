from fastapi import APIRouter
from app.routers.utils.client import get_interest_rate
from fastapi import HTTPException

router = APIRouter(prefix="/rates", tags=["Rates"])

@router.get("/interest")
async def get_rates():
    try:
        data = await get_interest_rate()
        return {"rates": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


