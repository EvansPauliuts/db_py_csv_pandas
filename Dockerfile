FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем cron
RUN apt-get update && apt-get install -y cron python3

# Создаем директорию для данных, если её нет
RUN mkdir -p /app/data

# Устанавливаем права доступа для директории /app/data
RUN chmod 777 /app/data

# Копируем crontab файл и скрипт для запуска задачи
COPY crontab /etc/cron.d/my-cron-job
COPY app/run_task.sh /app/run_task.sh

# Создаем директорию и файл для логов cron
RUN mkdir -p /var/log && touch /var/log/cron.log

# Применяем права и запускаем cron
RUN chmod 0644 /etc/cron.d/my-cron-job
RUN chmod +x /app/run_task.sh
RUN crontab /etc/cron.d/my-cron-job

# Запускаем cron в фоновом режиме
CMD cron && tail -f /var/log/cron.log
