from selenium.webdriver.common.by import By
import time
from ..pages.sbis_main_pagemain_page import MainPage


link = 'https://sbis.ru/'


def test_open_sbis(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'sbisru-Header-ContactsMenu').click()
    time.sleep(10)

