from pages.modal_dialogs import ModalDialogsPage
import pytest
import allure
import pytest


@allure.feature('ModalDialogs page')
@allure.story('Checking modals')
@allure.severity(allure.severity_level.NORMAL)
def test_modal_btn(browser):

    page_modal_dialog = ModalDialogsPage(driver=browser)

    if page_modal_dialog.code_status() != 200:
        pytest.skip(reason=f'Page {page_modal_dialog.base_url} is unavailable')

    page_modal_dialog.visit()

    assert page_modal_dialog.small_modal_btn.exist()
    assert page_modal_dialog.large_modal_btn.exist()

    page_modal_dialog.small_modal_btn.click()
    assert page_modal_dialog.modal_content.exist()
    assert page_modal_dialog.close_small_modal.exist()
    page_modal_dialog.close_small_modal.click()

    page_modal_dialog.large_modal_btn.click()
    assert page_modal_dialog.modal_content.exist()
    assert page_modal_dialog.close_large_modal.exist()
    page_modal_dialog.close_large_modal.click()