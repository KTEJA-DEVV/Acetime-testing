import pytest

from api.signup_api import signup_api
@pytest.mark.api
def test_signupapi(api_request):
    signupapi=signup_api(api_request)
    signupapi.signup()