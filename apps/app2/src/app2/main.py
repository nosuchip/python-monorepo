from fastapi import FastAPI
from pkg_requests.api1 import fetch_PUBLIC_API_1
from pkg_requests.api2 import fetch_PUBLIC_API_2

app = FastAPI()


@app.get("/api1")
def api1():
    return fetch_PUBLIC_API_1()


@app.get("/api2")
def api2():
    return fetch_PUBLIC_API_2()


@app.get("/name")
def name():
    return {"app": "app2"}
