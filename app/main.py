import os

import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from database import get_db_connection
from query_data import queries
from logger_config import setup_logger

logger = setup_logger()


def query_and_save_to_csv():
    try:
        if not os.path.exists('data'):
            os.makedirs('data')

        connection = get_db_connection()

        for query_info in queries:
            query = query_info.get('query', None)
            file_name = query_info.get('name', 'unknown_query')

            if not query:
                logger.warning(f'Запрос для {file_name} не найден.')
                logger.error(
                    f'Запрос с именем {file_name} не был найден или некорректен.'
                )
                continue

            logger.info(f'Запрос: {query}')

            try:
                df = pd.read_sql(query, connection)
                logger.info(f'Получено данных: {len(df)} строк')

                current_date = datetime.now(tz=ZoneInfo('Europe/Minsk')).strftime(
                    '%Y-%m-%d_%H-%M-%S'
                )
                filename = f'data/{file_name}_{current_date}.csv'

                logger.info(f'Сохраняем в файл: {filename}')
                df.to_csv(filename, index=False)

                if not df.empty:
                    logger.info(f'Файл {filename} успешно сохранен.')
                else:
                    logger.warning(
                        f'Запрос {file_name} не вернул данных, файл не сохранен.'
                    )

            except Exception as e:
                logger.error(
                    f'Ошибка выполнения запроса {file_name}: {e}', exc_info=True
                )

        connection.close()

    except Exception as e:
        logger.error(
            f'Ошибка при подключении к базе данных или выполнении запросов: {e}',
            exc_info=True,
        )


if __name__ == '__main__':
    query_and_save_to_csv()
