from django.db import models
#from django.contrib.auth.models import User


class Sounds(models.Model):
    title = models.TextField(max_length=50)
    path = models.FileField()
    artist = models.TextField(max_length=50, default="Untitled Artist")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sound"
        verbose_name_plural = "Sounds"


'''artist = models.TextField(max_length=50)
    album = models.TextField(max_length=50)
    track_num = models.IntegerField(default=0)
    duration = models.IntegerField(default=0,null=False)
    genre = models.TextField(max_length=50)
    recording_date = models.IntegerField(null=False)
    cover = models.BinaryField()'''
