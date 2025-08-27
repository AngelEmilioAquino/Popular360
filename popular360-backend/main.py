from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import rates, change

app = FastAPI(title="Popular360 API 🚀", version="1.0.0")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(rates.rates_router)
app.include_router(change.changes_router)

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Bienvenido a Popular360 🚀"}


