from pydantic_settings import BaseSettings

class ClickHouseSettings(BaseSettings):
    host: str = "localhost"
    port: int = 8123
    user: str = "default"
    password: str = ""
    database: str = "default"
