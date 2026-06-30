# backend

FastAPI + PostgreSQL + MinIO. Clean architecture.

## Run (Docker)

```bash
docker compose up --build
```

Services:

- backend: http://localhost:4000 (OpenAPI: http://localhost:4000/docs)
- MinIO API: http://localhost:9000
- MinIO Console: http://localhost:9001 (login `flowforge` / `flowforge-secret`)
- Postgres: localhost:5433 (`flowforge` / `flowforge` / db `flowforge`)

The MinIO bucket `flowforge-uploads` is created on first request automatically.
Alembic migrations run on container start.

## Endpoints

```
POST   /api/v1/uploads       multipart/form-data; key: files (1..10 images, <=10 MB each)
GET    /api/v1/uploads/{id}
DELETE /api/v1/uploads/{id}
GET    /health
```

Accepted MIME types: `image/jpeg`, `image/png`, `image/webp`, `image/gif`, `image/svg+xml`, `image/heic`, `image/heif`.

## Layout (clean architecture)

```
app/
  domain/          pure business rules (entities, value objects, exceptions)
  application/     use cases + ports (ObjectStorage, FileRepository)
  infrastructure/  adapters (SQLAlchemy repository, MinIO storage)
  interface/       FastAPI routers, schemas, DI
  core/            settings, config
```

Dependency direction: `interface → application → domain ← infrastructure`.

## Quick smoke test

```bash
curl -F "files=@/path/to/photo.jpg" http://localhost:4000/api/v1/uploads
```
