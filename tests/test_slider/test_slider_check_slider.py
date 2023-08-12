from pages.slider import SliderPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import time
import allure


@allure.feature('Slider page')
@allure.story('Checking slider')
@allure.severity(allure.severity_level.NORMAL)
def test_check_slider(browser):

    page = SliderPage(driver=browser)
    action_chains = ActionChains(browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()
    #action_chains.click_and_hold(page.slider.find_element()).move_by_offset(, 0).release().perform()

    while not page.slider_value.get_dom_attribute('value') == '50':
        page.slider.send_keys(Keys.ARROW_RIGHT)
    assert page.slider_value.get_dom_attribute("value") == '50'



