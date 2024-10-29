from .base_page import BasePage
from selenium.webdriver.common.by import By


class SbisMainPageLocators():
    LOCATOR_SBIS_CONTACTS = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu')
    LOCATOR_SBIS_CONTACTS_LIST = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')


class MainPage(BasePage): 
    
    def click_on_the_(self):
        pass

    def check_contacts_popup(self):
        pass
