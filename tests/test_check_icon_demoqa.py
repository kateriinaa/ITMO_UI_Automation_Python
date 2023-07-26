from pages.demoqa import DemoQa


def test_site_version(browser):

    page = DemoQa(driver=browser)
    page.visit()
    page.icon.click()
    # page.click_on_the_icon()
    assert page.equal_url()
    assert page.icon.exist()



    # browser.get('https://demoqa.com/')
    # try:
    #     browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    # except NoSuchElementException:
    #     assert False
    # assert True
