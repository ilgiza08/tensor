from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage():

    #def __init__(self, browser, url, timeout=10):
    #    self.browser = browser
    #    self.url = url
    #    self.browser.implicitly_wait(timeout)

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_site(self): 
        self.browser.get(self.url)

    #def is_element_present(self, how, what):
    #    try:
    #        self.browser.find_element(how, what)
    #    except (NoSuchElementException):
    #        return False
    #    return True

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), 
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.browser,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")