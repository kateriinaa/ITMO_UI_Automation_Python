from pages.textbox import TextBox


def test_placeholder(browser):

    page = TextBox(driver=browser)
    page.visit()
    assert page.full_name.get_dom_attribute('placeholder') == 'Full Name'
