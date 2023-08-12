from pages.checkbox_page import CheckBoxPage
import allure
import pytest


@allure.feature('CheckBox page')
@allure.story('Checking number of elements')
@allure.severity(allure.severity_level.NORMAL)
def test_count_checkbox(browser):

    checkbox_page = CheckBoxPage(driver=browser)

    if checkbox_page.code_status() != 200:
        pytest.skip(reason=f'Page {checkbox_page.base_url} is unavailable')

    checkbox_page.visit()
    assert checkbox_page.checkbox.check_count_elements(1)
    checkbox_page.btn_expand_all.click()
    assert checkbox_page.checkbox.check_count_elements(17)
    checkbox_page.refresh()
    assert checkbox_page.checkbox.check_count_elements(1)