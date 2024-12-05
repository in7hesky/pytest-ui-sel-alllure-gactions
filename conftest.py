import pytest
import allure
from allure_commons.types import AttachmentType
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


pytest_plugins = ["fixtures.userdata"]

def pytest_addoption(parser):
    parser.addoption("--browser", 
                     action="store",
                     choices=["chrome", "firefox"],
                     help="Choose browser type")
    
    parser.addoption("--headless", 
                     action="store_true",
                     help="Run in headless mode")

@pytest.fixture
def driver_options(request):
    if request.config.getoption("--browser") == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        options = FirefoxOptions()
        options.add_argument("-width=1920")
        options.add_argument("-height=1080")
        
    if request.config.getoption("--headless"): 
        options.add_argument("--headless")
        
    return options

@pytest.fixture(autouse=True)
def driver(request, driver_options):
    driver = webdriver.Chrome(options=driver_options) \
        if request.config.getoption("--browser") == "chrome" \
        else webdriver.Firefox(options=driver_options)
    
    request.cls.driver = driver
    
    yield driver
    
    driver.quit()

def pytest_exception_interact(node):
    driver = node.instance.driver

    allure.attach(
        body=driver.get_screenshot_as_png(),
        attachment_type=AttachmentType.PNG,
        name='Screenshot',
    )
