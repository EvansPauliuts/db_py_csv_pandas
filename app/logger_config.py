import logging


def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler('query_log.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
