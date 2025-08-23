from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import rates, change
from db import database

# Lifespan para manejar conexión y desconexión de la base de datos
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(title="Popular360 API 🚀", version="1.0.0", lifespan=lifespan)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(rates.router)
app.include_router(change.router)

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Bienvenido a Popular360 🚀"}

# Endpoint para probar conexión a la base de datos
@app.get("/test-db")
async def test_db():
    query = "SELECT NOW();"
    result = await database.fetch_one(query)
    return {"database_time": result["now"]}

