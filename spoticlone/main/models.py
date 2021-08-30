from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Songs(models.Model):
    artist = models.TextField(max_length=50)
    album = models.TextField(max_length=50)
    title = models.TextField(max_length=50)
    track_num = models.IntegerField(max_length=2)
    genre = models.TextField(max_length=50)
    recording_date = models.IntegerField(max_length=4)
    cover = models.FileField(upload_to='uploads/')
    path = models.FileField(upload_to='uploads/')

    '''cover = models.FileField(upload_to='uploads/')
    path = models.FileField(upload_to='uploads/')

    @classmethod
    def create(cls, artist, album, title, track_num, genre, recording_date, cover, path):
        songs = cls(artist=artist, album=album, title=title, track_nu=track_num, genre=genre, recording_date=recording_date
                    , cover=cover, path=path)
        # do something with the book
        return songs'''


    def __str__(self):
        return self.artist + ' - ' + self.title

    '''def get_absolute_url(self):
        return f'/news/{self.id}'''

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"


class Users(User):
    pass

