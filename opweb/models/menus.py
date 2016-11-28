from django.db import models


class Menus(models.Model):
    menu_name = models.CharField(max_length=200, )
    parent = models.ForeignKey('self', null=True, default="0")