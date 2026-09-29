import logging
from pathlib import Path
from venv import logger

class Logger:

    def __init__(self, name=__name__):

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.WARNING)

        if not self.logger.handlers:

            Path("logs").mkdir(exist_ok=True)

            file_handler = logging.FileHandler(
                "logs/selenium_tests.log",
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def info(self, msg):
        self.logger.info(msg)
        
    def warning(self, msg):
        self.logger.warning(msg)    