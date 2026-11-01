import time
from typing import Any
_cache: dict[str, dict] = {}

def get_from_cache(key: str)-> Any:
    if key not in _cache:
        return None
    entry = _cache[key]
    if time.time() - entry["timestamp"] > entry["ttl"]:
        del _cache[key]
        return None
    return entry["data"]

def set_in_cache(key: str, value, ttl: int):
    _cache[key] = {
        "data": value,
        "ttl": ttl,  # Cache for 1 hour
        "timestamp": time.time()
    }

def clear_cache():
    _cache.clear()  