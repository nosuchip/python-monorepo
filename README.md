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

# New components

### Adding new package

```
uv init --lib ./packages/pkg-data
```

### Adding new service

While UV create apps with just `init` it is recommended to use the same command as for package with just path fixing:

```
uv init --lib ./apps/apps5
```

and then remove from `pyproject.toml` followig tables:

- tool.hatch.build.targets.wheel
- tool.uv.sources
- build-system

It will generate `src`-based code structure. By fact you cant use `uv init ./apps/app5` and just create `src/<SERVICE_NAME>/main.py` manually.

### UV init --lib vs --package

Creating new lib implies package. Creating new package by fact creates the same file structure but main intention is to make something packageable. So for package `pyproject.toml` will contains table `python.script` and for lib - will not. But everything else will be the same.
