# accounts/views.py

from .forms import SignupForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
    success_message = "User has been created, please login with your username and password"
