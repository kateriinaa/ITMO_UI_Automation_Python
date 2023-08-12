from pages.base_page import BasePage
from components.components import WebElement


class RadioPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes_btn = WebElement(driver, locator='#yesRadio', locator_type='css')
        self.impressive_btn = WebElement(driver, locator='#impressiveRadio', locator_type='css')
        self.no_btn = WebElement(driver, locator='#noRadio', locator_type='css')
        self.text = WebElement(driver, locator='.text-success', locator_type='css')
