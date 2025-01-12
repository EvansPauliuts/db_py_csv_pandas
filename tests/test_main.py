import pytest
from app.main import get_db_connection, query_and_save_to_csv
from unittest.mock import patch


def test_db_connection():
    connection = get_db_connection()
    assert connection is not None
    connection.close()


@patch('app.main.pd.read_sql')
def test_query_and_save_to_csv(mock_read_sql):
    # Мокаем поведение pandas.read_sql
    mock_read_sql.return_value = 'test_data'

    # Проверим, что функция завершится без ошибок
    try:
        query_and_save_to_csv()
    except Exception as e:
        pytest.fail(f"Test failed with exception {e}")
