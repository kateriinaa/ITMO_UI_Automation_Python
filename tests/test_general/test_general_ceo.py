from pages.demoqa import DemoQa
from pages.accordian_page import AccordianPage
from pages.alerts import AlertsPage
from pages.browser_tab import BrowserTabPage
import pytest
import time
import allure


@allure.feature('Demoqa page')
@allure.story('Checking title')
@allure.severity(allure.severity_level.NORMAL)
def test_title(browser):

    page_demoqa = DemoQa(driver=browser)

    if page_demoqa.code_status() != 200:
        pytest.skip(reason=f'Page {page_demoqa.base_url} is unavailable')

    page_demoqa.visit()
    assert page_demoqa.get_title() == 'DEMOQA'


@allure.feature('Title')
@allure.story('Checking titles')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('pages', [AccordianPage, AlertsPage, DemoQa, BrowserTabPage])
def test_check_title_all_pages(browser, pages):

    page = pages(browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'

