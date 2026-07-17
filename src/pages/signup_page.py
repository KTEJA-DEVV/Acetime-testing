from playwright.sync_api import expect
from utils.data_generator import mailgenerator, passgenerator, namegenerator


class SignupPage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def test_signuppage_load(self):
        self.page.goto(self.base_url)
        self.page.get_by_role("link", name="Get Started Free").click()
        expect(self.page.get_by_text("Create your account to get started.")).to_be_visible()
        assert self.page.get_by_placeholder("John Doe").is_visible()
        assert self.page.get_by_placeholder("you@example.com").is_visible()
        assert self.page.get_by_placeholder("Create a strong password").is_visible()
        assert self.page.get_by_placeholder("Confirm your password").is_visible()
        assert self.page.get_by_role('button',name="Create Account").is_enabled()

    def signup_success(self):
        name=namegenerator()
        email=mailgenerator()
        password=passgenerator()
        self.page.get_by_placeholder('John Doe').fill(name)
        self.page.get_by_placeholder('you@example.com').fill(email)
        self.page.get_by_placeholder('Create a strong password').fill(password)
        self.page.get_by_placeholder('Confirm your password').fill(password)
        self.page.get_by_text("Create Account").click()