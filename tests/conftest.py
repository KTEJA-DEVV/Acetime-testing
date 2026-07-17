import pytest
import json
import os
from config.browser_config import Browser_config
@pytest.fixture(scope='function')
def context(browser):
    context=browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope='function')
def page(context):
    page=context.new_page()
    yield page
    page.close()

@pytest.fixture(scope='session')
def base_url():
    base_url=Browser_config['base_url']
    return base_url


@pytest.fixture(scope='session')
def load_test_user_data():
    path = os.path.join(os.path.dirname(__file__), "..","test_data", "users.json")
    with open(path, "r") as read_file:
        data = json.load(read_file)
    return data["user_data"][0]



