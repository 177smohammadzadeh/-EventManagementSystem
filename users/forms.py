from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    """
    Custom login form that extends Django's built-in AuthenticationForm.
    Adds customization for the username and password fields.
    """
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    """
    Custom registration form that extends Django's UserCreationForm.
    Includes additional fields such as email, first_name, and last_name.
    """
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text="Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Enter your last name.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']