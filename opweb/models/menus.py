from django.db import models


class Menus(models.Model):
    menu_name = models.CharField(max_length=200, )
