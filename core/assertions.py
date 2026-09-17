from selenium.webdriver.support.ui import WebDriverWait

def is_checkbox_selected(driver, checkbox_locator):
    """
    Check if a checkbox is selected.

    :param driver: The WebDriver instance.
    :param checkbox_locator: The locator for the checkbox element.
    :return: True if the checkbox is selected, False otherwise.
    """
    try:
        checkbox_element = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(*checkbox_locator)
        )
        return checkbox_element.is_selected()
    except Exception as e:
        print(f"Error checking checkbox selection: {e}")
        return False
    
    
def assert_text_contains(actual_text,expected_text):
        assert expected_text in actual_text, \
         f"Expected '{expected_text}' in '{actual_text}'"
    
        """
        Assert that the actual text contains the expected text.

        :param actual_text: The actual text to check.
        :param expected_text: The expected text to look for.
        :raises AssertionError: If the actual text does not contain the expected text.
        """
