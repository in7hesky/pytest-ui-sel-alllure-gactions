import pytest
import string
import random
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    
    request.cls.driver = driver
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="session")
def valid_user_data():
    filepath = "data/valid_user_data.json"
    try:
        with open(filepath, 'r') as json_file:
            return json.load(json_file)
        
    except FileNotFoundError:
        pytest.fail(f"JSON file not found at {filepath}")
        
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format")
