from pages.demoqa import DemoQa
import allure
import pytest

@allure.feature('Demoqa page')
@allure.story('Checking footer')
@allure.severity(allure.severity_level.NORMAL)
def test_check_text(browser):
    page = DemoQa(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    if page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        assert True
    else:
        assert False
