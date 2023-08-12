from pages.demoqa import DemoQa
import allure


@allure.feature('Demoqa page')
@allure.story('Checking icon')
@allure.severity(allure.severity_level.NORMAL)
def test_site_version(browser):

    page = DemoQa(driver=browser)

    page.visit()
    page.icon.click()
    assert page.equal_url()
    assert page.icon.exist()


