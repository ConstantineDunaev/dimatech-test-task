#!/bin/sh
echo "Ожидание запуска PostgreSQL..."
sleep 10
alembic upgrade head
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --log-config logging.yaml
