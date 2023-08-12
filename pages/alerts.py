from pages.base_page import BasePage
from components.components import WebElement


class AlertsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(driver, locator='#alertButton', locator_type='css')
        self.btn_confirm = WebElement(driver, locator='#confirmButton', locator_type='css')
        self.confirm_result = WebElement(driver, locator='#confirmResult', locator_type='css')
        self.btn_prompt = WebElement(driver, locator='#promtButton', locator_type='css')
        self.prompt_result = WebElement(driver, locator='#promptResult', locator_type='css')
        self.timer_alert_btn = WebElement(driver, locator='#timerAlertButton', locator_type='css')

