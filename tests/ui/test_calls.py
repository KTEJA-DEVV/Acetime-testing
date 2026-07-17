import pytest

from pages.calls_page import CallsPage
from api.signin_api import Signinapi
from api.calls_api import Callsapi


@pytest.mark.ui
def test_calls_page(page,base_url,load_test_user_data,api_request):
    signinapi = Signinapi(api_request, load_test_user_data)
    details = signinapi.login()
    callsapi = Callsapi(api_request, details)
    roomId=callsapi.startcall()
    callspage=CallsPage(page,base_url,load_test_user_data,roomId)
    callspage.newcall()
    callspage.joincall()

