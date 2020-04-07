from django.urls import re_path, include
from .views import index, login, compare,home

urlpatterns = [
    re_path(r'^visualise$', index, name='index'),
    re_path(r'^login',login,name='login'),
    re_path(r'^compare$', compare, name='compare'),
    re_path(r'^$', home, name='home'),
]