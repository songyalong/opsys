from django.conf.urls import url, include
from ..views.login import *
from ..views.base import *
from ..views.machine import *
urlpatterns = [
    url(r'^login/', login_in),
    url(r'^menus/', get_menus),
<<<<<<< HEAD
=======
    url(r'^index/', index),
    url(r'^machine/list/', machine_list),
>>>>>>> dev
]