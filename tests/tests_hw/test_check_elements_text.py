from pages.elements_page import ElementsPage


def test_check_elements(browser):
    page = ElementsPage(driver=browser)

    page.visit()
    assert page.elements_name.get_text() == 'Elements'

    assert page.icon.exist()
    assert page.sidebar_btn.exist()
    assert page.sidebar_textbox.exist()
