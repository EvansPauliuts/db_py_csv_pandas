#!/bin/bash

# Загрузить окружение, чтобы cron использовал правильный PATH
source /etc/profile

# Проверка, что PostgresSQL доступен
# until nc -z -v -w30 $DB_HOST $DB_PORT; do
#     echo "Ожидание доступности PostgresSQL..."
#     sleep 5
# done

# Проверка, что cron использует правильный рабочий каталог
cd /app

# Запускать задачу трижды за одну минуту с интервалом 20 секунд
echo "Запуск задачи в $(date)" >> /var/log/cron.log
python3 /app/app/main.py >> /var/log/cron.log 2>&1

# Ожидание перед следующей задачей
sleep 20
echo "Запуск задачи в $(date)" >> /var/log/cron.log
python3 /app/app/main.py >> /var/log/cron.log 2>&1
sleep 20
echo "Запуск задачи в $(date)" >> /var/log/cron.log
python3 /app/app/main.py >> /var/log/cron.log 2>&1
