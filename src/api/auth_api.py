from playwright.sync_api import expect




class AuthAPI:
    def __init__(self,api_request,base_url,page,details):
        self.api_request = api_request
        self.base_url = base_url
        self.page = page
        self.user,self.access_token,self.refresh_token = details

    def loginapi(self):
        self.page.goto(self.base_url)
        self.page.evaluate(
            """([accessToken, refreshToken, user]) => {
                localStorage.setItem("__not_first_visit__", "1");
                localStorage.setItem("accessToken", accessToken);
                localStorage.setItem("refreshToken", refreshToken);
                localStorage.setItem("isWhitelist", "false");
                localStorage.setItem("loglevel", "WARN");
                localStorage.setItem("onboarding-storage", JSON.stringify({isCompleted: true}));
                localStorage.setItem("user", JSON.stringify(user));
            }""",
            [self.access_token, self.refresh_token, self.user]
        )

        with self.page.expect_response(lambda r: "/api/auth/verify" in r.url) as resp_info:
            self.page.reload()

        verify_response = resp_info.value
        assert verify_response.status == 200, f"Token verification failed: {verify_response.status}"
        print(verify_response.json()["user"])
        self.page.goto(f"{self.base_url}home")
        self.page.wait_for_load_state("networkidle")
        expect(self.page.get_by_text("Start a new call or join an existing one")).to_be_visible()




