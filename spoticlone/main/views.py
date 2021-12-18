from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sounds
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    sounds = Sounds.objects.all()
    return render(request, 'main/index.html', {'sounds': sounds})


def about(request):
    return render(request, 'main/about.html')




