import pytest
import allure


@allure.feature('Checking test status')
def test_success():
    assert True


@allure.feature('Checking test status')
def test_failure():
    assert False


@allure.feature('Checking test status')
def test_skip():
    pytest.skip('Need to be skipped')


@allure.feature('Checking test status')
def test_broken():
    raise Exception('oops')

