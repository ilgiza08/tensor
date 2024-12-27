from .base_page import BasePage
from selenium.webdriver.common.by import By
import pytest_check as check
from selenium.webdriver.common.action_chains import ActionChains
import time


class SbisContactsPageLocators():
    LOCATOR_SBIS_CONTACTS_LOGO = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
    LOCATOR_SBIS_CONTACTS_MY_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    LOCATOR_SBIS_CONTACTS_PARTNERS = (By.CSS_SELECTOR, '[data-qa="item"]')
    LOCATOR_SBIS_CONTACTS_PARTNERS_SITY = (By.ID, 'city-id-2')
    LOCATOR_SBIS_CONTACTS_KAMCHATKA = (By.CSS_SELECTOR, '[title="Камчатский край"]')


class ContactsPage(BasePage):

    def click_on_the_banner(self):
        return self.find_element(SbisContactsPageLocators
                                 .LOCATOR_SBIS_CONTACTS_LOGO, time=1).click()
    
    def should_be_my_region(self):
        my_region = self.find_element(SbisContactsPageLocators
                                      .LOCATOR_SBIS_CONTACTS_MY_REGION).text
        assert "Республика Башкортостан" == my_region, f"Wrong region, got {my_region}, must be 'Республика Башкортостан'"

    def must_have_partners(self):
        partners = self.find_elements(SbisContactsPageLocators.LOCATOR_SBIS_CONTACTS_PARTNERS_SITY)
        assert partners, "No partners"

    def change_region(self):
        my_region = self.find_element(SbisContactsPageLocators.LOCATOR_SBIS_CONTACTS_MY_REGION)
        my_region.click()
        kamchatka = self.find_element(SbisContactsPageLocators.LOCATOR_SBIS_CONTACTS_KAMCHATKA)
        ActionChains(self.browser).scroll_to_element(kamchatka).perform()
        kamchatka.click()
        time.sleep(5)
        new_region = self.find_element(SbisContactsPageLocators.LOCATOR_SBIS_CONTACTS_MY_REGION).text
        check.equal(new_region, "Камчатский край")

        partners = self.find_element(SbisContactsPageLocators.LOCATOR_SBIS_CONTACTS_PARTNERS_SITY).text
        check.equal(partners, "Петропавловск-Камчатский")
#
        current_url = self.browser.current_url
        check.is_in("kamchatskij", current_url)
#
        title = self.browser.title
        check.is_in("Камчатский край", title)


        

