from .base_page import BasePage
from selenium.webdriver.common.by import By


class TensorMainPageLocators():
    LOCATOR_TENSOR_TEXT = (By.CLASS_NAME, 'tensor_ru-VideoBanner__additions-title')
    LOCATOR_TENSOR_TEAM_BLOCK = (By.XPATH, '//p[text()="Сила в людях"]') 
    LOCATOR_TENSOR_ABOUT_TEAM = (By.XPATH, '//p/a[@href="/about"]')


class TensorMainPage(BasePage): 
    
    #def should_be_tensor_site(self):
    #    header_text = self.find_element(TensorMainPageLocators.LOCATOR_TENSOR_TEXT, time=1).text
    #    assert "А также" == header_text, "error"

    def contains_a_block_about_the_team(self):
        header_text = self.find_element(TensorMainPageLocators.LOCATOR_TENSOR_TEAM_BLOCK).text
        assert "Сила в людях" == header_text, "Can't find a block abot the team"

    def go_to_about_page(self):
        return self.find_element(TensorMainPageLocators.LOCATOR_TENSOR_ABOUT_TEAM).click()


