import time
import pytest
import allure
from pages.droppable import DroppablePage
from selenium.webdriver import ActionChains


@allure.feature('Droppable page')
@allure.story('Checking drag and drop')
@allure.severity(allure.severity_level.NORMAL)
def test_drag_drop(browser):

    drop_page = DroppablePage(driver=browser)
    action_chains = ActionChains(browser)

    if drop_page.code_status() != 200:
        pytest.skip(reason=f'Page {drop_page.base_url} is unavailable')

    drop_page.visit()
    action_chains.drag_and_drop(drop_page.drag.find_element(), drop_page.drop.find_element()).perform()

    time.sleep(1)


@allure.feature('Droppable page')
@allure.story('Checking drag and drop')
@allure.severity(allure.severity_level.NORMAL)
def test_drag_drop_color(browser):

    drop_page = DroppablePage(driver=browser)
    action_chains = ActionChains(browser)

    if drop_page.code_status() != 200:
        pytest.skip(reason=f'Page {drop_page.base_url} is unavailable')

    drop_page.visit()
    assert not drop_page.drop.get_dom_attribute("background-color")
    action_chains.drag_and_drop(drop_page.drag.find_element(), drop_page.drop.find_element()).perform()
    assert drop_page.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop_by_offset(drop_page.drag.find_element(), 100, 100).perform()
    assert drop_page.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')



