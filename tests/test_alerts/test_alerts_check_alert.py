from pages.alerts import AlertsPage
import time
import allure
import pytest


@allure.feature('Alerts page')
@allure.story('Checking alert')
@allure.severity(allure.severity_level.NORMAL)
def test_alert(browser):

    alert_page = AlertsPage(driver=browser)

    if alert_page.code_status() != 200:
        pytest.skip(reason=f'Page {alert_page.base_url} is unavailable')

    alert_page.visit()
    assert not alert_page.alert()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


@allure.feature('Alerts page')
@allure.story('Checking alert text')
@allure.severity(allure.severity_level.NORMAL)
def test_alert_text(browser):

    alert_page = AlertsPage(driver=browser)

    if alert_page.code_status() != 200:
        pytest.skip(reason=f'Page {alert_page.base_url} is unavailable')

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()


@allure.feature('Alerts page')
@allure.story('Checking confirm')
@allure.severity(allure.severity_level.NORMAL)
def test_confirm(browser):

    alert_page = AlertsPage(driver=browser)

    if alert_page.code_status() != 200:
        pytest.skip(reason=f'Page {alert_page.base_url} is unavailable')

    alert_page.visit()
    alert_page.btn_confirm.click()
    alert_page.alert().dismiss()
    assert alert_page.confirm_result.get_text() == 'You selected Cancel'


@allure.feature('Alerts page')
@allure.story('Checking prompt')
@allure.severity(allure.severity_level.NORMAL)
def test_prompt(browser):

    alert_page = AlertsPage(driver=browser)

    if alert_page.code_status() != 200:
        pytest.skip(reason=f'Page {alert_page.base_url} is unavailable')

    text = 'j'

    alert_page.visit()
    alert_page.btn_prompt.click()
    alert_page.alert().send_keys(text)
    alert_page.alert().accept()
    assert alert_page.prompt_result.get_text() == 'You entered ' + text


@allure.feature('Alerts page')
@allure.story('Checking alert')
@allure.severity(allure.severity_level.NORMAL)
def test_time_alert(browser):

    alert_page = AlertsPage(driver=browser)

    if alert_page.code_status() != 200:
        pytest.skip(reason=f'Page {alert_page.base_url} is unavailable')

    alert_page.visit()
    assert not alert_page.alert()
    alert_page.timer_alert_btn.click()
    time.sleep(5)
    assert alert_page.alert()


