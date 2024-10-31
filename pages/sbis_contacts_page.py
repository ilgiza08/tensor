from .base_page import BasePage
from selenium.webdriver.common.by import By


class SbisContactsPageLocators():
    LOCATOR_SBIS_CONTACTS_LOGO = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
    LOCATOR_SBIS_CONTACTS_MY_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')


class ContactsPage(BasePage):

    def click_on_the_banner(self):
        return self.find_element(SbisContactsPageLocators
                                 .LOCATOR_SBIS_CONTACTS_LOGO, time=1).click()
    
    def should_be_my_region(self):
        my_region = self.find_element(SbisContactsPageLocators
                                      .LOCATOR_SBIS_CONTACTS_MY_REGION).text
