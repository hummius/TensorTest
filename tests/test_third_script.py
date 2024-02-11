from pages.sbis_main import  SbisMainPage
from pages.sbis_download_page import SbisDownloadPage
from utils import download_utilit


def test_download_page(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_page.get_download_page()


def test_download_file(browser):
    download_page = SbisDownloadPage(browser)
    download_page.click_plugin()
    download_utilit.dir_create()
    download = download_page.download_plugin()
    download_page.download_click(download)
    name = download_page.get_file_name(download)
    assert download_utilit.download_check(name)


def test_file_size(browser):
    download_page = SbisDownloadPage(browser)
    download = download_page.download_plugin()
    name = download_page.get_file_name(download)
    size = download_page.get_file_size(download)
    assert download_utilit.file_size_check(name, size)
    download_utilit.file_delete(name)