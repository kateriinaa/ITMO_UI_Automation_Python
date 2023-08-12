from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time
import allure
import pytest


@allure.feature('Demoqa page')
@allure.story('Checking navigation')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation(browser):

    page_demoqa = DemoQa(driver=browser)
    page_elements = ElementsPage(driver=browser)

    if page_demoqa.code_status() != 200:
        pytest.skip(reason=f'Page {page_demoqa.base_url} is unavailable')
    if page_elements.code_status() != 200:
        pytest.skip(reason=f'Page {page_elements.base_url} is unavailable')

    page_demoqa.visit()
    page_demoqa.bth_element.click_force()
    page_elements.refresh()
    browser.refresh()
    page_elements.back()
    time.sleep(3)
    page_demoqa.forward()
    time.sleep(3)
    page_elements.equal_url()
