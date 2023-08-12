from pages.base_page import BasePage
from components.components import WebElement


class ProgressBarPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)

        self.procent = WebElement(driver, locator='.progress-bar', locator_type='css')
        self.btn = WebElement(driver, locator='#startStopButton', locator_type='css')