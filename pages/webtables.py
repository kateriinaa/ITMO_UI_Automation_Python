from pages.base_page import BasePage
from components.components import WebElement
import randominfo
import random
import string


class WebtablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.add_btn = WebElement(driver, locator='#addNewRecordButton', locator_type='css')
        self.registration_form = WebElement(driver, locator='.modal-content', locator_type='css')
        self.submit_btn = WebElement(driver, locator='#submit', locator_type='css')
        self.no_rows_found_block = WebElement(driver, locator='.rt-noData', locator_type='css')
        self.delete_btn = WebElement(driver, locator='[title="Delete"]', locator_type='css')
        self.rows_text = WebElement(driver, locator='.rt-tbody', locator_type='css')
        self.first_name = WebElement(driver, locator='#firstName', locator_type='css')
        self.last_name = WebElement(driver, locator='#lastName', locator_type='css')
        self.user_email = WebElement(driver, locator='#userEmail', locator_type='css')
        self.age = WebElement(driver, locator='#age', locator_type='css')
        self.salary = WebElement(driver, locator='#salary', locator_type='css')
        self.department = WebElement(driver, locator='#department', locator_type='css')
        self.previous_btn = WebElement(driver, locator='.-previous button', locator_type='css')
        self.next_btn = WebElement(driver, locator='.-next button', locator_type='css')
        self.total_pages = WebElement(driver, locator='.-totalPages', locator_type='css')
        self.current_page = WebElement(driver, locator='.-pageJump input', locator_type='css')
        self.header_first_name = WebElement(driver,
                                            locator= 'div:nth-child(1) > div.rt-resizable-header-content',
                                            locator_type='css')
        self.header_last_name = WebElement(driver,
                                           locator='div:nth-child(2) > div.rt-resizable-header-content',
                                           locator_type='css')
        self.header_age = WebElement(driver,
                                     locator='div:nth-child(3) > div.rt-resizable-header-content',
                                     locator_type='css')
        self.header_email = WebElement(driver,
                                       locator='div:nth-child(4) > div.rt-resizable-header-content',
                                       locator_type='css')
        self.header_salary = WebElement(driver,
                                        locator='div:nth-child(5) > div.rt-resizable-header-content',
                                        locator_type='css')
        self.header_department = WebElement(driver,
                                            locator='div:nth-child(6) > div.rt-resizable-header-content',
                                            locator_type='css')
        self.rows_first_name = WebElement(driver,
                                          locator='div.rt-tbody > div > div > div:nth-child(1)',
                                          locator_type='css')
        self.rows_last_name = WebElement(driver,
                                         locator='div.rt-tbody > div > div > div:nth-child(2)',
                                         locator_type='css')
        self.rows_age = WebElement(driver,
                                   locator='div.rt-tbody > div > div > div:nth-child(3)',
                                   locator_type='css')
        self.rows_email = WebElement(driver,
                                     locator='div.rt-tbody > div > div > div:nth-child(4)',
                                     locator_type='css')
        self.rows_salary = WebElement(driver,
                                      locator='div.rt-tbody > div > div > div:nth-child(5)',
                                      locator_type='css')
        self.rows_department = WebElement(driver,
                                          locator='div.rt-tbody > div > div > div:nth-child(6)',
                                          locator_type='css')


    def fill_form(self
                  , first_name=randominfo.get_first_name()
                  , last_name=randominfo.get_last_name()
                  , user_email=''.join(random.choice(string.ascii_lowercase[:12]) for i in range(7))+'@gmail.com'
                  , age=random.randrange(18, 99)
                  , salary=random.randrange(1000, 10000, 1000)
                  , department=random.choice(['IT', 'Sales', 'Marketing'])):

        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.user_email.send_keys(user_email)
        self.age.send_keys(str(age))
        self.salary.send_keys(str(salary))
        self.department.send_keys(department)
