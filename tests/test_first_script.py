from utils.img_match import img_matching
from pages.sbis_main import  SbisMainPage
from pages.contacts import ContactsPage
from pages.tensor_main import TensorMainPage
from pages.tensor_about_page import TensorAboutPage


def test_button_contacts(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_page.button_click()


def test_tensor_banner(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.button_click()


def test_tensor_main_page(browser):
    browser.switch_to.window(browser.window_handles[1])
    tensor_page = TensorMainPage(browser)
    assert tensor_page.block().is_displayed()


def test_tensor_main_about(browser):
    tensor_page = TensorMainPage(browser)
    tensor_page.link_click()
    assert browser.current_url == "https://tensor.ru/about"


def test_tensor_about_work(browser):
    about_page = TensorAboutPage(browser)
    block = about_page.block()
    assert img_matching(browser, block)
