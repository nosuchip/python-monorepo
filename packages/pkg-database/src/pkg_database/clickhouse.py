from pkg_settings.clickhouse import ClickHouseSettings

def get_clickhouse_connection_string():
    settings = ClickHouseSettings()
    return f"clickhouse://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.database}"
