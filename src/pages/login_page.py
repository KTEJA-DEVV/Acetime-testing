from playwright.sync_api import expect

from tests.conftest import base_url


class LoginPage:
    def __init__(self,page,base_url,userdata):
        self.page=page
        self.base_url=base_url
        self.userdata=userdata

    def login_success(self):
        self.page.goto(self.base_url)
        self.page.get_by_role('link', name="Sign In").nth(1).click()
        self.page.wait_for_selector("p:has-text('Welcome back! Sign in to continue.')")
        email=self.userdata['email']
        password=self.userdata['password']
        self.page.get_by_placeholder("you@example.com").fill(email)
        self.page.get_by_placeholder("Enter your password").fill(password)
        self.page.get_by_role('button',name="Sign In").click()
        self.page.wait_for_selector('p:has-text("Start a new call or join an existing one")')
        expect(self.page.get_by_text('Start a new call or join an existing one')).to_be_visible()

