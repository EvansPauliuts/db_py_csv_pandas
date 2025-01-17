#!/bin/bash

source /etc/profile

# Проверка, что PostgresSQL доступен
# until nc -z -v -w30 $DB_HOST $DB_PORT; do
#     echo "Ожидание доступности PostgresSQL..."
#     sleep 5
# done

cd /app

echo "Запуск задачи в $(date)" >> /var/log/cron.log
python3 /app/app/main.py >> /var/log/cron.log 2>&1

sleep 20
echo "Запуск задачи в $(date)" >> /var/log/cron.log
python3 /app/app/main.py >> /var/log/cron.log 2>&1
sleep 20
echo "Запуск задачи в $(date)" >> /var/log/cron.log
python3 /app/app/main.py >> /var/log/cron.log 2>&1
