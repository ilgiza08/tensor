from .base_page import BasePage
from selenium.webdriver.common.by import By


class TensorAboutPageLocators():
    LOCATOR_TENSOR_TEXT = (By.CLASS_NAME, 'tensor_ru-VideoBanner__additions-title')
    LOCATOR_TENSOR_IMGS = (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image")]')


class TensorAboutPage(BasePage):

    def should_be_about_page(self):
        about_link = self.browser.current_url
        assert "https://tensor.ru/about" == about_link, "Page link is not https://tensor.ru/about"
        
    def should_be_the_same_img_size(self):
        imgs = self.find_elements(TensorAboutPageLocators.LOCATOR_TENSOR_IMGS)
        img_params = []
        for img in imgs:
            width = img.get_attribute("width")
            height = img.get_attribute("height")
            if not img_params:
                img_params.append(width)
                img_params.append(height)
            else: 
                assert img_params == [width, height], "Images sizes are not the same"


