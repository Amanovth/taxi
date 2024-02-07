from django.urls import path
from .views import (
    NearestDriversListAPIView,
    index,
    room,
    CheckAPIView,
    RatingAPIView
)

urlpatterns = [
    path('nearestdrivers', NearestDriversListAPIView.as_view(), name='nearestdrivers'),
    # path("", index, name="index"),
    # path("<str:room_name>/", room, name="room"),
    path('check', CheckAPIView.as_view(), name='check'),
    path('rating', RatingAPIView.as_view(), name='rating')
]
