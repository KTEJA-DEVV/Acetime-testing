import pytest

from pages.signup_page import SignupPage

@pytest.mark.ui
def test_signup_page(page, base_url):
    signup_page = SignupPage(page, base_url)
    signup_page.test_signuppage_load()
    signup_page.signup_success()


