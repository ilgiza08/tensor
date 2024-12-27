from pages.sbis_main_page import SbisMainPage
from pages.sbis_download_page import SbisDownloadPage
from utilities.config import Config


def test_download_plugin(browser):
    url = f"{Config.BASE_URL}"
    sbis_main_page = SbisMainPage(browser, url)
    sbis_main_page.open_site()
    sbis_main_page.go_to_download_page()
    sbis_download_page = SbisDownloadPage(browser, browser.current_url)
    sbis_download_page.compare_file_size()
