from .base_page import BasePage
from selenium.webdriver.common.by import By
import urllib.request
import os

class SbisDownloadPageLocators():
    LOCATOR_SBIS_DOWNLOAD_LINK = (By.XPATH, '//h3[text()="Веб-установщик "]/../following-sibling::div//a')
    # //h3[text()="Веб-установщик "]/../following-sibling::div//a - link download


class SbisDownloadPage(BasePage):

    def compare_file_size(self):
        link = self.find_element(SbisDownloadPageLocators.LOCATOR_SBIS_DOWNLOAD_LINK)
        url = link.get_attribute("href")
        destination = 'sbisplugin-setup-web.exe'
        urllib.request.urlretrieve(url, destination)

        file = os.stat('sbisplugin-setup-web.exe')
        file_size = round(file.st_size*(10**(-6)), 2)

        text_in_link = link.text
        expected_size = ''.join(filter(lambda x: (x.isdigit() or x == '.'), text_in_link))

        assert file_size == expected_size, f'the downloaded file size does not match, expected {expected_size}, file size = {file_size} '


