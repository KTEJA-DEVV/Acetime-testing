import pytest

from pages.dashboard_page import Dashboard

@pytest.mark.ui
def test_dashboard_page(page,load_test_user_data,base_url):

    dashboardpage=Dashboard(page,load_test_user_data,base_url)
    dashboardpage.test_dashboard()
    dashboardpage.test_welcome_message_shows_username()
    dashboardpage.test_user_avatar_visible()
    dashboardpage.test_dashboard_core_elements_visible()
    dashboardpage.test_user_logout()