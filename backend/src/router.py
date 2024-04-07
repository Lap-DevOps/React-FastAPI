from fastapi import APIRouter

from backend.src.init import cmc_client

router = APIRouter(
    prefix="/cryptocurrencies"
)


@router.get("/")
async def get_cryptocurrencies():
    """
    Retrieve a list of cryptocurrencies using the CoinMarketCap API.
    """
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_currency(currency_id: int):
    """
    A description of the entire function, its parameters, and its return types.
    """
    return await cmc_client.get_currency(currency_id)
