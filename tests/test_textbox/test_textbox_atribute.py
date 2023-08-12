import allure
from pages.textbox import TextBox


@allure.feature('Check attribute')
@allure.story('Checking placeholder')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):

    page = TextBox(driver=browser)
    page.visit()
    assert page.full_name.get_dom_attribute('placeholder') == 'Full Name'


@allure.feature('Check attribute')
@allure.story('Checking placeholder')
@allure.severity(allure.severity_level.NORMAL)
def test_fail():
    assert 1 == 2

