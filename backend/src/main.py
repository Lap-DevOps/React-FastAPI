from fastapi import FastAPI

from backend.src.router import router as currency_routes

app = FastAPI()

app.include_router(currency_routes)
