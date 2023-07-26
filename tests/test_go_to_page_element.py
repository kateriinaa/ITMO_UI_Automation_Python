from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_element(browser):

    page = DemoQa(driver=browser)
    elements_page = ElementsPage(driver=browser)

    page.visit()
    assert page.equal_url()
    page.bth_element.click_force()
    assert elements_page.equal_url()
