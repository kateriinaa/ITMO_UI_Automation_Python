from pages.demoqa import DemoQa
from pages.radio_button import RadioPage
import pytest
import allure


# @pytest.mark.skip
@allure.feature('Demoqa page')
@allure.story('Checking headings')
@allure.severity(allure.severity_level.NORMAL)
def test_decor(browser):

    page = DemoQa(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    assert page.h5.check_count_elements(6)
    for i in page.h5.find_elements():
        assert i.text is not None


# @pytest.mark.skipif(True, reason='Need to be skipped')
@allure.feature('Demoqa page')
@allure.story('Checking button')
@allure.severity(allure.severity_level.NORMAL)
def test_btn_radio(browser):

    page = RadioPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    page.yes_btn.click_force()
    assert page.text.get_text() == 'Yes'
    page.impressive_btn.click_force()
    assert page.text.get_text() == 'Impressive'
    assert 'disabled' in page.no_btn.get_dom_attribute('class')
