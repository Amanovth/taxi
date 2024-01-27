from django.urls import path
from .views import (
    RegisterView,
    VerifyPhoneView,
    UpdateFullNameView,
    LogoutView,
    LoginAPIView,
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path("auth/login", LoginAPIView.as_view(), name="login"),
    path('verify', VerifyPhoneView.as_view(), name='verify'),
    path('update-full-name', UpdateFullNameView.as_view(), name='update-full-name'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('login', LoginView.as_view(), name='login')
]
