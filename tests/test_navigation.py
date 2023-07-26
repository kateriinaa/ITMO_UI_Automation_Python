from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


def test_navigation(browser):

    page_demoqa = DemoQa(driver=browser)
    page_elements = ElementsPage(driver=browser)

    page_demoqa.visit()
    page_demoqa.bth_element.click_force()
    page_elements.refresh()
    browser.refresh()
    page_elements.back()
    time.sleep(3)
    page_demoqa.forward()
    time.sleep(3)
    page_elements.equal_url()
