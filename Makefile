DOCKER_COMPOSE = docker-compose
DOCKER_IMAGE = myapp
DOCKER_CONTAINER = myapp_container
DB_CONTAINER = postgres
ENV_FILE = .env

build:
	@echo "Сборка контейнеров..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) build

up:
	@echo "Запуск контейнеров..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) up -d

down:
	@echo "Остановка контейнеров..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) down

clean:
	@echo "Удаление контейнеров и volumes..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) down -v --remove-orphans

logs:
	@echo "Просмотр логов приложения..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) logs -f app

test:
	@echo "Запуск тестов..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) exec app pytest tests/

cron:
	@echo "Запуск cron в контейнере..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) exec app bash -c "cron && tail -f /var/log/cron.log"
