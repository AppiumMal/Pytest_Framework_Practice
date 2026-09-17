import pytest
from core.assertions import assert_text_contains
from pages import checkbox_page
from utils.logger import Logger
logger = Logger() # tests does not inherit from BasePage, so we need to create a logger instance here


@pytest.mark.usefixtures("open_url")
class TestCheckboxPage:
    def test_checkbox_page_title(self, driver):
        checkbox = checkbox_page.CheckboxPage(driver)
        logger.info("Verifying the title of the checkbox page")
        assert_text_contains(checkbox.get_title(), "Checkboxes")
        #assert checkbox.get_title() == "Section 3 — Checkboxes & Radio Buttons"
        
"""     def test_select_all_checkboxes(self, driver):
        checkbox = checkbox_page.CheckboxPage(driver)
        logger.info("Selecting all checkboxes")
        checkbox.select_all_checkboxes()
        assert checkbox.is_checkbox_selected("OPTION_A")
        assert checkbox.is_checkbox_selected("OPTION_B")
        assert checkbox.is_checkbox_selected("OPTION_C") """