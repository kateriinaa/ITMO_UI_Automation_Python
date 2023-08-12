from pages.elements_page import ElementsPage
import time
import allure
import pytest


@allure.feature('Elements page')
@allure.story('Checking visibility')
@allure.severity(allure.severity_level.NORMAL)
def test_visible_btn_sidebar(browser):

    page = ElementsPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    # page.sidebar_btn.click()
    time.sleep(3)
    assert page.sidebar_textbox.visible()


@allure.feature('Elements page')
@allure.story('Checking visibility')
@allure.severity(allure.severity_level.NORMAL)
def test_not_visible_btn_sidebar(browser):

    page = ElementsPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    assert page.btn_sidebar_first_checkbox.visible()
    page.sidebar_btn.click()
    time.sleep(2)
    assert not page.btn_sidebar_first_checkbox.visible()
