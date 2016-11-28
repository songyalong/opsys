from django.conf.urls import url, include
from ..views.login import *
from ..views.base import *
urlpatterns = [
    url(r'^login/', login_in),
    url(r'^menus/', get_menus),
    
]