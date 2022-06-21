import logging
from os import path, remove


def get_logger():
    if path.isfile("debug.log"):
        remove("debug.log")
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    logger_handler = logging.FileHandler('debug.log')
    logger_handler.setLevel(logging.DEBUG)
    logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    logger_handler.setFormatter(logger_formatter)
    log.addHandler(logger_handler)
    log.info('Настройка логгирования окончена!')
    return log
