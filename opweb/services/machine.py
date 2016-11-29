#!coding:utf-8
from ..models.machine import *


class MachineService(object):
    """所有的机器信息"""

    def get_all_machine(self):
        return Machine.objects.all()
