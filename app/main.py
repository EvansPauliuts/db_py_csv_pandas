import os
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from database import get_db_connection
from query_data import queries
from logger_config import setup_logger

logger = setup_logger()


def create_data_directory(path='data'):
    if not os.path.exists(path):
        os.makedirs(path)


def get_current_timestamp():
    return datetime.now(tz=ZoneInfo('Europe/Minsk')).strftime('%Y-%m-%d_%H-%M-%S')


def save_dataframe_with_custom_delimiter(df, file_csv):
    df.to_csv(file_csv, index=False, sep=',')

    with open(file_csv, 'r') as file:
        content = file.read()

    content = content.replace(',', '%|%')

    with open(file_csv, 'w') as file:
        file.write(content)


def process_query(query_info, connection):
    query = query_info.get('query')
    file_name = query_info.get('name', 'unknown_query')

    if not query:
        logger.warning(f'Запрос для {file_name} не найден.')
        logger.error(f'Запрос с именем {file_name} не был найден или некорректен.')
        return

    logger.info(f'Запрос: {query}')

    try:
        df = pd.read_sql(query, connection)
        logger.info(f'Получено данных: {len(df)} строк')

        if not df.empty:
            current_date = get_current_timestamp()
            file_csv = f'data/{file_name}_{current_date}.csv'
            save_dataframe_with_custom_delimiter(df, file_csv)
            logger.info(f'Файл {file_csv} успешно сохранен с разделителем "%|%".')
        else:
            logger.warning(f'Запрос {file_name} не вернул данных, файл не сохранен.')

    except Exception as e:
        logger.error(f'Ошибка выполнения запроса {file_name}: {e}', exc_info=True)


def query_and_save_to_csv():
    try:
        create_data_directory()

        connection = get_db_connection()
        logger.info('START_LOGGER')

        for query_info in queries:
            process_query(query_info, connection)

        connection.close()

    except Exception as e:
        logger.error(
            f'Ошибка при подключении к базе данных или выполнении запросов: {e}',
            exc_info=True,
        )


if __name__ == '__main__':
    query_and_save_to_csv()
