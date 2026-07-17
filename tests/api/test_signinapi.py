import pytest

from api.signin_api import Signinapi
@pytest.mark.api
def test_signin_api(api_request,load_test_user_data):
    signinapi=Signinapi(api_request,load_test_user_data)
    signinapi.login()

