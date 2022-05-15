from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs, Albums, Artists
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView, DetailView


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


def index(request):
    songs = Songs.objects.all()
    return render(request, 'main/index.html', {'sounds': songs, 'title': 'Main page'})


def about(request):
    songs = Songs.objects.all()
    return render(request, 'main/about.html', {'songs': songs})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        songs_list = Songs.objects.filter(
            Q(title__icontains=query)
        )
        albums_list = Albums.objects.filter(
            Q(title__icontains=query)
        )
        artists_list = Artists.objects.filter(
            Q(name__icontains=query)
        )
    return render(request, 'main/search_results.html', {'songs': songs_list, 'albums': albums_list,
                                                        'artists': artists_list, 'query': query})



