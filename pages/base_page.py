from selenium.webdriver.remote.webelement import WebElement
from core.wait_helpers import WaitHelpers
from core.actions import Actions 
class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_helpers = WaitHelpers(driver)
        self.actions = Actions(driver, self.wait_helpers)