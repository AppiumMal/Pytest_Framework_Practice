
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ButtonPage(BasePage):

    LOCATORS = {
        "TITLE": (By.CSS_SELECTOR, "#section-2>h2"),
        "BUTTON_SECTION": (By.CSS_SELECTOR, "a[href='#section-2']"),
        "SINGLE_CLICK_BUTTON": (By.ID, "single-click-btn"),
        "DOUBLE_CLICK_BUTTON": (By.ID, "double-click-btn"),
        "RIGHT_CLICK_BUTTON": (By.CSS_SELECTOR, "button[data-testid='right-click-btn']"),
        "SINGLE_CLICK_RESULT": (By.CSS_SELECTOR, "p[data-testid='single-click-result']"),
        "DOUBLE_CLICK_RESULT": (By.CSS_SELECTOR, "p[data-testid='double-click-result']"),
        "RIGHT_CLICK_RESULT": (By.CSS_SELECTOR, "p[data-testid='right-click-result']"),
        "TIMER_BUTTON": (By.ID, "start-delay-btn"),
        "ENABLE_BUTTON": (By.ID, "delayed-enable-btn"),
    }

    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # inherits the BasePage constructor and initializes the driver, wait_helpers, and actions attributes

    def get_title(self) -> str:
        title_element = self.actions.get_text(self.LOCATORS["TITLE"])
        return title_element

    def single_click_button(self) -> None:
        self.logger.info(f"Clicking on button")
        self.actions.perform_click(self.LOCATORS["SINGLE_CLICK_BUTTON"])

    def double_click_button(self) -> None:
        self.logger.info(f"Double-clicking on button")
        self.actions.perform_dblclick(self.LOCATORS["DOUBLE_CLICK_BUTTON"])

    def right_click_button(self) -> None:
        self.logger.info(f"Right-clicking on button")
        self.actions.perform_right_click(self.LOCATORS["RIGHT_CLICK_BUTTON"])
        
    def get_result_text(self, result_locator: str) -> str:
        self.logger.info(f"Getting result text for '{result_locator}'")
        return self.actions.get_text(self.LOCATORS[result_locator])   
    
    def is_button_section_visible(self,timeout = 10) -> bool:
        self.logger.info("Checking if the button section is visible")
        self.actions.perform_click(self.LOCATORS["TIMER_BUTTON"])  # Click on the button section to make it visible
        self.logger.info("Waiting for ENABLE_BUTTON to become clickable")
        return self.wait_helpers.wait_for_clickable(self.LOCATORS["ENABLE_BUTTON"], timeout=timeout)  # check enable button is visible after clicking the timer button