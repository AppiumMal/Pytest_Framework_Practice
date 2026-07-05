from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from core.wait_helpers import WaitHelpers
from pages.base_page import BasePage



class CheckboxPage(BasePage):
    
    LOCATORS = {
         "TITLE": (By.CSS_SELECTOR, "#section-3>h2"),
         "CHECKBOX_SECTION": (By.CSS_SELECTOR, "a[href='#section-3']"),
         "SELECT_ALL_CHECKBOX": (By.ID, "select-all"),
         "OPTION_A": (By.ID, "check-a"),
         "OPTION_B": (By.ID, "check-b"),
          "OPTION_C": (By.ID, "check-c"),
                 }
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_helpers = WaitHelpers(driver)
        
    def get_title(self) -> str:
        title_element = self.wait_helpers.wait_for_visible(self.LOCATORS["TITLE"])
        return title_element.text 
    def select_all_checkboxes(self) -> None:
        checkbox_section = self.wait_helpers.wait_for_visible(self.LOCATORS["CHECKBOX_SECTION"])
        checkbox_section.click()
        select_all = self.wait_helpers.wait_for_visible(self.LOCATORS["SELECT_ALL_CHECKBOX"])
        select_all.click()
        
    def is_checkbox_selected(self, locator: WebElement) -> bool:
        checkbox = self.wait_helpers.wait_for_visible(locator)
        return checkbox.is_selected()    
        