from django.contrib import admin
from .models import Songs, Artists, Albums
# Register your models here.


class SongsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'artist', 'album', 'duration', 'track_number']


class ArtistsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AlbumsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'artist', 'rec_date', 'number_of_tracks', 'duration']


admin.site.register(Songs, SongsAdmin)
admin.site.register(Artists, ArtistsAdmin)
admin.site.register(Albums, AlbumsAdmin)