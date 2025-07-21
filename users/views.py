from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages  # <-- THIS LINE
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')  # Redirect to login page after registration

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'products:product_list'  # Make sure this name exists
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'users/login.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out


@login_required
def home_view(request):
    return render(request, 'base.html')
