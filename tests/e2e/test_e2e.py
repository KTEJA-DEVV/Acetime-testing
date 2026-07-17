import pytest

from api.signup_api import signup_api
from api.calls_api import  Callsapi
from pages.calls_page import CallsPage
from pages.dashboard_page import  Dashboard
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from api.signin_api import Signinapi
from api.auth_api import AuthAPI
@pytest.mark.e2e
def test_e2e(page,base_url,api_request,load_test_user_data):
    signupage=SignupPage(page,base_url)
    signupage.test_signuppage_load()
    signupage.signup_success()
    loginpage=LoginPage(page,base_url,load_test_user_data)
    loginpage.login_success()
    signupapi=signup_api(api_request)
    details=signupapi.signup()
    signinapi=Signinapi(api_request,load_test_user_data)
    token=signinapi.login()
    dashboardpage=Dashboard(page,load_test_user_data,base_url)
    dashboardpage.test_dashboard()
    dashboardpage.test_welcome_message_shows_username()
    dashboardpage.test_dashboard_core_elements_visible()
    dashboardpage.test_user_avatar_visible()
    dashboardpage.test_user_logout()
    authapi=AuthAPI(api_request,base_url,page,details)
    authapi.loginapi()
    callsapi=Callsapi(api_request,token)
    roomId=callsapi.startcall()
    callsapi.joincall(roomId)
    callspage = CallsPage(page, base_url, load_test_user_data,roomId)
    callspage.joincall()



