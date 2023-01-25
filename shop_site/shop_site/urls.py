from django.urls import include,  re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path('accounts/', include('allauth.urls')),
    re_path('logout/', LogoutView.as_view(), name="logout"),
    re_path("admin/", admin.site.urls, name="admin"),
    re_path("user/", include('user.urls')),
    re_path("", include('shop.urls')),
]
