from django.urls import path
from rest_framework.permissions import IsAdminUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Taxi',
        default_version='v1',
        description='API for Taxi',
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(IsAdminUser,),
    # url='https://taxi.kg'
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
