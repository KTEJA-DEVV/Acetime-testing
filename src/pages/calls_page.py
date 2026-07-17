from playwright.sync_api import expect

from pages.login_page import LoginPage
class CallsPage:
    def __init__(self,page,base_url,load_test_user_data,roomId):
        self.page=page
        self.base_url=base_url
        self.load_test_user_data=load_test_user_data
        self.roomId=roomId

    def newcall(self):
        loginpage=LoginPage(self.page,self.base_url,self.load_test_user_data)
        loginpage.login_success()
        self.page.context.grant_permissions(['camera', 'microphone'])
        start_call_btn = self.page.get_by_role('button', name='Start New Call')
        expect(start_call_btn).to_be_visible()
        start_call_btn.click()
        expect(self.page.get_by_text('Generate Image')).to_be_visible()
        self.page.get_by_title('End call').click()
        self.page.screenshot(path='screenshot.png')

    def joincall(self):
        self.page.context.grant_permissions(['camera', 'microphone'])
        join_call_btn=self.page.get_by_role('button', name='Join Call')
        expect(join_call_btn).to_be_visible()
        join_call_btn.click()
        self.page.get_by_placeholder('ABCDEF').fill(self.roomId)
        self.page.get_by_role('button', name='Join Call',exact=True).click()


