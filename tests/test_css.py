from pages.elements_page import ElementsPage


def test_flex_menu(browser):

    page = ElementsPage(driver=browser)
    page.visit()
    assert page.col.check_css('flex', '0 0 25%')
    assert page.col.check_css('max-width', '25%')
    browser.set_window_size(600, 1000)
    assert page.col.check_css('flex', '0 0 100%')
    assert page.col.check_css('max-width', '100%')
    browser.set_window_size(1000, 1000)


