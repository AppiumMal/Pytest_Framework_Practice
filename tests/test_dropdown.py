
from pages import dropdown_page
from utils.logger import Logger
logger = Logger() 

class TestDropDownPage:
   

      def test_standard_dropdown(self,driver):  
           dropdown=dropdown_page.DropdownPage(driver)
           logger.info("Verifying the title of the dropdown page")  
           assert dropdown.get_title() == "Section 4 — Dropdowns"
           logger.info("Selecting an option from the standard dropdown")
           dropdown.select_standard_dropdown_option("Green")
        
      def test_multi_select_dropdown(self,driver):
        dropdown=dropdown_page.DropdownPage(driver)
        logger.info("Selecting multiple options from the multi-select dropdown")
        dropdown.select_multi_select_dropdown_options(["Option 1", "Option 2"])
        