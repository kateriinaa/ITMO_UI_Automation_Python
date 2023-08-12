from pages.modal_dialogs import ModalDialogsPage
from pages.demoqa import DemoQa
import pytest
import allure


@allure.feature('ModalDialogs page')
@allure.story('Checking navigation')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_modal(browser):

    modal_page = ModalDialogsPage(driver=browser)
    page_demoqa = DemoQa(driver=browser)

    if modal_page.code_status() != 200:
        pytest.skip(reason=f'Page {modal_page.base_url} is unavailable')
    if page_demoqa.code_status() != 200:
        pytest.skip(reason=f'Page {page_demoqa.base_url} is unavailable')

    modal_page.visit()
    modal_page.refresh()
    modal_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert page_demoqa.equal_url()
    assert page_demoqa.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)

