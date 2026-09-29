#This page for Practise adding and removing items and asserting on the changing list length.

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DynamicListPage(BasePage):

    LOCATORS = {
        "TITLE": (By.CSS_SELECTOR, "#section-23>h2"),
        "DYNAMIC_LIST_SECTION": (By.CSS_SELECTOR, "a[href='#section-23']"),
        "INPUT_FIELD": (By.CSS_SELECTOR, "[data-testid='list-input']"),
        "ADD_ITEM_BUTTON": (By.ID, "list-add-btn"),
        "REMOVE_ITEM_BUTTON": (By.CSS_SELECTOR, "[data-testid='list-remove-0']"),
        "ITEMS_LIST": (By.CSS_SELECTOR, "ul[data-testid='dynamic-list'] li"),
    }

    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # inherits the BasePage constructor and initializes the driver, wait_helpers, and actions attributes

    def get_title(self) -> str:
        title_element = self.actions.get_text(self.LOCATORS["TITLE"])
        return title_element

    def add_item(self) -> None:
        self.logger.info(f"Clicking on 'Add Item' button")
        self.actions.type_text(self.LOCATORS["INPUT_FIELD"], "New Item")
        self.actions.perform_click(self.LOCATORS["ADD_ITEM_BUTTON"])

    def remove_item(self) -> None:
        self.logger.info(f"Clicking on 'Remove Item' button")
        self.actions.perform_click(self.LOCATORS["REMOVE_ITEM_BUTTON"])
        
    def get_items_count(self) -> int:
        self.logger.info(f"Getting the count of items in the list")
        items = self.actions.find_elements(self.LOCATORS["ITEMS_LIST"])
        #print(type(items)) 
        return len(items)
    
