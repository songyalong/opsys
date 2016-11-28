#coding:utf-8
from ..models.menus import *
class MenusService(object):

    @staticmethod
    def get_menus():
        menus = Menus.get_parent_menus("0")
        if menus:
            for menu in menus:
                menu.sub_menus = Menus.get_menus_by_parent_id(parent_id=menu.id)
        return menus