FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y cron python3

RUN mkdir -p /app/data

RUN chmod 777 /app/data

COPY crontab /etc/cron.d/my-cron-job
COPY app/run_task.sh /app/run_task.sh

RUN mkdir -p /var/log && touch /var/log/cron.log

RUN chmod 0644 /etc/cron.d/my-cron-job
RUN chmod +x /app/run_task.sh
RUN crontab /etc/cron.d/my-cron-job

CMD cron && tail -f /var/log/cron.log
