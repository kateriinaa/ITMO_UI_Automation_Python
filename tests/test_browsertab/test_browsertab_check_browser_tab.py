import pytest
import allure
from pages.browser_tab import BrowserTabPage
import time


@allure.feature('BrowserTab page')
@allure.story('Checking browser tab')
@allure.severity(allure.severity_level.NORMAL)
def test_browser_tab(browser):

    browser_page = BrowserTabPage(driver=browser)

    if browser_page.code_status() != 200:
        pytest.skip(reason=f'Page {browser_page.base_url} is unavailable')

    browser_page.visit()
    assert len(browser.window_handles) == 1
    browser_page.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
