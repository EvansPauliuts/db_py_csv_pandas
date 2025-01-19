import logging
from datetime import datetime
from zoneinfo import ZoneInfo


class LoggerFormatter(logging.Formatter):
    def format(self, record):
        tz = ZoneInfo('Europe/Minsk')
        record.asctime = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

        if record.levelname == 'INFO' and record.message == 'START_LOGGER':
            return f'------------- {record.asctime} -------------'

        log_message = f'{record.asctime} - {record.levelname} - {record.message}'
        return log_message


def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)

    formatter = LoggerFormatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler('query_log.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
