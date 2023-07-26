from pages.demoqa import DemoQa


def test_check_text(browser):
    page = DemoQa(driver=browser)
    page.visit()
    if page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        assert True
    else:
        assert False
