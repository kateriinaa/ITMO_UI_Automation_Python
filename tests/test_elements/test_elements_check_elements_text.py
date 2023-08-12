from pages.elements_page import ElementsPage
import allure
import pytest


@allure.feature('Elements page')
@allure.story('Checking elements')
@allure.severity(allure.severity_level.NORMAL)
def test_check_elements(browser):

    page = ElementsPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    assert page.elements_name.get_text() == 'Elements'

    assert page.icon.exist()
    assert page.sidebar_btn.exist()
    assert page.sidebar_textbox.exist()
