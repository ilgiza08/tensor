from ..pages.sbis_contacts_page import ContactsPage


def test_change_region_in_sbis(browser):
    url = 'https://sbis.ru/contacts'
    sbis_contacts_page = ContactsPage(browser, url)
    sbis_contacts_page.open_site()
    sbis_contacts_page.should_be_my_region()
    sbis_contacts_page.change_region()