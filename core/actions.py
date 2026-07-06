from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from core.wait_helpers import WaitHelpers
#from driver_factory import factory
#Actions file  will hold and knows all the selenium actions that can be performed in the core module
#import wait_helpers    

class Actions:
    def __init__(self, driver: WebDriver, wait_helpers: WaitHelpers) -> None: #dependency injection of driver and wait_helpers
        self.driver: WebDriver = driver
        self.wait_helpers: WaitHelpers = wait_helpers
     

    #method to perform type action
    def type_text(self, locator:WebElement, text):
        # Implementation for performing type actions
        element = self.wait_helpers.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)


    def perform_click(self, locator):
        # Implementation for performing click actions
        element = self.wait_helpers.wait_for_clickable(locator)
        element.click()
        
        pass
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