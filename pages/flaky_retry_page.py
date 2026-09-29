
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage

class FlakyRetryPage(BasePage):
    LOCATORS = {
        "TITLE": (By.CSS_SELECTOR, "#section-25>h2"),
        "FLAKY_RETRY_SECTION": (By.CSS_SELECTOR, "a[href='#section-25']"),
        "FLAKY_RETRY_BUTTON": (By.ID, "flaky-btn"),
        "FLAKY_RETRY_MESSAGE": (By.CSS_SELECTOR, "[data-testid='flaky-result']"),
        
    }
    
    def __init__(self, driver:WebDriver):
        super().__init__(driver)  # inherits the BasePage constructor and initializes the driver, wait_helpers, and actions attributes
        
        
    def get_title(self) -> str:
        title_element = self.actions.get_text(self.LOCATORS["TITLE"])
        return title_element    
    
    def click_flaky_retry_button(self) -> None:
        self.logger.info(f"Clicking on 'Flaky Retry' button")
        self.actions.retry_action(
            lambda: self.actions.perform_click(self.LOCATORS["FLAKY_RETRY_BUTTON"])
        )

    def get_flaky_retry_message(self) -> str:
        message_element = self.actions.get_text(self.LOCATORS["FLAKY_RETRY_MESSAGE"])
        return message_element    
    
   