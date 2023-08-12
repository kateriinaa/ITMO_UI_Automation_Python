from pages.elements_page import ElementsPage
import allure
import pytest


@allure.feature('Elements page')
@allure.story('Checking CSS')
@allure.severity(allure.severity_level.NORMAL)
def test_flex_menu(browser):

    page = ElementsPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    assert page.col.check_css('flex', '0 0 25%')
    assert page.col.check_css('max-width', '25%')
    browser.set_window_size(600, 1000)
    assert page.col.check_css('flex', '0 0 100%')
    assert page.col.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)


