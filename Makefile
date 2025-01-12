# Переменные
DOCKER_COMPOSE = docker-compose
DOCKER_IMAGE = myapp
DOCKER_CONTAINER = myapp_container
DB_CONTAINER = postgres
ENV_FILE = .env

# Сборка контейнеров
build:
	@echo "Сборка контейнеров..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) build

# Запуск контейнеров
up:
	@echo "Запуск контейнеров..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) up -d

# Остановка контейнеров
down:
	@echo "Остановка контейнеров..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) down

# Очистка контейнеров (удаление)
clean:
	@echo "Удаление контейнеров и volumes..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) down -v --remove-orphans

# Просмотр логов приложения
logs:
	@echo "Просмотр логов приложения..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) logs -f app

# Запуск тестов
test:
	@echo "Запуск тестов..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) exec app pytest tests/

# Выполнить cron-планировщик
cron:
	@echo "Запуск cron в контейнере..."
	$(DOCKER_COMPOSE) --env-file $(ENV_FILE) exec app bash -c "cron && tail -f /var/log/cron.log"
