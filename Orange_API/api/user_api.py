from utils.test_data_reader import TestDataReader

class UserAPI:
    def __init__(self, session):
        self.session = session
        self.base_url = TestDataReader.get("base_url")

    def get_user_info(self, user_id):
        response = self.session.get(f"{self.base_url}/web/index.php/api/v2/pim/employees/{user_id}")
        return response
