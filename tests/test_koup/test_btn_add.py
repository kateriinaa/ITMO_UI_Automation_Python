from pages.internet_herokuapp import InternetHeroku
from pages.internet_herokuapp_add_remove_elements import InternetHerokuAddRemove
import pytest
import allure


@allure.feature('InternetHeroku page')
@allure.story('Checking elements')
@allure.severity(allure.severity_level.NORMAL)
def test_bth(browser):

    page = InternetHeroku(driver=browser)
    add_remove_page = InternetHerokuAddRemove(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')
    if add_remove_page.code_status() != 200:
        pytest.skip(reason=f'Page {add_remove_page.base_url} is unavailable')

    page.visit()
    assert page.link.get_text() == 'Add/Remove Elements'
    page.link.click()
    assert add_remove_page.equal_url()
    assert add_remove_page.btn.get_text() == 'Add Element'
    assert add_remove_page.btn.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        add_remove_page.btn.click()
    assert add_remove_page.delete_btn.check_count_elements(4)
    for i in add_remove_page.delete_btn.find_elements():
        assert i.text == 'Delete'
    for i in range(4):
        add_remove_page.delete_btn.click()
    assert add_remove_page.delete_btn.check_count_elements(0)



