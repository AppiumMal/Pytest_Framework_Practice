import pytest
from pages import checkbox_page


@pytest.mark.usefixtures("open_url")
class TestCheckboxPage:
    def test_checkbox_page_title(self, driver):
        checkbox = checkbox_page.CheckboxPage(driver)
        assert checkbox.get_title() == "Section 3 — Checkboxes & Radio Buttons"
        
    def test_select_all_checkboxes(self, driver):
        checkbox = checkbox_page.CheckboxPage(driver)
        checkbox.select_all_checkboxes()
        assert checkbox.is_checkbox_selected("OPTION_A")
        assert checkbox.is_checkbox_selected("OPTION_B")
        assert checkbox.is_checkbox_selected("OPTION_C")