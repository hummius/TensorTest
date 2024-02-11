from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.action_chains import ActionChains


plugin_selector = (By.XPATH, "//*[@data-id='plugin']")
download_selector = (By.XPATH, "//*[contains(@href,'/win32/sbisplugin')]")

class SbisDownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def plugin_button(self):
        return self.find(plugin_selector)

    def click_plugin(self):
        button = self.plugin_button
        ActionChains(self.browser).move_to_element(button).click(button).perform()
        ActionChains(self.browser).move_to_element(button).click(button).perform()


    def download_plugin(self):
        return self.find(download_selector)

    def get_file_name(self, element):
        return re.search(r"(?<=/win32/)\S+",element.get_attribute("href"))[0]

    def get_file_size(self, element):
        return float(re.search(r"(?<=Exe )\S+", element.text)[0])
    def download_click(self, element):
        ActionChains(self.browser).move_to_element(element).click(element).perform()

