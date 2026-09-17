import pytest
from pages import button_page
from utils.logger import Logger
logger = Logger() 

@pytest.mark.usefixtures("open_url")
@pytest.mark.regression

class TestButtonPage:
    def test_button_page_title(self, driver):
        button = button_page.ButtonPage(driver)
        logger.info("Verifying the title of the button page")
        assert button.get_title() == "Section 2 — Buttons"
        
    def test_single_click_button(self, driver):
        button = button_page.ButtonPage(driver)
        logger.info("Text before clicking the single click button: " + button.get_result_text("SINGLE_CLICK_RESULT"))
        logger.info("Clicking on the single click button")
        button.single_click_button()
        assert button.get_result_text("SINGLE_CLICK_RESULT") == "Single clicked!"
        
    def test_double_click_button(self, driver):
        button = button_page.ButtonPage(driver)
        logger.info("Text before double clicking the double click button: " + button.get_result_text("DOUBLE_CLICK_RESULT"))
        logger.info("Double clicked!")
        button.double_click_button()
        assert button.get_result_text("DOUBLE_CLICK_RESULT") == "Double clicked!"
        
    def test_right_click_button(self, driver):
        button = button_page.ButtonPage(driver)
        logger.info("Right clicking on the right click button")
        button.right_click_button()
        assert button.get_result_text("RIGHT_CLICK_RESULT") == "Right click captured (context menu blocked)"
        
    def test_button_section_visible(self,driver):
        button = button_page.ButtonPage(driver)
        
        logger.info("Checking if the button section is visible")
        assert button.is_button_section_visible(timeout=10)
            
    