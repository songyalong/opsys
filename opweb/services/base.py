# coding:utf-8
from ..models.menus import *
from ..common.json_config import *

class MenusService(object):
    @staticmethod
    def get_menus():
        menus = Menus.get_parent_menus("0")
        if menus:
            for menu in menus:
                menu.sub_menus = Menus.get_menus_by_parent_id(parent_id=menu.id)
        return menus

class BaseService(object):
    def __init__(self):
        self.role = None

    @classmethod
    def del_models_by_id(cls, model, model_id):
        model.del_models_by_id(model_id)

    @classmethod
    def del_models_by_ids(cls, model, model_ids):
        model.del_models_by_ids(model_ids)

    @classmethod
    def set_user_role(cls, role):
        cls.role = role

    @classmethod
    def get_user_role(cls):
        return cls.role

    @staticmethod
    def flatten_list_data(list_data, data):
        """序列化多个model"""
        for ld in list_data:
            if type(ld) is dict:
                ld_pic = ld
            else:
                ld_pic = flatten(ld)
            data.append(ld_pic)
        return data

    @staticmethod
    def flatten_data_return(data):
        """序列化单个model, 返回序列化后的data"""
        data_pic = flatten(data)
        return data_pic
