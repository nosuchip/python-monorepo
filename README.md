# Python monorepo experiments

This branch contains pdm-related experiments. Each package/app initialized with `pdm init`, packages make installabel/buildable.

# Dependencies

- apps1:
  - fastapi
  - pkg-database
  - pkg-settings
- app2:
  - fastapi
  - pkg-requests
- app3:
  - fastapi
  - pkg-settings

# Build docker
```shell
docker build --build-arg APPLICATION=app1 -f etc/docker/Dockerfile .
```

# Run docker
```shell
docker run -it <image-id> pdm run uvicorn main:app --host 0.0.0.0 --port 8080
```
