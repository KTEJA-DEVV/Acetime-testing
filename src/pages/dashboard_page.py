import re

from playwright.sync_api import expect
from pages.login_page import  LoginPage
class Dashboard:
    def __init__(self,page,data,base_url):
        self.page=page
        self.data=data
        self.base_url=base_url

    def test_dashboard(self):
        loginpage=LoginPage(self.page,self.base_url,self.data)
        loginpage.login_success()
        expect(self.page.get_by_text("Start a new call or join an existing one")).to_be_visible()

    def test_welcome_message_shows_username(self):
        username="tesing"
        expect(self.page.get_by_text(f"Welcome back, {username}!")).to_be_visible()

    def test_dashboard_core_elements_visible(self):
        expect(self.page.get_by_role("heading",name=re.compile("Welcome back"))).to_be_visible()
        expect(self.page.get_by_text("Join Call")).to_be_visible()
        expect(self.page.get_by_role("link", name="Messages",exact=True)).to_be_visible()
        expect(self.page.get_by_role("link", name="Network",exact=True)).to_be_visible()
        expect(self.page.get_by_role("link", name="History")).to_be_visible()

    def test_user_avatar_visible(self):
        avatar=self.page.get_by_role("button",name="T",exact=True)
        expect(avatar).to_be_visible()
        expect(avatar).to_have_text("T")

    def test_user_logout(self):
        avatar = self.page.get_by_role("button", name="T", exact=True)
        avatar.click()
        self.page.get_by_role("button", name="Logout", exact=True).click()
        expect(self.page.get_by_text("Video calls with AI superpowers")).to_be_visible()


