from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from config.config import config as app_config


class DriverFactory:
    def __init__(self, cfg):
        self.config = cfg

    def get_browser(self):
        return self.config["browser"]

    def create_driver(self):
        print(type(self.config))
        print(self.config)
        if self.config["browser"] == "Chrome":
            
            options = Options()

            if self.config.get("headless", True):
               options.add_argument("--headless")
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        elif self.config["browser"] == "Firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(
                f"Unsupported browser: {self.config['browser']}"
            )


factory = DriverFactory(app_config)

