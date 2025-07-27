import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            # Xac dinh duong dan toi file config
            try:
                project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                config_path = os.path.join(project_root, 'test_setting.json')
            except Exception as e:
                raise RuntimeError(f"Loi xac dinh duong dan file: {e}")
            # Kiem tra file ton tai
            if not os.path.isfile(config_path):
                raise FileNotFoundError(f"Khong tim thay file cau hinh tai: {config_path}")
            # Doc va parse Json
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    ConfigReader._config = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"loi khi doc ten file cau hinh")
            except Exception as e:
                raise RuntimeError(f'Loi khi doc file cau hinh: {e}')
        return ConfigReader._config

    @staticmethod
    def get_base_url():
        """Get the base URL from the configuration"""
        return ConfigReader.load_config().get('base_url')
    
    @staticmethod
    def get_expected_url():
        """Get the expected URL from the configuration"""
        return ConfigReader.load_config().get('expected_url')

    @staticmethod
    def get_username():
        """Get the username from the configuration"""
        return ConfigReader.load_config().get('credentials', {}).get('username')

    @staticmethod
    def get_password():
        """Get the password from the configuration"""
        return ConfigReader.load_config().get('credentials', {}).get('password')

    @staticmethod
    def get_implicit_timeout():
        """Get the implicit timeout from the configuration"""
        return ConfigReader.load_config().get('timeout', {}).get('implicit')

    @staticmethod
    def get_page_load_timeout():
        """Get the page load timeout from the configuration"""
        return ConfigReader.load_config().get('timeout', {}).get('page_load')
    
    @staticmethod
    def get_firstname():
        """Get the firstname from the configuration"""
        return ConfigReader.load_config().get('checkout_info', {}).get('first_name')

    @staticmethod
    def get_lastname():
        """Get the lastname from the configuration"""
        return ConfigReader.load_config().get('checkout_info', {}).get('last_name')
    
    @staticmethod
    def get_postal_code():
        """Get the code from the configuration"""
        return ConfigReader.load_config().get('checkout_info', {}).get('postal_code')
    
    @staticmethod
    def get_expected_message():
        """Get the expected message from the configuration"""
        return ConfigReader.load_config().get('expected_message')