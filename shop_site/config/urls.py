from django.urls import include,  path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("user/", include('user.urls')),
    path("", include('shop.urls')),
] 

# handler500 = 'shop.views.error_500'
