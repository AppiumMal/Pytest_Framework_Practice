import pytest
from utils.config_loader import ConfigLoader
from core.driver_factory import DriverFactory
import config


@pytest.fixture(scope="function")
def open_url(driver):
    """Session fixture that returns the base URL from config_loader."""
    loader = ConfigLoader(config)
    driver.get(loader.get_base_url())
   

@pytest.fixture(scope="session")
def driver():
    factory = DriverFactory(config) 
    driver = factory.create_driver() 
    yield driver
    driver.quit()
    