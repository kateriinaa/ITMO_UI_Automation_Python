from pages.demoqa import DemoQa
from pages.accordian_page import AccordianPage
from pages.alerts import AlertsPage
from pages.browser_tab import BrowserTabPage
import pytest
import time
import allure


@allure.feature('Meta')
@allure.story('Checking meta')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('pages', [AccordianPage, AlertsPage, DemoQa, BrowserTabPage])
def test_check_title_all_pages(browser, pages):

    page = pages(browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    time.sleep(2)
    assert page.head_meta.get_dom_attribute('name') == 'viewport'
    assert page.head_meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
