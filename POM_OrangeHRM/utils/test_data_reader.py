import json
import os

class TestDataReader:
    _config = None

    @staticmethod
    def load_data():
        if TestDataReader._config is None:
            try:
                project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                config_path = os.path.join(project_root, 'test_data.json')
            except Exception as e:
                raise RuntimeError(f"Lỗi xác định đường dẫn file: {e}")

            if not os.path.isfile(config_path):
                raise FileNotFoundError(f"Không tìm thấy file test_data.json tại: {config_path}")

            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    TestDataReader._config = json.load(f)
            except json.JSONDecodeError:
                raise ValueError(f"Lỗi khi đọc JSON từ file")
            except Exception as e:
                raise RuntimeError(f'Lỗi khi đọc file: {e}')
        return TestDataReader._config

    @staticmethod
    def get_firstname():
        return TestDataReader.load_data().get('employee_name', {}).get('firstname')

    @staticmethod
    def get_midname():
        return TestDataReader.load_data().get('employee_name', {}).get('middlename')
    
    @staticmethod
    def get_lastname():
        return TestDataReader.load_data().get('employee_name', {}).get('lastname')

    @staticmethod
    def get_expected_title():
        return TestDataReader.load_data().get('title')