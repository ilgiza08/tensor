from pages.sbis_contacts_page import ContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage
from utilities.config import Config


def test_can_go_to_the_tensor_site(browser):
    url = f"{Config.BASE_URL}/contacts"
    sbis_contacts_page = ContactsPage(browser, url)
    sbis_contacts_page.open_site()
    sbis_contacts_page.click_on_the_banner()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    tensor_main_page = TensorMainPage(browser, browser.current_url)
    tensor_main_page.contains_a_block_about_the_team()
    tensor_main_page.go_to_about_page()
    tensor_about_page = TensorAboutPage(browser, browser.current_url)
    tensor_about_page.should_be_about_page()
    tensor_about_page.should_be_the_same_img_size()
    

   



