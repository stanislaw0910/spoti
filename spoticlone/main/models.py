from django.db import models
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    album_art = models.ImageField(upload_to=f'uploads/{artist}/title', null=True, blank=True)
    number_of_tracks = models.PositiveIntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)  # duration of an album in seconds
    # type =

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Songs(models.Model):
    title = models.TextField(max_length=50)
    file = models.FileField()
    artist = models.ForeignKey(Artists, related_name='artist', on_delete=models.CASCADE)
    album = models.ForeignKey(Albums, related_name='album', on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)  # song duration in seconds
    track_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

@receiver(post_save, sender=Songs)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Albums.objects.create(user=instance)
    instance.profile.save()

'''artist = models.TextField(max_length=50)
    album = models.TextField(max_length=50)
    track_num = models.IntegerField(default=0)
    duration = models.IntegerField(default=0,null=False)
    genre = models.TextField(max_length=50)
    recording_date = models.IntegerField(null=False)
    cover = models.BinaryField()'''
