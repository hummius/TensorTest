from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.XPATH, "//a[@title='tensor.ru']")
location_selector = (By.XPATH, "//*[@class='sbis_ru-Region-Chooser__text sbis_ru-link'][1]")
partners_selector = (By.XPATH, "//*[contains(@class,'controls-ListViewV__')][1]")
change_selector = (By.XPATH, "//*[@title='Камчатский край']")
title_selector = (By.XPATH, "//title[@class='state-1']")


class ContactsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def button(self):
        return self.find(button_selector)

    def button_click(self):
        self.button.click()

    def partners_block(self):
        return self.find(partners_selector)

    def location(self):
        return self.find(location_selector)

    def location_change(self):
        return self.find(change_selector)

    def title(self):
        return self.find(title_selector)