from pages.progress_bar import ProgressBarPage
import pytest
import time
import allure


@allure.feature('ProgressBar page')
@allure.story('Checking progress bar')
@allure.severity(allure.severity_level.NORMAL)
def test_check_bar(browser):

    page = ProgressBarPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    time.sleep(2)
    page.btn.click()
    while page.procent.get_dom_attribute('aria-valuenow') != '51':
        page.btn.click()
    time.sleep(2)