from pages.base_page import BasePage
from selenium.webdriver.common.by import By


button_selector = (By.XPATH, "//li[contains(@class,'sbisru-Header__menu-item-1')]/a")
download_page_selector = (By.XPATH, "//*[@href='/download']")

class SbisMainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("http://sbis.ru")

    @property
    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button.is_displayed()

    def button_click(self):
        self.button.click()

    @property
    def download_page(self):
        return self.find(download_page_selector)

    def get_download_page(self):
        self.browser.get(self.download_page.get_attribute("href"))