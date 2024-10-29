from .base_page import BasePage
from selenium.webdriver.common.by import By


class SbisContactsPageLocators():
    LOCATOR_SBIS_CONTACTS_LOGO = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')


class ContactsPage(BasePage): 
    
    def click_on_the_banner(self):
        return self.find_element(SbisContactsPageLocators
                                 .LOCATOR_SBIS_CONTACTS_LOGO, time=1).click()
        
        
        #return self.browser.find_element(By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
        #assert self.is_element_present(*SbisContactsPageLocators.LOCATOR_SBIS_CONTACTS_LOGO), "Banner link is not presented"

        
