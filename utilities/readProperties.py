import configparser

config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_username1():
        username1 = config.get('common info', 'username1')
        return username1

    @staticmethod
    def get_password1():
        password1 = config.get('common info', 'password1')
        return password1

    @staticmethod
    def get_username2():
        username2 = config.get('common info', 'username2')
        return username2

    @staticmethod
    def get_password2():
        password2 = config.get('common info', 'password2')
        return password2

    @staticmethod
    def get_username3():
        username3 = config.get('common info', 'username3')
        return username3

    @staticmethod
    def get_password3():
        password3 = config.get('common info', 'password3')
        return password3

    @staticmethod
    def get_username4():
        username4 = config.get('common info', 'username4')
        return username4

    @staticmethod
    def get_password4():
        password4 = config.get('common info', 'password4')
        return password4
