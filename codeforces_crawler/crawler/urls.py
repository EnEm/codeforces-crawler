from django.urls import re_path, include
from .views import index, login, compare

urlpatterns = [
    re_path(r'^visualise$', index, name='index'),
    re_path(r'^compare$', compare, name='compare'),
    re_path(r'^$', login, name='login'),
]