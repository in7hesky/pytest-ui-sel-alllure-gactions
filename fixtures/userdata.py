import pytest
import json


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
