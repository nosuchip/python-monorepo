# Python monorepo experiments

This branch contains monorepo implementation with `uv`.

To run apps locally use:

```
uv run uvicorn apps.app1.src.main:app --host 0.0.0.0 --port 8001 &
uv run uvicorn apps.app2.src.main:app --host 0.0.0.0 --port 8002 &
uv run uvicorn apps.app3.src.main:app --host 0.0.0.0 --port 8003 &
```
