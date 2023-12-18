from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as docs
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.users.urls')),
    path('', include('src.drivers.urls')),
]

urlpatterns += docs
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
