import httpx
from pkg_settings.api import APISettings


def fetch_PUBLIC_API_2():
    settings = APISettings()
    response = httpx.get(f"{settings.PUBLIC_API_2}/users")
    return response.json()
