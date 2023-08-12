from pages.base_page import BasePage
from components.components import WebElement


class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.content_first_block = WebElement(driver, locator='#section1Content > p', locator_type='css')
        self.content_second_block1 = WebElement(driver, locator='#section2Content > p:nth-child(1)', locator_type='css')
        self.content_second_block2 = WebElement(driver, locator='#section2Content > p:nth-child(2)', locator_type='css')
        self.content_third_block = WebElement(driver, locator='#section3Content > p', locator_type='css')
        self.heading = WebElement(driver, locator='#section1Heading', locator_type='css')


