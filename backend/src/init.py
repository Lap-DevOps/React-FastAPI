from .config import settings
from .http_client import CMCHttpClient

cmc_client = CMCHttpClient(base_url="https://pro-api.coinmarketcap.com",
                           api_key=settings.CMC_API_KEY)
