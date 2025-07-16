import allure
from api.auth_api import AuthAPI
from api.user_api import UserAPI
from utils.test_data_reader import TestDataReader

@allure.feature("API Testing")
@allure.severity(allure.severity_level.CRITICAL)
def test_api_login_and_get_user():
    auth_api = AuthAPI()
    username = TestDataReader.get("username")
    password = TestDataReader.get("password")
    login_response = auth_api.login(username, password)

    assert login_response.status_code == 200
    assert "token" in login_response.text or "success" in login_response.text

    user_api = UserAPI(auth_api.session)
    user_id = TestDataReader.get("user_id")
    user_response = user_api.get_user_info(user_id)

    assert user_response.status_code == 200
