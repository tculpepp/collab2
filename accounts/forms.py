from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Override the default username and password only fields to include required profile fields
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']