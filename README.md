Создать таблицы:
    docker exec fastapi-app alembic upgrade head

Сгенерировать ревизию:
    docker exec fastapi-app alembic revision --autogenerate -m "init"

docker exec fastapi-app alembic downgrade -1
