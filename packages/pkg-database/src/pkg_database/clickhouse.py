from pkg_settings.clickhouse import ClickHouseSettings


def get_clickhouse_connection_string():
    settings = ClickHouseSettings()
    return f"clickhouse://{settings.CLICKHOUSE_USER}:{settings.CLICKHOUSE_PASSWORD}@{settings.CLICKHOUSE_HOST}:{settings.CLICKHOUSE_PORT}/{settings.CLICKHOUSE_DATABASE}"
