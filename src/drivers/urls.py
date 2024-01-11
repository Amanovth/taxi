from django.urls import path
from .views import NearestDriversListAPIView, index, room

urlpatterns = [
    path('nearestdrivers', NearestDriversListAPIView.as_view(), name='nearestdrivers'),
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),

]
