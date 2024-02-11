from pages.base_page import BasePage
from selenium.webdriver.common.by import By

block_selector = (By.XPATH, "//div[contains(@class,'About__block3')]")


class TensorAboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def block(self):
        return self.find(block_selector)


