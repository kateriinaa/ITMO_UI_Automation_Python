from pages.modal_dialogs import ModalDialogsPage
import pytest
import allure


@allure.feature('ModalDialogs page')
@allure.story('Checking number of buttons')
@allure.severity(allure.severity_level.NORMAL)
def test_modal_elements(browser):

    page_modal_dialog = ModalDialogsPage(driver=browser)

    if page_modal_dialog.code_status() != 200:
        pytest.skip(reason=f'Page {page_modal_dialog.base_url} is unavailable')

    page_modal_dialog.visit()
    assert page_modal_dialog.btns.check_count_elements(5)





