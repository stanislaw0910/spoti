from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Songs(models.Model):
    artist = models.TextField(max_length=50)
    album = models.TextField(max_length=50)
    title = models.TextField(max_length=50)
    track_num = models.IntegerField(default=0)
    duration = models.IntegerField(default=0,null=False)
    genre = models.TextField(max_length=50)
    recording_date = models.IntegerField(null=False)
    path = models.FilePathField()
    #cover = models.BinaryField()


    def __str__(self):
        return self.artist + ' - ' + self.title

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"


'''class Albums(models.Model):
    pass
class Artist(models.Model):
    pass
class Users(User):
    pass'''

