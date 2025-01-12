import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Загружаем переменные окружения из .env файла
load_dotenv()

# Чтение переменных окружения
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_NAME = os.getenv('DB_DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Создаем строку подключения для SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаем объект подключения через SQLAlchemy
engine = create_engine(DATABASE_URL)


# Функция для получения соединения
def get_db_connection():
    return engine.connect()
