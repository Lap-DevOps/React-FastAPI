from typing import Any, Dict

from aiohttp import ClientSession


class HTTPClient:
    """
    Initialize the class with the base URL and API key.

    Parameters:
        base_url (str): The base URL for the session.
        api_key (str): The API key for authentication.

    Returns:
        None
    """

    def __init__(self, base_url: str, api_key: str) -> None:
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': api_key},
        )


class CMCHttpClient(HTTPClient):

    async def get_listings(self) -> list[Dict[str, Any]]:
        """
        Asynchronously retrieves a list of the latest cryptocurrency listings.
        """
        async with self._session.get(
                "/v1/cryptocurrency/listings/latest") as resp:
            result = await resp.json()
            return result["data"]

    async def get_currency(self, currency_id: int) -> dict[str, Any]:
        """
        A function to retrieve currency information based on the provided currency ID.

        Parameters:
            currency_id (int): The ID of the currency for which information is to be retrieved.

        Returns:
         dict: The currency data corresponding to the provided currency ID.
        """
        async with self._session.get(
                "/v2/cryptocurrency/quotes/latest",
                params={"id": currency_id}) as resp:
            result = await resp.json()
            return result["data"][str(currency_id)]
