from pages.demoqa import DemoQa


def test_title(browser):

    page_demoqa = DemoQa(driver=browser)

    page_demoqa.visit()
    assert page_demoqa.get_title() == 'DEMOQA'
