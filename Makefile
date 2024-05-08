DC = docker compose
ALEMBIC = docker exec fastapi-app alembic
APP = docker-compose.yml

.PHONY: app-up
app-up:
	${DC} -f ${APP} up -d

.PHONY: app-down
app-down:
	${DC} -f ${APP} down

.PHONY: alembic-revision
alembic-revision:
	${ALEMBIC} revision --autogenerate -m "init"

.PHONY: alembic-upgrade
alembic-upgrade:
	${ALEMBIC} upgrade head

.PHONY: alembic-downgrade
alembic-downgrade:
	${ALEMBIC} downgrade -1