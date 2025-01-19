#!/bin/bash

source /etc/profile

cd /app

export TZ="Europe/Minsk"
echo "Запуск задачи в $(date)" >> /var/log/cron.log

python3 /app/app/main.py >> /var/log/cron.log 2>&1