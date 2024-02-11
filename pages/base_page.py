from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, selector):
        return WebDriverWait(self.browser, timeout=10).until(EC.presence_of_element_located(selector),
                                                       message=f"Can`t find element by selector")

    def click_script(self, selector):
        self.browser.execute_script("arguments[0].click();", selector)