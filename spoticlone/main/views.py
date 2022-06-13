from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs, Albums, Artists
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, ListView
from itertools import chain

class RenderHTMLPlayer(TemplateView):
    template_name = "main/player.html"
    model = Songs
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        song = Songs.objects.filter(id=id).first()
        song_uri = '/media' + request.build_absolute_uri(song.file.url).split('media')[-1]
        context = {'track_url': song_uri}
        return render(request, self.template_name, context)


class ArtistView(DetailView):
    model = Artists
    template_name = 'main/artist_page.html'
    context_object_name = 'artist'


class AlbumView(DetailView):
    model = Albums
    template_name = 'main/album_page.html'
    context_object_name = 'album'


class Index(ListView):
    model = Songs
    template_name = 'main/index.html'
    context_object_name = 'songs'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Main page'
        return context


class About(TemplateView):
    template_name = 'main/about.html'


class SearchResultsView(ListView):
    template_name = "main/search_results.html"
    model = Songs

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        context['query']=self.request.GET.get('q')
        context['songs']=Songs.objects.filter(
            Q(title__icontains=context['query'])
        )
        context['albums']=Albums.objects.filter(
            Q(title__icontains=context['query'])
        )
        context['artists']=Artists.objects.filter(
            Q(name__icontains=context['query'])
        )
        return context


class FavoritesView(TemplateView):
    template_name = 'main/favorites.html'

    def get_context_data(self, **kwargs):
        context = super(FavoritesView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user.profile
            context['songs'] = [object.song for object in user.favoritesong_set.all()]
            context['artists'] = [object.artist for object in user.favoriteartist_set.all()]
            context['albums']= [object.album for object in user.favoritealbum_set.all()]
        return context

