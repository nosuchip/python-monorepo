from pydantic_settings import BaseSettings

class PostgresSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str = "user"
    password: str = "password"
    database: str = "db"
