import requests

class LoginAPI:
    def __init__(self):
        self.session = requests.Session()
        self.login_url = "https://opensource-demo.orangehrmlive.com"
        self.headers = {
            "Content-Type": "application/json"
        }

    def login(self, username, password):
        payload = {"username": username, "password": password}
        response = self.session.post(self.login_url, json=payload, headers=self.headers)
        return response
