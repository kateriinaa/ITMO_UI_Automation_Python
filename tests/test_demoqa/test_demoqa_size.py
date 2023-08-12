from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time
import allure
import pytest


@allure.feature('Demoqa page')
@allure.story('Checking window size')
@allure.severity(allure.severity_level.NORMAL)
def test_size(browser):

    page_demoqa = DemoQa(driver=browser)

    if page_demoqa.code_status() != 200:
        pytest.skip(reason=f'Page {page_demoqa.base_url} is unavailable')

    page_demoqa.visit()
    browser.set_window_size(300, 1000)
    time.sleep(3)
    browser.set_window_size(1000, 1000)
    time.sleep(3)


@allure.feature('Demoqa page')
@allure.story('Checking window size')
@allure.severity(allure.severity_level.NORMAL)
def test_visible_nav_bar(browser):

    page_elements = ElementsPage(driver=browser)

    if page_elements.code_status() != 200:
        pytest.skip(reason=f'Page {page_elements.base_url} is unavailable')

    page_elements.visit()
    assert not page_elements.nav_bar.visible()
    browser.set_window_size(767, 1000)
    assert page_elements.nav_bar.visible()