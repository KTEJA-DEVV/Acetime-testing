import pytest

from api.signin_api import Signinapi
from api.calls_api import Callsapi
@pytest.mark.api
def test_callsapi(api_request,load_test_user_data):
    signinapi=Signinapi(api_request,load_test_user_data)
    details=signinapi.login()
    callsapi=Callsapi(api_request,details)
    roomid=callsapi.startcall()
    callsapi.joincall(roomid)