from pages.form_page import FormPage
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def test_login_form(browser):

    formpage = FormPage(driver=browser)

    formpage.visit()
    assert not formpage.modal_dialog.exist()
    formpage.firstname.send_keys('tester')
    formpage.lastname.send_keys('testerovich')
    formpage.useremail.send_keys('test@ttt.tt')
    formpage.gender_radio_1.click_force()
    formpage.usernumber.send_keys('9992223344')
    formpage.hobbies_sport.click_force()
    formpage.currentAddress.send_keys('Spb')
    formpage.state_btn.click()
    ActionChains(browser).send_keys(Keys.DOWN).perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    formpage.city_btn.click()
    ActionChains(browser).send_keys(Keys.DOWN).perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(3)
    formpage.btn_submit.click_force()
    time.sleep(3)
    assert formpage.modal_dialog.exist()
    formpage.btn_close_modal.click_force()
