from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from core.actions import Actions
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
        self.actions.perform_click(self.LOCATORS["CHECKBOX_SECTION"])
        
        self.actions.perform_click(self.LOCATORS["SELECT_ALL_CHECKBOX"])
        
        
    def is_checkbox_selected(self, name: str) -> bool:
        return self.actions.is_checkbox_selected(self.LOCATORS[name])   
        