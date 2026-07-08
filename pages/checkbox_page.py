

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
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
        super().__init__(driver)      # inherits the Basepage constructor and initializes the driver, wait_helpers, and actions attributes
        
        
    def get_title(self) -> str:
        title_element = self.actions.get_text(self.LOCATORS["TITLE"])
        return title_element
    
    def select_all_checkboxes(self) -> None:
        
        self.logger.warning("Checkbox section is not visible, clicking on the checkbox section to make it visible")
        self.actions.perform_click(self.LOCATORS["CHECKBOX_SECTION"])
        
        self.logger.debug("Clicking on the select all checkbox to select all checkboxes")
        self.actions.perform_click(self.LOCATORS["SELECT_ALL_CHECKBOX"])
        
        
    def is_checkbox_selected(self, name: str) -> bool:
        self.logger.info(f"Checking if checkbox '{name}' is selected")
        return self.actions.is_checkbox_selected(self.LOCATORS[name])   
        