#conftest.py 
# ├─ Fixtures --provides resources,used by tests,returns objects,eg.driver setup
# ├─ Driver lifecycle 
# └─ PyTest Hooks -reacts to Pytest events,used by pytest itself,modifies execution,eg.capture screenshot on failure.

import pytest
from utils.config_loader import ConfigLoader
from core.driver_factory import DriverFactory
from config.config import config as app_config


@pytest.fixture(scope="function")
def open_url(driver):
    """Session fixture that maximizes the browser and navigates to the base URL."""
    loader = ConfigLoader(app_config)
    driver.maximize_window()
    driver.get(loader.get_base_url())
    return driver


@pytest.fixture(scope="session")
def driver():
    print(type(app_config))
    print(app_config)
    factory = DriverFactory(app_config)
    driver = factory.create_driver()
    yield driver
    driver.quit()
