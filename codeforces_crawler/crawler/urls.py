from django.urls import re_path, include
from .views import index

urlpatterns = [
    re_path(r'^$', index, name='index'),
]