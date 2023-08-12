from pages.accordian_page import AccordianPage
import time
import allure
import pytest


@allure.feature('Accordian page')
@allure.story('Checking blocks')
@allure.severity(allure.severity_level.NORMAL)
def test_accordian_visible(browser):

    accordian_page = AccordianPage(driver=browser)

    if accordian_page.code_status() != 200:
        pytest.skip(reason=f'Page {accordian_page.base_url} is unavailable')

    accordian_page.visit()
    assert accordian_page.content_first_block.visible()
    accordian_page.heading.click()
    time.sleep(3)
    assert not accordian_page.content_first_block.visible()


@allure.feature('Accordian page')
@allure.story('Checking blocks')
@allure.severity(allure.severity_level.NORMAL)
def test_visible_accordion_default(browser):

    accordian_page = AccordianPage(driver=browser)

    if accordian_page.code_status() != 200:
        pytest.skip(reason=f'Page {accordian_page.base_url} is unavailable')

    accordian_page.visit()
    assert not accordian_page.content_second_block1.visible()
    assert not accordian_page.content_second_block2.visible()
    assert not accordian_page.content_third_block.visible()

