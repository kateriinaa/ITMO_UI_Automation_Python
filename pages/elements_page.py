from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.col = WebElement(driver, locator='div.row > div:nth-child(1)', locator_type='css')
        self.elements_name = WebElement(driver, locator='.main-header', locator_type='css')
        self.icon = WebElement(driver, locator='#app > header > a > img', locator_type='css')
        self.sidebar_btn = WebElement(driver, locator='div:nth-child(1) > span > div', locator_type='css')
        self.sidebar_textbox = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-0 > span',
                                          locator_type='css')
        self.btn_sidebar_first_checkbox = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-1 > span',
                                                     locator_type='css')
        self.btns_first_menu = WebElement(driver, locator='div:nth-child(1) > div > ul > li', locator_type='css')



