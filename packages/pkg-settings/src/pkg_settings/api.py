from pydantic_settings import BaseSettings

class APISettings(BaseSettings):
    public_api_1: str = "https://jsonplaceholder.typicode.com"
    public_api_2: str = "https://reqres.in/api"
