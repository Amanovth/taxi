from django.urls import path
from .views import NearestDriversListAPIView

urlpatterns = [
    path('nearestdrivers', NearestDriversListAPIView.as_view(), name='nearestdrivers'),
    # path('register', )
]
