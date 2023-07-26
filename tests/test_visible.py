from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):

    page = ElementsPage(driver=browser)

    page.visit()
    # page.sidebar_btn.click()
    time.sleep(3)
    assert page.sidebar_textbox.visible()


def test_not_visible_btn_sidebar(browser):

    page = ElementsPage(driver=browser)

    assert page.btn_sidebar_first_checkbox.visible()
    page.sidebar_btn.click()
    time.sleep(2)
    assert not page.btn_sidebar_first_checkbox.visible()
