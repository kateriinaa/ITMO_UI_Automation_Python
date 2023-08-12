from pages.elements_page import ElementsPage
import allure
import pytest


@allure.feature('Elements page')
@allure.story('Checking number of buttons')
@allure.severity(allure.severity_level.NORMAL)
def test_find_elements(browser):

    element_page = ElementsPage(driver=browser)

    if element_page.code_status() != 200:
        pytest.skip(reason=f'Page {element_page.base_url} is unavailable')

    element_page.visit()
    assert element_page.btns_first_menu.check_count_elements(9)