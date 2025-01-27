from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages

def user_login(request):
    """
    Handles user login functionality.
    If the request is POST, it validates the login form and logs the user in.
    Displays success or error messages accordingly.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_register(request):
    """
    Handles user registration functionality.
    If the request is POST, it validates the registration form and creates a new user.
    Logs the user in after successful registration and displays appropriate messages.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            login(request, user)
            messages.success(request, "Your account has been created successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_logout(request):
    """
    Handles user logout functionality.
    Logs the user out and redirects them to the homepage with a logout message.
    """
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')