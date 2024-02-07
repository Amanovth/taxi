from django.urls import path, include
from rest_framework import routers
from .views import CallView, CallListView, AcceptCallView, HistoryAPIView, HistoryDetailAPIView

router = routers.SimpleRouter()

# router.register(r"call-taxi", CallView, basename='call-taxi')

urlpatterns = [
    path('', include(router.urls)),
    path('call/post', CallView.as_view(), name='call-post'),
    path('call/list', CallListView.as_view(), name='call-list'),
    path('call/accept', AcceptCallView.as_view(), name='call-accept'),
    path('call/history', HistoryAPIView.as_view(), name='history-list'),
    path('call/<int:pk>/', HistoryDetailAPIView.as_view(), name='history-detail'),
]