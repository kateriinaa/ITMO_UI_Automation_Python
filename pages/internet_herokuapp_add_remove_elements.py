from pages.base_page import BasePage
from components.components import WebElement


class InternetHerokuAddRemove(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn = WebElement(driver, locator='#content > div > button', locator_type='css')
        self.delete_btn = WebElement(driver, locator='#elements > button', locator_type='css')

