
from django.urls import path
from . import views

"""
Defines URL patterns for user authentication and registration.

- 'login/': Handles user login.
- 'register/': Provides a form for user registration.
- 'logout/': Logs the user out.
"""
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]