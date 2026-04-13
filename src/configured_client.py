import os
from src.external_api import fetch_user

def get_user_from_env(user_id: int) -> dict:
    base_url = os.getenv("API_BASE_URL", "http://defaultapi.com")
    timeout = int(os.getenv("API_TIMEOUT", "5"))
    return fetch_user(user_id, base_url=base_url, timeout=timeout)