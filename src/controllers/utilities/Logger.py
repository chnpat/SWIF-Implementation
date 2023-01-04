import logging
import enum


class LogLevel(enum.Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    

def log(message, level=LogLevel.DEBUG):
    logging.basicConfig(filename="../log.txt", level=logging.DEBUG,
                        format="%(name)s - %(levelname)s : %(asctime)s : %(message)s")

    if level == LogLevel.INFO:
        logging.info(message, exc_info=True)
    elif level == LogLevel.WARNING:
        logging.warning(message, exc_info=True)
    elif level == LogLevel.ERROR:
        logging.error(message, exc_info=True)
    elif level == LogLevel.CRITICAL:
        logging.critical(message, exc_info=True)
    else:
        logging.debug(message, exc_info=True)
