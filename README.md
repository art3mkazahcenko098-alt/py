# Task Manager API

Fullstack-ready FastAPI backend: PostgreSQL + SQLAlchemy + Alembic, JWT auth with RBAC, Celery + Redis, Docker Compose, GitHub Actions CI.

## Run locally

```bash
cp .env.example .env
docker compose up --build
```

API docs: http://localhost:8000/docs

## Migrations

```bash
docker compose exec api alembic upgrade head
```

## Tests

```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest -q
```

## Admin user

Create an admin directly in DB or promote an existing user:

```sql
UPDATE users SET role = 'admin' WHERE email = 'admin@example.com';
```
