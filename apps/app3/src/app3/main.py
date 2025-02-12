from fastapi import FastAPI
from pkg_settings.api import APISettings
from pkg_settings.clickhouse import ClickHouseSettings
from pkg_settings.postgres import PostgresSettings

app = FastAPI()


@app.get("/settings")
def settings():
    return {
        "postgres": PostgresSettings().dict(),
        "clickhouse": ClickHouseSettings().dict(),
        "api": APISettings().dict(),
    }


@app.get("/name")
def name():
    return {"app": "app3"}
