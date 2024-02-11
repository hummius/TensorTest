import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="session")
def browser():
    path = (os.path.dirname(os.path.abspath(__file__)) + "/downloads")
    prefs = {"download.default_directory": path}
    options = Options()
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
