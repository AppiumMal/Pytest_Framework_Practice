import pytest
from core.assertions import assert_text_contains
from pages import  flaky_retry_page
from utils.logger import Logger
logger = Logger()


@pytest.mark.usefixtures("open_url")
def test_flaky_retry(driver):
    flaky_retry=flaky_retry_page.FlakyRetryPage(driver)
    logger.info("Verifying the title of the Flaky Retry page")
    assert flaky_retry.get_title() == "Section 25: Random Fail (Flaky) Elements"
    
@pytest.mark.usefixtures("open_url")
@pytest.mark.smoke
def test_click_flaky_retry_button_and_verify_message(driver):  
    flaky_retry=flaky_retry_page.FlakyRetryPage(driver)  
    logger.info("Clicking on the Flaky Retry button")   
    flaky_retry.click_flaky_retry_button() 
    actual_message = flaky_retry.get_flaky_retry_message()
    logger.warning(f"Verifying the message after clicking the Flaky Retry button: {actual_message}")
    assert actual_message == "Success (passed this run)"