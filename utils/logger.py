import logging

class Logger:

    def __init__(self, name =__name__):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
        
logging.basicConfig(
    filename="framework.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
    

#Cheatsheet for using logger in different files:
""" logger.py
    creates logger object

BasePage
    self.logger = logger

CheckboxPage
    self.logger.info(...)

Tests
    import logger
    logger.info(...) """
    
   #Logger to write logs to a file
   
   