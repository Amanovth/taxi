from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.users.urls')),
]

urlpatterns += docs
