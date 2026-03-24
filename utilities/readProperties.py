import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configuration\\config.ini')

class RawConfig:

    @staticmethod
    def getApplicationURLL():
        url=config.get('common_file','baseurl')
        return url
