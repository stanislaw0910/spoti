from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from user.models import Profile
from django.conf import settings
from .custom_storage import MyFileStorage
import datetime

mfs = MyFileStorage()


class Artists(models.Model):
    name = models.CharField(max_length=100, default="Untitled Artist")
    picture = models.ImageField(upload_to=f'uploads/{name}', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"


class Albums(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    rec_date = models.PositiveIntegerField()
    album_art = models.ImageField(upload_to=f'{artist.name}/{title}', null=True, blank=True)
    number_of_tracks = models.PositiveIntegerField(default=0, null=True, blank=True)
    # type =

    def __str__(self):
        return self.title

    def number_of_tracks(self):
        number = self.songs.all().count()
        return number

    def album_duration(self):
        duration = self.songs.all().aggregate(Sum('duration'))
        duration = str(datetime.timedelta(seconds=duration['duration__sum']))
        return duration if duration[0] != '0' else duration[2:]

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Songs(models.Model):
    '''def generate_album_folder(self, filename):
        name = f"{self.artist}/{self.album}/{filename.split('/')[-1]}"
        return name'''

    title = models.TextField(max_length=50)
    artist = models.ForeignKey(Artists, related_name='songs', on_delete=models.CASCADE)
    album = models.ForeignKey(Albums, related_name='songs', on_delete=models.CASCADE)
    file=models.FileField(storage=mfs)
    duration = models.IntegerField(default=0)  # song duration in seconds
    track_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def song_duration(self):  # duration formatted to h:mm:ss
        f_duration = str(datetime.timedelta(seconds=self.duration))
        return f_duration if f_duration[0]!='0' else f_duration[2:]

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"


class FavoriteBase(models.Model):
    class Meta:
        abstract=True

    user=models.ForeignKey(Profile, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class FavoriteArtist(FavoriteBase):
    artist = models.ForeignKey(Artists, related_name='favorite_artist', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}_{self.artist}'


class FavoriteSong(FavoriteBase):
    song = models.ForeignKey(Songs, related_name='favorite_song', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}_{self.song}'


class FavoriteAlbum(FavoriteBase):
    album = models.ForeignKey(Albums, related_name='favorite_album', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}_{self.album}'
