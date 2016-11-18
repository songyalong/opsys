# coding:utf-8
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, )
    password = models.CharField(max_length=200, )
    birthday = models.DateField()
    create_time = models.DateField(auto_now_add=True)
    telphone = models.CharField(max_length=20, )
    age = models.IntegerField()
