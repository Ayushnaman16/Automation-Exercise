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

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "automation.log")

        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True
        )

        return logging.getLogger()