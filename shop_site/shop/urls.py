from django.urls import include,  re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    re_path(r'^home/', home, name='home'),
    re_path(r'', home, name='home')
]
