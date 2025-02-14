DOCKER_COMPOSE = docker compose -f ./docker-compose.yml

.PHONY: build
build:
	$(DOCKER_COMPOSE) build

.PHONY: up
up: build
	$(DOCKER_COMPOSE) up

.PHONY: down
down:
	$(DOCKER_COMPOSE) down

.PHONY: migrate
migrate:
	cd src && python manage.py migrate

.PHONY: runserver
runserver: migrate
	cd src && python manage.py runserver

.PHONY: pytest
pytest:
	cd src && pytest


