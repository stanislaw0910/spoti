from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs
from .forms import NewUserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def index(request):
    '''data = {
        'title':'Main Page!!',
        'values':['Some','Hello','123']
    }'''
    songs = Songs.objects.all()
    return render(request, 'main/index.html', {'songs': songs})


def about(request):
    return render(request, 'main/about.html')


def login(request):
    form = LoginForm()
    data = {
        'form': form,
    }
    return render(request, 'main/login.html', data)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/index.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("home")
        messages.error(request, "Unsuccessful registration.Invalid information")
    form = NewUserForm()
    data = {
        'form': form,
    }
    return render(request, 'main/index.html', data)


'''def registration_request(request):

    return render(request, 'main/index.html')'''

