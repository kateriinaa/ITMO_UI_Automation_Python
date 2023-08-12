from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.firstname = WebElement(driver, locator='#firstName', locator_type='css')
        self.lastname = WebElement(driver, locator='#lastName', locator_type='css')
        self.useremail = WebElement(driver, locator='#userEmail', locator_type='css')
        self.gender_radio_1 = WebElement(driver, locator='#gender-radio-1', locator_type='css')
        self.usernumber = WebElement(driver, locator='#userNumber', locator_type='css')
        self.btn_submit = WebElement(driver, locator='#submit', locator_type='css')
        self.modal_dialog = WebElement(driver, locator='body > div.fade.modal.show > div', locator_type='css')
        self.btn_close_modal = WebElement(driver, locator='#closeLargeModal', locator_type='css')
        self.hobbies_sport = WebElement(driver, locator='#hobbies-checkbox-1', locator_type='css')
        self.currentAddress = WebElement(driver, locator='#currentAddress', locator_type='css')
        self.state_btn = WebElement(driver, locator='#state', locator_type='css')
        self.city_btn = WebElement(driver, locator='#city', locator_type='css')
        self.form = WebElement(driver, locator='#userForm', locator_type='css')
