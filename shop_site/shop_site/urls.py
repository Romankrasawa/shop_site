from django.urls import include,  re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"", include('shop.urls')),
    re_path(r"user/", include('user.urls')),
]

