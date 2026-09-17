#page objects and locators for dropdown page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from core.actions import Actions
from pages.base_page import BasePage

class DropdownPage(BasePage):
    """Page object for the dropdown page."""

    LOCATORS = {
    "TITLE": (By.CSS_SELECTOR, "#section-4>h2"),
    "DROPDOWN_SECTION": (By.CSS_SELECTOR, "a[href='#section-4']"),
    "STANDARD_DROPDOWN": (By.ID, "standard-select"),
    "STANDARD_DROPDOWN_TEXT": (By.CSS_SELECTOR, "[data-testid='standard-select-result']"),
    "MULTI_SELECT_DROPDOWN": (By.ID, "multi-select"),
    "MULTI_SELECT_DROPDOWN_RESULT": (By.CSS_SELECTOR, "[data-testid='multi-select-result']"),
    "CUSTOM_DROPDOWN": (By.ID, "custom-dropdown-toggle"),
    "CUSTOM_DROPDOWN_OPTIONS": (By.CSS_SELECTOR, "[data-testid='custom-dropdown-menu']"),
    "CUSTOM_DROPDOWN_OPTION1": (By.CSS_SELECTOR, "[data-testid='custom-option-alpha']"),
    "CUSTOM_DROPDOWN_OPTION2": (By.CSS_SELECTOR, "[data-testid='custom-option-beta']"),
    "CUSTOM_DROPDOWN_OPTION3": (By.CSS_SELECTOR, "[data-testid='custom-option-gamma']"),
    "CUSTOM_DROPDOWN_RESULT": (By.CSS_SELECTOR, "[data-testid='custom-dropdown-result']"),
    "DYNAMIC_DROPDOWN": (By.ID, "dynamic-select"),
    "DYNAMIC_DROPDOWN_RESULT": (By.CSS_SELECTOR, "[data-testid='dynamic-select-result']"),
    
    }
  
    def __init__(self, driver):
        super().__init__(driver)  # inherits the BasePage constructor and initializes the driver, wait_helpers, and actions attributes    def get_title(self):


    def get_title(self) -> str:
        title_element = self.actions.get_text(self.LOCATORS["TITLE"])
        return title_element
    
    
    #method to select an option from the standard dropdown
    def select_standard_dropdown_option(self, option_text): 
        self.logger.warning("Dropdown section is not visible, clicking on the dropdown section to make it visible")
        self.actions.perform_click(self.LOCATORS["DROPDOWN_SECTION"])
        
        self.logger.info(f"Selecting option '{option_text}' from the standard dropdown")
        self.actions.perform_click(self.LOCATORS["STANDARD_DROPDOWN"])
        
        dropdown_element = self.wait_helpers.wait_for_visible(self.LOCATORS["STANDARD_DROPDOWN"])
        for option in dropdown_element.find_elements(By.TAG_NAME, "option"):
            if option.text == option_text:
                option.click()
                break
            
    def select_multi_select_dropdown_options(self, options):
        self.logger.warning("Dropdown section is not visible, clicking on the dropdown section to make it visible")
        self.actions.perform_click(self.LOCATORS["DROPDOWN_SECTION"])
        
        self.logger.info(f"Selecting multiple options {options} from the multi-select dropdown")
        multi_select_element = self.wait_helpers.wait_for_visible(self.LOCATORS["MULTI_SELECT_DROPDOWN"])
       # get_multi_select_dropdown_result = Select.select_by_index(multi_select_element, options)
        
               