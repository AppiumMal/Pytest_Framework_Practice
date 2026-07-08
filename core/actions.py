from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from core.wait_helpers import WaitHelpers
from utils.logger import Logger
#from driver_factory import factory
#Actions file  will hold and knows all the selenium actions that can be performed in the core module
#import wait_helpers    

class Actions:
    def __init__(self, driver: WebDriver, wait_helpers: WaitHelpers) -> None: #dependency injection of driver and wait_helpers
        self.driver: WebDriver = driver
        self.wait_helpers: WaitHelpers = wait_helpers
        self.logger = Logger()
        self.action_chains = ActionChains(driver)  # Initialize action_chains to None
     

    #method to perform type action
    def type_text(self, locator, text):
        # Implementation for performing type actions
        element = self.wait_helpers.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)


    def perform_click(self, locator):
        # Implementation for performing click actions
        self.logger.info(f"Clicking {locator}")
        element = self.wait_helpers.wait_for_clickable(locator)
        element.click()
        
    def perform_dblclick(self, locator):
        # Implementation for performing double click actions
        self.logger.info(f"Double clicking {locator}")
        element = self.wait_helpers.wait_for_clickable(locator)
        self.action_chains.double_click(element).perform()    
        
    def perform_right_click(self, locator):
        # Implementation for performing right click actions
        self.logger.info(f"Right clicking {locator}")
        element = self.wait_helpers.wait_for_clickable(locator)
        self.action_chains.context_click(element).perform()    
            
        
    def get_text(self, locator):
        # Implementation for getting text from an element
        element = self.wait_helpers.wait_for_visible(locator)
        return element.text
    
    def is_checkbox_selected(self, locator):
        # Implementation for checking if a checkbox is selected
        checkbox = self.wait_helpers.wait_for_visible(locator)
        return checkbox.is_selected() 
    
    def is_element_visible(self, locator):
        # Implementation for checking if an element is visible
        try:
            element = self.wait_helpers.wait_for_visible(locator)
            return element.is_displayed()
        except Exception:
            return False
        
    def is_element_clickable(self, locator, timeout=5):
        # Implementation for checking if an element is clickable
        try:
            element = self.wait_helpers.wait_for_clickable(locator, timeout=timeout)
            return True
        except Exception:
            return False    