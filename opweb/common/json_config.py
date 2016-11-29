# coding: utf-8
import jsonpickle
pickler = jsonpickle.pickler.Pickler(unpicklable=False, max_depth=2)

def flatten(model):
    """去除pickler.flatten里面的一个字段"""
    json = pickler.flatten(model)
    json.pop('_state', None)
    return json


class JsonDic():
    def __init__(self, status, message, data=None):
        self.dic = {}
        self.dic['status'] = status
        self.dic['message'] = message
        self.dic['objects'] = data