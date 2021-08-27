# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.forms import UserCreationForm


def user_page(request):
    if request.user.is_authenticated:
        return render(request, 'user/user_page.html')
    else:
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                print('WRONG')
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})




