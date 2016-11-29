#coding:utf-8
from ..models.user import *
class UserService(object):
    @classmethod
    def login_user_check(cls, username, password, session):
        is_login = User.objects.filter(username=username, password=password)
        return is_login