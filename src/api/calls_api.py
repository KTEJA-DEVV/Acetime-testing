from os import access
from urllib import response
from wsgiref import headers


class Callsapi:
    def __init__(self,request,access_token):
        self.request = request
        self.access_token = access_token

    def startcall(self):
        access_token = self.access_token
        response=self.request.post('/api/rooms',
                                   headers={'Authorization': 'Bearer ' + access_token})

        return response.json()['roomId']

    def joincall(self,roomId):
        access_token = self.access_token
        response=self.request.post(f'/api/rooms/{roomId}/join',
                                   headers={'Authorization':'Bearer '+ access_token})

        print(response.json())



