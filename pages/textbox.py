from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, locator='#userName', locator_type='css')
        self.address = WebElement(driver, locator='#currentAddress.form-control', locator_type='css')
        self.btn_submit = WebElement(driver, locator='#submit', locator_type='css')
        self.name_saved = WebElement(driver, locator='#name', locator_type='css')
        self.current_address_saved = WebElement(driver, locator='#currentAddress.mb-1', locator_type='css')


