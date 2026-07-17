import pytest

from pages.login_page import LoginPage

@pytest.mark.ui
def test_signin_page(page,base_url,load_test_user_data):
    loginpage=LoginPage(page,base_url,load_test_user_data)
    loginpage.login_success()