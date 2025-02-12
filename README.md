# Python monorepo experiments

This branch contains monorepo implementation with `uv`.

To run apps locally use:

```
uv run uvicorn apps.app1.src.main:app --host 0.0.0.0 --port 8001 &
uv run uvicorn apps.app2.src.main:app --host 0.0.0.0 --port 8002 &
uv run uvicorn apps.app3.src.main:app --host 0.0.0.0 --port 8003 &
```

# Build docker image

```
docker build --progress=plain --build-arg APPLICATION=app1 -t service_1 .
docker build --progress=plain --build-arg APPLICATION=app2 -t service_2 .
docker build --progress=plain --build-arg APPLICATION=app3 -t service_3 .
```

`APPLICATION` must be name of one of app under `apps` directory, container name and tag could be any

# Run docker image

```
docker run -p 8000:8000 -e POSTGRES_USER=USER -e ..... -it service_1
docker run -p 8000:8000 -e POSTGRES_USER=USER -e ..... -it service_2
docker run -p 8000:8000 -e POSTGRES_USER=USER -e ..... -it service_3
```

# Dependencies management:

### Add external dependency

To an application:

```
uv add --project apps/app3 fastapi
```

To an another package:

```
uv add --project packages/pkg-requests httpx
```

### Add internal dependency

To an application

```
uv add --project apps/app3 ./packages/pkg-settings/
```

To an another package:

```
uv add --project packages/pkg-requests ./packages/pkg-settings
```

### Locking

Whole project uses single lockfile `uv.lock`. Per-app lock-files should not be added to repo and not used during build.
To regenerate lock-file in the project root use command

```
uv lock
```
