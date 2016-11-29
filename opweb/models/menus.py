from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json


class Menus(models.Model, DjangoJSONEncoder):
    menu_name = models.CharField(max_length=200)
    menu_url = models.CharField(max_length=200)
    menu_no = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, )

    def to_json(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    @classmethod
    def get_menus_by_parent_id(cls, parent_id):
        menus = cls.objects.filter(parent_id=parent_id)
        return menus

    @classmethod
    def get_parent_menus(cls, parent_id="0"):
        return cls.objects.filter(parent_id=parent_id)

    @classmethod
    def inset_menus(cls, menu_name, parent_id="0"):
        cls.objects.create(menu_name=menu_name, parent_id=parent_id)
