from pages.contacts import ContactsPage
from pages.sbis_main import  SbisMainPage
from utils.title_check import check_title


def test_button_contacts(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_page.button_click()


def test_location_contacts(browser):
    contacts_page = ContactsPage(browser)
    assert (contacts_page.location().text == "Владимирская обл."
            and contacts_page.partners_block().is_displayed())


def test_change_location(browser):
    location_page = ContactsPage(browser)
    location_page.location().click()
    location_page.location_change().click()


def test_change_checking(browser):
    change_page = ContactsPage(browser)
    title = change_page.title()
    assert (check_title(browser, title) and "41-kamchatskij-kraj" in browser.current_url
            and change_page.location().text == "Камчатский край"
            and "Камчатка" in change_page.partners_block().text)
