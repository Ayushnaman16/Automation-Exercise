# import logging
# import os
#
# class LogGen:
#
#     @staticmethod
#     def loggen():
#         log_dir = os.path.join(os.getcwd(), "logs")
#         os.makedirs(log_dir, exist_ok=True)
#
#         log_file = os.path.join(log_dir, "automation.log")
#
#         logging.basicConfig(filename=log_file,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger


import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("automation_logger")
        logger.setLevel(logging.DEBUG)

        # ❗ Prevent duplicate handlers
        if not logger.handlers:

            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s:%(levelname)s:%(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger