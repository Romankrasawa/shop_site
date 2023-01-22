from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'about_us/', about_us, name='about_us'),
    re_path(r'feedback/', feedback, name='feedback'),
    re_path(r'product/', product, name='product'),
    re_path(r'search/', search, name='search'),
    re_path(r'catalog/', catalog, name='catalog'),
    re_path(r'category/', category, name='category'),
    re_path(r'home/', home, name='home'),
    re_path(r'', home, name='home')
]
