from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TensorMainPageLocators():
    LOCATOR_TENSOR_TEXT = (By.CLASS_NAME, 'tensor_ru-VideoBanner__additions-title')
    LOCATOR_TENSOR_TEAM_BLOCK = (By.XPATH, '//p[text()="Сила в людях"]') 
    LOCATOR_TENSOR_ABOUT_TEAM = (By.XPATH, '//p/a[@href="/about"]')


class TensorMainPage(BasePage):

    def contains_a_block_about_the_team(self):
        header_text = self.find_element(TensorMainPageLocators.LOCATOR_TENSOR_TEAM_BLOCK).text
        assert "Сила в людях" == header_text, "Can't find a block abot the team"

    def go_to_about_page(self):
        about_page_link = self.find_element(TensorMainPageLocators.LOCATOR_TENSOR_ABOUT_TEAM)
        ActionChains(self.browser).scroll_to_element(about_page_link).perform()
        return about_page_link.click()


