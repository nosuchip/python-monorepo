from fastapi import FastAPI
from pkg_database.postgres import get_postgres_connection_string
from pkg_database.clickhouse import get_clickhouse_connection_string
from app1 import __application__

app = FastAPI()


@app.get("/postgres")
def postgres():
    return {"connection": get_postgres_connection_string()}


@app.get("/clickhouse")
def clickhouse():
    return {"connection": get_clickhouse_connection_string()}


@app.get("/name")
def name():
    return {"app": __application__}
