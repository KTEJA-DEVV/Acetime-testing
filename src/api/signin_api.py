import json
import os
class Signinapi:

    def __init__(self,request,data):
        self.request = request
        self.data = data

    def login(self):

        email=self.data["email"]
        password=self.data["password"]
        response=self.request.post("/api/auth/login",
                                   data={"email": email, "password": password})

        data = response.json()
        access_token = data["accessToken"]
        refresh_token = data["refreshToken"]
        user = data["user"]
        print(user["name"])
        return  access_token