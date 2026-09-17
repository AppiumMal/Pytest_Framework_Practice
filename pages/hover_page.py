from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HoverPage(BasePage):
    LOCATORS = {
        "TITLE": (By.CSS_SELECTOR, "#section-14>h2"),
        "HOVER_SECTION": (By.CSS_SELECTOR, "a[href='#section-14']"),
        "HOVER_ELEMENT": (By.CSS_SELECTOR, "[data-testid='hover-menu-trigger']"),
        "HOVER_SUBMENU": (By.CSS_SELECTOR, "[data-testid='hover-submenu']"),
        "HOVER_SUBMENU_ITEM1": (By.CSS_SELECTOR, "[data-testid='submenu-item-1']"),
        "HOVER_SUBMENU_ITEM2": (By.CSS_SELECTOR, "[data-testid='submenu-item-2']"),
        "HOVER_SUBMENU_ITEM3": (By.CSS_SELECTOR, "[data-testid='submenu-item-3']"),
        "HOVER_TEXT": (By.CSS_SELECTOR, "[data-testid='hover-text']"),
    }

    def __init__(self, driver):
        super().__init__(driver)  # inherits the BasePage constructor and initializes the driver, wait_helpers, and actions attributes

    def get_title(self) -> str:
        title_element = self.actions.get_text(self.LOCATORS["TITLE"])
        return title_element
    
    def click_hover_section(self) -> None:
        self.logger.info("Clicking on the hover section to make it visible")
        self.actions.perform_click(self.LOCATORS["HOVER_SECTION"])
        
    def hover_over_element(self) -> None:
        self.logger.info("Hovering over the element to reveal the hidden text")
        self.actions.perform_hover(self.LOCATORS["HOVER_ELEMENT"])    


    def get_hover_text(self) -> str:
        self.logger.info("Getting the text revealed after hovering over the element")
        return self.actions.get_text(self.LOCATORS["HOVER_SUBMENU"])
  
       #get the text of the submenu items after hovering
    def get_hover_submenu_item_text(self, item_number: int) -> str:
        locator_key = f"HOVER_SUBMENU_ITEM{item_number}"
        self.logger.info(f"Getting the text of submenu item {item_number}")
        return self.actions.get_text(self.LOCATORS[locator_key])