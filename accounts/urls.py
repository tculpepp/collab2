# accounts/urls.py
from django.urls import path

from .views import SignUpView

# URL pattern for the account creation page
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]