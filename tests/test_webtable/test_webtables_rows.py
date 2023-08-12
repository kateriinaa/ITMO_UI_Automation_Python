from pages.webtables import WebtablesPage
import time
import pytest
import allure


@allure.feature('Webtables page')
@allure.story('Checking delete button')
@allure.severity(allure.severity_level.NORMAL)
def test_webtables_rows(browser):

    webtable_page = WebtablesPage(driver=browser)

    if webtable_page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    webtable_page.visit()
    assert not webtable_page.no_rows_found_block.exist()
    while webtable_page.delete_btn.exist():
        webtable_page.delete_btn.click()
    assert webtable_page.no_rows_found_block.exist()
