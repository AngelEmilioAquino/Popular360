import httpx, os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasa/consultaTasa"
BASE_URL_EXCHANGE = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasasinteres/consultaTasasInteres"

HEADERS = {
    "Accept": "application/json",
    "X-IBM-Client-Id": os.getenv('CLIENT_ID_TASA'),
    "Authorization": f"Bearer {os.getenv('BEARER_TOKEN_TASA')}"
}

HEADERS_EXCHANGE = {
    "Accept": "application/json",
    "X-IBM-Client-Id": os.getenv('CLIENT_ID_INTERES'),
    "Authorization": f"Bearer {os.getenv('BEARER_TOKEN_INTERES')}"
}

async def get_interest_rate():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        return response.json()

async def get_exchange_rate():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL_EXCHANGE, headers=HEADERS_EXCHANGE)
        response.raise_for_status()
        return response.json()
