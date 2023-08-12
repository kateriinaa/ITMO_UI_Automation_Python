from pages.base_page import BasePage
from components.components import WebElement


class BrowserTabPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)

        self.new_tab = WebElement(driver, locator='#tabButton', locator_type='css')

