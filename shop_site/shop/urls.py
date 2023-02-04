from django.urls import path
from .views import *

urlpatterns = [
    path('about_us/', about_us, name='about_us'),
    path('feedback/', feedback, name='feedback'),
    path('product/', product, name='product'),
    path('search/', search, name='search'),
    path('catalog/', catalog, name='catalog'),
    path('category/', category, name='category'),
    path('home/', home, name="home"),
    path('', home, name="home"),
]
