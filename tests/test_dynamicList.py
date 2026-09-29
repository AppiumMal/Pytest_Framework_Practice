import pytest
from core.assertions import assert_text_contains
from pages import dynamicList_page
from utils.logger import Logger
logger = Logger() # tests does not inherit from BasePage, so we need to create a logger instance here


@pytest.mark.usefixtures("open_url")
def test_dynamic_list (driver): 
    dynamic_list = dynamicList_page.DynamicListPage(driver)
    
    logger.info("Verifying the title of the dynamic list page")
    assert_text_contains(dynamic_list.get_title(), "Dynamic List")
    
   
    
    initial_count = dynamic_list.get_items_count()
    logger.info(f"Initial count of items in the list: {initial_count}")
    
    logger.info("Adding an item to the list")
    dynamic_list.add_item()
    new_count = dynamic_list.get_items_count()
    logger.info(f"Count of items after adding an item: {new_count}")
    #assert new_count == initial_count 
    
    
    logger.info("Removing an item from the list")
    dynamic_list.remove_item()
    final_count = dynamic_list.get_items_count()
    logger.info(f"Count of items after removing an item: {final_count}")
    assert final_count == initial_count
    