import httpx, os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasa/consultaTasa"
BASE_URL_EXCHANGE = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasasinteres/consultaTasasInteres"

HEADERS = {
    "X-IBM-Client-Id": os.getenv('CLIENT_ID_RATE'),
    "Authorization": f"Bearer {os.getenv('BEARER_TOKEN_RATE')}",
    "Content-Type": "application/json"
}

HEADERS_EXCHANGE = {
    "X-IBM-Client-Id": os.getenv('CLIENT_ID_CHANGE'),
    "Authorization": f"Bearer {os.getenv('BEARER_TOKEN_CHANGE')}",
    "Content-Type": "application/json"
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