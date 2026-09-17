import pytest
from pages import hover_page
from utils.logger import Logger
from core.assertions import assert_text_contains

@pytest.mark.usefixtures("open_url")

class TestHoverPage:
    
    @pytest.mark.smoke
    def test_hover_page_title(self, driver):
        hover = hover_page.HoverPage(driver)
        assert_text_contains(hover.get_title(), "Hover")
        #assert hover.get_title() == "Section 14 — Hover"
        

    @pytest.mark.regression   
    def test_hover_submenu_items(self, driver):
        hover = hover_page.HoverPage(driver)
        hover.click_hover_section()  # Click to make the hover section visible
        hover.hover_over_element()  # Perform the hover action
        
        # Get the text of submenu items after hovering
        submenu_item1_text = hover.get_hover_submenu_item_text(1)
        submenu_item2_text = hover.get_hover_submenu_item_text(2)
        submenu_item3_text = hover.get_hover_submenu_item_text(3)
        
        # Add assertions here to verify the expected text of submenu items
        assert_text_contains(submenu_item1_text, "Submenu item 1")
        assert_text_contains(submenu_item2_text, "Submenu item 2")
        assert_text_contains(submenu_item3_text, "Submenu item 3")   
        
