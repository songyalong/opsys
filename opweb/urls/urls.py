from django.conf.urls import url, include
from ..views import *
from ..tests import *
urlpatterns = [
    url(r'^test/', test),
]