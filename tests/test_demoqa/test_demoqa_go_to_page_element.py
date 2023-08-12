from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import allure
import pytest


@allure.feature('Demoqa page')
@allure.story('Checking navigation')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_page_element(browser):

    page = DemoQa(driver=browser)
    elements_page = ElementsPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')
    if elements_page.code_status() != 200:
        pytest.skip(reason=f'Page {elements_page.base_url} is unavailable')

    page.visit()
    assert page.equal_url()
    page.bth_element.click_force()
    assert elements_page.equal_url()
