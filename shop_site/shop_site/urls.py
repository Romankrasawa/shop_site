from django.urls import include,  re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"user/", include('user.urls')),
    re_path(r"", include('shop.urls')),
]
