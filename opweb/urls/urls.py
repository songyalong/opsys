from django.conf.urls import url, include
from ..views import *
from ..views.login import *
urlpatterns = [
    url(r'^login/', login_in),
]