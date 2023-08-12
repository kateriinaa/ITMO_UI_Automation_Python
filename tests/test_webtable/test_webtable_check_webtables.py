from pages.webtables import WebtablesPage
import time
import allure
import pytest


@allure.feature('WebtablesPage page')
@allure.story('Checking registration form')
@allure.severity(allure.severity_level.NORMAL)
def test_webtables(browser):

    webtable_page = WebtablesPage(driver=browser)

    if webtable_page.code_status() != 200:
        pytest.skip(reason=f'Page {webtable_page.base_url} is unavailable')

    webtable_page.visit()
    assert webtable_page.add_btn.exist()
    assert not webtable_page.registration_form.exist()
    webtable_page.add_btn.click()
    assert webtable_page.registration_form.exist()
    webtable_page.submit_btn.click()
    assert webtable_page.registration_form.exist()

    webtable_page.fill_form()

    time.sleep(3)
    webtable_page.submit_btn.click()
    time.sleep(3)
    assert not webtable_page.registration_form.exist()
    time.sleep(3)


@allure.feature('WebtablesPage page')
@allure.story('Checking form')
@allure.severity(allure.severity_level.NORMAL)
def test_pages_webtables(browser):

    webtable_page = WebtablesPage(driver=browser)

    if webtable_page.code_status() != 200:
        pytest.skip(reason=f'Page {webtable_page.base_url} is unavailable')

    webtable_page.visit()
    for i in range(2):
        webtable_page.add_btn.click()
        webtable_page.fill_form()
        webtable_page.submit_btn.click()

    assert webtable_page.previous_btn.get_dom_attribute('disabled') == 'true'
    assert webtable_page.next_btn.get_dom_attribute('disabled') == 'true'
    assert not webtable_page.previous_btn.is_enabled()
    assert not webtable_page.next_btn.is_enabled()

    for i in range(6):
        webtable_page.add_btn.click()
        webtable_page.fill_form()
        webtable_page.submit_btn.click()
        time.sleep(1)

    assert webtable_page.next_btn.is_enabled()
    assert webtable_page.total_pages.get_text() == '2'
    webtable_page.next_btn.click_force()
    assert webtable_page.current_page.get_dom_attribute('value') == '2'
    assert webtable_page.previous_btn.is_enabled()
    time.sleep(3)




