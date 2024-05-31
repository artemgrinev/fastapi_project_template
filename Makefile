DC = docker compose
ALEMBIC = docker exec fastapi-app alembic
APP-FILE = docker-compose.yml
APP = fastapi-app

.PHONY: app-build
app-build:
	${DC} -f ${APP-FILE} up --build -d

.PHONY: app-up
app-up:
	${DC} -f ${APP-FILE} up -d

.PHONY: app-down
app-down:
	${DC} -f ${APP-FILE} down
	
.PHONY: app-logs
app-logs:
	docker logs ${APP} -f

.PHONY: alembic-revision
alembic-revision:
	${ALEMBIC} revision --autogenerate -m "init"

.PHONY: alembic-upgrade
alembic-upgrade:
	${ALEMBIC} upgrade head

.PHONY: alembic-downgrade
alembic-downgrade:
	${ALEMBIC} downgrade -1