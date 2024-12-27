from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SbisMainPageLocators():
    LOCATOR_SBIS_MAIN_DOWNLOAD = (By.CSS_SELECTOR, '[href="/download"]')


class SbisMainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SbisMainPage, self).__init__(*args, **kwargs)

    def go_to_download_page(self):
        download_page_link = self.find_element(SbisMainPageLocators.LOCATOR_SBIS_MAIN_DOWNLOAD)
        ActionChains(self.browser).scroll_to_element(download_page_link).perform()
        return download_page_link.click()
    