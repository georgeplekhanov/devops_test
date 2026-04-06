# DevOps Engineer Technical Task

## How to run

```bash
git clone https://github.com/georgeplekhanov/devops_test.git
cd devops_test
docker compose up -d
```

## How to test

```bash
curl http://localhost:5000/
curl http://localhost:5000/task
curl http://localhost:5000/task-redis
```

## How to check logs

```bash
docker compose logs -f app
docker compose logs -f worker
docker compose logs -f worker-redis
```

Mounted log files:

```bash
tail -f logs/worker-redis.log
```

## How to stop

```bash
docker compose down
```

## How it works

### I added comments to the files to explain the main parts

You can read them in the files:

App:
- [app/app.py](app/app.py)
- [app/Dockerfile](app/Dockerfile)
- [app/entrypoint.sh](app/entrypoint.sh)

Worker:
- [worker/worker.py](worker/worker.py)
- [worker/Dockerfile](worker/Dockerfile)

Worker-redis:
- [worker-redis/worker_redis.py](worker-redis/worker_redis.py)
- [worker-redis/Dockerfile](worker-redis/Dockerfile)

Docker Compose:
- [docker-compose.yml](docker-compose.yml)

Environment variables:
- [env](env)

CI:
- [.github/workflows/build-app-image.yml](.github/workflows/build-app-image.yml)

---

Docker Compose in this project starts 4 containers:

1. `app`
2. `worker`
3. `worker-redis`
4. `redis`

The app has 2 task handlers:

1. `/task`
`app` sends request directly to `worker` over http in sync way.

2. `/task-redis`
`app` sends task to `redis` using pub/sub and `worker-redis` receives it with subscribe and processes it in async way.

It uses one Docker network, so containers can access each other by service name:

- `app`
- `worker`
- `worker-redis`
- `redis`

This works through Docker bridge network and internal DNS.

## What was added

- Added Dockerfiles for `app`, `worker` and `worker-redis`
- Added custom entrypoint for `app`
- Added environment variables through `env`
- Added Redis between `app` and `worker-redis`
- Added mounted logs directory for `worker-redis`
- Added `gunicorn` for `app` and `worker` to avoid Flask development server warning
- Added GitHub Actions workflow for pushing images to GHCR

`PYTHONUNBUFFERED=1` is used in Python containers so logs appear immediately in Docker logs.

`depends_on` is used for startup order.

And others - check comments in files.

## CI pipeline

Workflow file:

```text
.github/workflows/build-app-image.yml
```

The pipeline runs on push to `main` branch.

It:

- builds 3 images
- pushes them to `ghcr.io`

Images:

- `ghcr.io/georgeplekhanov/app`
- `ghcr.io/georgeplekhanov/worker`
- `ghcr.io/georgeplekhanov/worker-redis`

Tags:

- `latest`
- `YYYYMMDD-<short_sha>`
