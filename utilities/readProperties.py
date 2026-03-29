import configparser
import os

class ReadConfig:

    config = configparser.ConfigParser()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "configurations", "config.ini")

    config.read(config_path)

    @staticmethod
    def get_value(section, key):
        return ReadConfig.config.get(section, key)

    @staticmethod
    def get_section(section):
        return dict(ReadConfig.config.items(section))

    # @staticmethod
    # def get_username():
    #     return ReadConfig.config.get('commonInfo1','user_name')
    #
    # @staticmethod
    # def get_useremail():
    #     return ReadConfig.config.get('commonInfo1','user_email')
    #
    # @staticmethod
    # def get_title():
    #     return ReadConfig.config.get('commonInfo1','title')
    #
    # @staticmethod
    # def get_password():
    #     return ReadConfig.config.get('commonInfo1','password')
    #
    # @staticmethod
    # def get








