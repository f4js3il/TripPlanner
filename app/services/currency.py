import httpx
from config.config import CURRENCY_API_KEY
from services.cache import get_from_cache
from services.cache import set_in_cache

async def get_currency_rate(base_currency: str, target_currency: str):

    cache_key = f"{base_currency}_{target_currency}"

    if (cache := get_from_cache(cache_key)) is not None:
            return cache
    
    async with httpx.AsyncClient() as client:

        response = await client.get(f"https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/{base_currency}")
        response.raise_for_status()
        data = response.json()
        rate = data.get("conversion_rates", {}).get(target_currency, 1.0)  # Mock exchange rate for target currency
        if rate is not None: 
            set_in_cache(cache_key,rate, 3600)
        return rate

