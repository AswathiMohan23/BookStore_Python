import logging


def set_logger():
    logging.basicConfig(filename="bookStore_exception.log", level=logging.DEBUG,encoding='utf-8',
                        format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
    logger = logging.getLogger()
    return logger
