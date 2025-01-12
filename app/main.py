import os

import pandas as pd
from datetime import datetime
from database import get_db_connection
from query_data import queries


# Функция для выполнения SQL запроса и сохранения результата в CSV
def query_and_save_to_csv():
    try:
        # Проверяем и создаем директорию 'data', если она не существует
        if not os.path.exists('data'):
            os.makedirs('data')

        # Устанавливаем соединение с БД через SQLAlchemy
        connection = get_db_connection()

        # Проходим по всем запросам
        for query_info in queries:
            query = query_info['query']
            file_name = query_info['name']

            # Выполняем запрос и сохраняем результат в DataFrame
            print(f'Запрос: {query}')
            df = pd.read_sql(query, connection)
            print(f'Получено данных: {len(df)} строк')

            # Формируем имя файла с датой и названием запроса
            current_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = f'data/{file_name}_{current_date}.csv'

            # Сохраняем DataFrame в CSV файл
            print(f'Сохраняем в файл: {filename}')
            df.to_csv(filename, index=False)

            # Сохраняем DataFrame в CSV файл
            if not df.empty:
                df.to_csv(filename, index=False)
                print(f'Файл {filename} успешно сохранен.')
            else:
                print(f'Запрос {file_name} не вернул данных, файл не сохранен.')

        # Закрываем соединение с БД после выполнения всех запросов
        connection.close()

    except Exception as e:
        print(f'Произошла ошибка: {e}')


# Главная функция, которая будет вызываться раз в день
if __name__ == '__main__':
    query_and_save_to_csv()
