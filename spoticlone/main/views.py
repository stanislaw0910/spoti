from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    songs = Songs.objects.all()
    return render(request, 'main/index.html', {'sounds': songs})


def about(request):
    songs = Songs.objects.all()
    return render(request, 'main/about.html', {'songs': songs})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        object_list = Songs.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
    return render(request, 'main/search_results.html', {'songs': object_list})



