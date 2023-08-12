from pages.form_page import FormPage
import allure
import pytest


@allure.feature('Form page')
@allure.story('Checking form')
@allure.severity(allure.severity_level.NORMAL)
def test_login_form_validate(browser):

    form_page = FormPage(driver=browser)

    if form_page.code_status() != 200:
        pytest.skip(reason=f'Page {form_page.base_url} is unavailable')

    form_page.visit()
    assert form_page.firstname.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.lastname.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.useremail.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.useremail.get_dom_attribute('pattern') == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    form_page.btn_submit.click_force()
    assert form_page.form.get_dom_attribute('class') == 'was-validated'


