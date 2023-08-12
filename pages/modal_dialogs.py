from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns = WebElement(driver, locator='div.element-list.collapse.show ul li',
                               locator_type='css')
        self.icon = WebElement(driver, locator='#app > header > a > img', locator_type='css')
        self.small_modal_btn = WebElement(driver, locator='#showSmallModal', locator_type='css')
        self.large_modal_btn = WebElement(driver, locator='#showLargeModal', locator_type='css')
        self.modal_content = WebElement(driver, locator='.modal-content', locator_type='css')
        self.close_small_modal = WebElement(driver, locator='#closeSmallModal', locator_type='css')
        self.close_large_modal = WebElement(driver, locator='#closeLargeModal', locator_type='css')
