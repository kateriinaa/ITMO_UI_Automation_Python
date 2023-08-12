from pages.base_page import BasePage
from components.components import WebElement


class CheckBoxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)

        self.checkbox = WebElement(driver, locator='span.rct-text', locator_type='css')
        self.btn_expand_all = WebElement(driver, locator='.rct-option.rct-option-expand-all', locator_type='css')
