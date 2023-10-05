import yaml
import pytest
from testpage import OperationsHelper

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_simple(browser):
    value = OperationsHelper(browser)
    value.go_to_site()
    value.enter_login(testdata['user'])
    value.enter_password(testdata['password'])
    value.click_button()
    value.click_contact()
    value.enter_name('a')
    value.enter_email('a@a')
    value.enter_content('aaa')
    value.send_contact()
    value.switch()
    assert True


# def test_contact(browser):
#     value = OperationsHelper(browser)
#     value.go_to_site()
#     value.click_contact()
#     value.enter_name('a')
#     value.enter_email('a@a')
#     value.enter_content('aaa')
#     value.send_contact()
#     value.switch()
#     assert True


if __name__ == '__main__':
    pytest.main(['-v'])
