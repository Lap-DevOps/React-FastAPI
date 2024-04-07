from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.src.router import router as currency_routes

app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(currency_routes)
