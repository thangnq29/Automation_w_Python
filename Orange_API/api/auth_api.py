import requests
from utils.test_data_reader import TestDataReader

class AuthAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = TestDataReader.get("base_url")
        self.login_endpoint = "/web/index.php/auth/validate"

    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        response = self.session.post(self.base_url + self.login_endpoint, json=payload)
        return response
