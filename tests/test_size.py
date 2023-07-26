from pages.demoqa import DemoQa
import time


def test_size(browser):

    page_demoqa = DemoQa(driver=browser)

    page_demoqa.visit()
    browser.set_window_size(300, 1000)
    time.sleep(3)
    browser.set_window_size(1000, 1000)
    time.sleep(3)
