from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
# only imports selnium's WebDriverWait, expected_conditions, TimeoutException, and NoSuchElementException. It does not import any other modules or classes.

# WaitHelpers holds the custom wait for elements to be visible, clickable, or present in the DOM. It uses Selenium's WebDriverWait and expected_conditions to implement these waits. This class is used in the page objects to ensure that elements are ready for interaction before performing actions on them.

# WaitHelpers holds the custom wait for elements to be visible, clickable, or present in the DOM. It uses Selenium's WebDriverWait and expected_conditions to implement these waits. This class is used in the page objects to ensure that elements are ready for interaction before performing actions on them.

class WaitHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
  
        
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))



