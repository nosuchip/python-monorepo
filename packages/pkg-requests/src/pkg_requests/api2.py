import httpx
from pkg_settings.api import APISettings

def fetch_public_api_2():
    settings = APISettings()
    response = httpx.get(f"{settings.public_api_2}/users")
    return response.json()
