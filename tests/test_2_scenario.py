from pages.sbis_contacts_page import ContactsPage
from utilities.config import Config


def test_change_region_in_sbis(browser):
    url = f"{Config.BASE_URL}/contacts"
    sbis_contacts_page = ContactsPage(browser, url)
    sbis_contacts_page.open_site()
    sbis_contacts_page.should_be_my_region()
    sbis_contacts_page.must_have_partners()
    sbis_contacts_page.change_region()
    