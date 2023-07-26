from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, locator='#app > header > a')
        self.bth_element = WebElement(driver, locator='#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer_text = WebElement(driver, locator='#app > footer > span')





