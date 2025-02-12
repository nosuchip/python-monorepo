from pydantic_settings import BaseSettings


class APISettings(BaseSettings):
    PUBLIC_API_1: str = "https://jsonplaceholder.typicode.com"
    PUBLIC_API_2: str = "https://reqres.in/api"
