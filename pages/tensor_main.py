from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

block_selector = (By.XPATH, "//*[text()='Сила в людях']")
link_selector = (By.XPATH, "//*[contains(@class,'tensor_ru-Index__link')][@href='/about']")


class TensorMainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def block(self):
        return self.find(block_selector)

    @property
    def link(self):
        return self.find(link_selector)

    def link_click(self):
        WebDriverWait(self.browser, timeout=15).until(EC.element_to_be_clickable(self.link))
        self.click_script(self.link)