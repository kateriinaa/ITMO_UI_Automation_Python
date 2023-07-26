from pages.elements_page import ElementsPage


def test_find_elements(browser):

    element_page = ElementsPage(driver=browser)

    element_page.visit()
    assert element_page.btns_first_menu.check_count_elements(9)