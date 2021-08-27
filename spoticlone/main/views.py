from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    songs = Songs.objects.all()
    return render(request, 'main/index.html', {'songs': songs})


def about(request):
    return render(request, 'main/about.html')




