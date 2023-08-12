import time
from pages.webtables import WebtablesPage
import pytest
import allure


@allure.feature('WebtablesPage page')
@allure.story('Checking sort')
@allure.severity(allure.severity_level.NORMAL)
def test_sort(browser):

    page = WebtablesPage(driver=browser)

    if page.code_status() != 200:
        pytest.skip(reason=f'Page {page.base_url} is unavailable')

    page.visit()

    list_headers = [page.header_first_name, page.header_last_name, page.header_age, page.header_email,
                    page.header_salary, page.header_department]
    list_rows = [page.rows_first_name, page.rows_last_name, page.rows_age, page.rows_email,
                 page.rows_salary, page.rows_department]
    list_type = [str, str, int, str, int, str]

    for num, i in enumerate(list_headers):
        prev_rows = sorted([list_type[num](i.text) for i in list_rows[num].find_elements() if i.text != ' '])
        i.click()
        rows = [list_type[num](i.text) for i in list_rows[num].find_elements() if i.text != ' ']
        assert prev_rows == rows




