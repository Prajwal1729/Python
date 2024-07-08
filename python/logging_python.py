# Logging:Python import logging is a powerful tool for debugging and troubleshooting code. By default,
#  Python will log all messages to the standard output stream. However, 
# it is also possible to configure Python to log messages to a file, or even to a remote server.

import logging
import logging.config
import traceback
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')

# logging.debug("This is a debug message")
# logging.info("This is a info message")

# logging.warning("This is a warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")

# import helper

logger = logging.getLogger(__name__)

# create handler:
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format:
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is warning")
logger.error("This is a error")

logging.config.fileConfig('logging.conf')
logger.debug("This is debug message")

# try:
#     a = [3,4,5,6,6]
#     val = a[34]
# # except Exception as e:
# #     print(e)

# except:
#     # logging.error("e,exc_info=True")
#     logging.error("The error is %s",traceback.format_exc())


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log',maxBytes=2000,backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello, future!")



