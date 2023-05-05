# accounts/urls.py
from django.urls import path

from .views import SignUpView, ResetPasswordView

# URL pattern for the account creation page
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
]