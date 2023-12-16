from django.urls import path
from .views import (
    RegisterView,
    VerifyPhoneView,
    UpdateFullNameView
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('verify', VerifyPhoneView.as_view(), name='verify'),
    path('update-full-name', UpdateFullNameView.as_view(), name='update-full-name')
    # path('login', LoginView.as_view(), name='login')
]
