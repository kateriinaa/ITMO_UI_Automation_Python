from pages.textbox import TextBox
import pytest
import allure


@allure.feature('TextBox page')
@allure.story('Checking textbox')
@allure.severity(allure.severity_level.NORMAL)
def test_text_box(browser):

    textbox_page = TextBox(driver=browser)

    if textbox_page.code_status() != 200:
        pytest.skip(reason=f'Page {textbox_page.base_url} is unavailable')

    full_name = 'Alex'
    address = 'Spb'
    textbox_page.visit()
    textbox_page.full_name.send_keys(full_name)
    textbox_page.address.send_keys(address)
    textbox_page.btn_submit.click_force()
    assert textbox_page.name_saved.get_text() == 'Name:' + full_name
    assert textbox_page.current_address_saved.get_text() == 'Current Address :' + address
