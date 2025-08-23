import httpx

BASE_URL = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasa/consultaTasa"
BASE_URL_EXCHANGE = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasasinteres/consultaTasasInteres"

HEADERS = {
    "X-IBM-Client-Id": "4fb65998527971aeb28c1e2423d60847",
    "Authorization": "Bearer AAIgNGZiNjU5OTg1Mjc5NzFhZWIyOGMxZTI0MjNkNjA4NDdDNROjXvwQTvAp-vZcAdOwxiPoaHSO3NiCBv5EhT23AMQ_f4dGGlpc2-CUoiF5dHoNIbK92fXv_VQ0hETgwWt1-_9HH3WA5n3URbS8D2aJJzqpdm3raVpHiPuF4iUKKZ0",
    "Content-Type": "application/json"
}

HEADERS_EXCHANGE = {
    "X-IBM-Client-Id": "91e8532ff7da2b74d507ded56ead938e",
    "Authorization": "Bearer AAIgOTFlODUzMmZmN2RhMmI3NGQ1MDdkZWQ1NmVhZDkzOGU2PKWOnBKHxNbQFPLxfD1jeBa_8GR30Z7F3xLcP1GYPz3PzJVb1QsD4fQMbZG0M16vXYKrxBvSRDVv5bLEDqkISV-iB0KvPzYoV3hXch8_oAo1RO9geXvq13y5eMLO4So",
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