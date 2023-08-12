from pages.textbox import TextBox
import time
import allure
import pytest


@allure.feature('TextBox page')
@allure.story('Checking text box')
@allure.severity(allure.severity_level.NORMAL)
def test_clear(browser):

    textbox = TextBox(driver=browser)

    if textbox.code_status() != 200:
        pytest.skip(reason=f'Page {textbox.base_url} is unavailable')

    textbox.visit()
    textbox.full_name.send_keys('Alex')
    time.sleep(3)
    textbox.full_name.clear()
    time.sleep(3)
    assert textbox.full_name.get_text() == ''
