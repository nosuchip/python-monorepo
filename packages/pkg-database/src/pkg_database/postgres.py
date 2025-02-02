from pkg_settings.postgres import PostgresSettings

def get_postgres_connection_string():
    settings = PostgresSettings()
    return f"postgresql://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.database}"
