from urllib import response

from utils.data_generator import namegenerator,mailgenerator,passgenerator
class signup_api:
    def __init__(self,request):
        self.request=request

    def signup(self):
        name=namegenerator()
        email=mailgenerator()
        password=passgenerator()
        response=self.request.post('/api/auth/register',
                                   data={
                                       "name": name,
                                       "email": email,
                                       "password": password
                                   })

        data=response.json()
        access_token = data["accessToken"]
        refresh_token = data["refreshToken"]
        user = data["user"]
        print(user["name"])
        return user,access_token,refresh_token
