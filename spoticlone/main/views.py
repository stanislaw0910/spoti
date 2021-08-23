# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs
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


'''def registration_request(request):

    return render(request, 'main/index.html')'''

