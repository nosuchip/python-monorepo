from pkg_settings.postgres import PostgresSettings


def get_postgres_connection_string():
    settings = PostgresSettings()
    return f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DATABASE}"
