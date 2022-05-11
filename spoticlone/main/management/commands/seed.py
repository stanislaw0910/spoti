from django.core.files import File
from main.models import Songs, Artists, Albums
from django.core.management import BaseCommand
'''r = open('/home/stas/PycharmProjects/mp3_module/2009_-_Crack_The_Skye/CD_1/03._Quintessence.mp3', 'rb')
django_file = File(r)
sound = Sounds()
sound.title = '03._Quintessence'
sound.path.save('03._Quintessence.mp3', django_file, save=True)
r.close()
'''
"""
with open('/home/stas/PycharmProjects/mp3_module/soundlist.txt', 'r') as f:
    for line in f:
        tags = line.split(sep=',')
        print(tags)
       file = open(tags[-1].strip(), 'rb')
        django_file = File(file)
        song = Songs()
        artist = Artists()
        artist, _ = Artists.objects.get_or_create(name=tags[0])
        album = Albums()
        album, _ = Albums.objects.get_or_create(title=tags[1], genre=tags[5], artist=artist, rec_date=tags[6])
        song, _ = Songs.objects.get_or_create(title=tags[2], artist=artist, album=album,
                                    file=django_file, duration=tags[4], track_number=tags[3])"""
        #song.path.save(song.track_number + tags[2], django_file, save=True)

class Command(BaseCommand):
    help = "Seeding with media from folder"

    def handle(self, *args, **options):
        with open('/home/stas/PycharmProjects/mp3_module/spoticlone/soundlist.txt', 'r') as f:
            for line in f:
                tags=line.split(sep=',')
                r=open(tags[-1].strip(), 'rb')
                file=File(r)
                artist, _ =Artists.objects.get_or_create(name=tags[0])
                album, _ =Albums.objects.get_or_create(title=tags[1], genre=tags[5], artist=artist, rec_date=tags[6])
                song, created = Songs.objects.get_or_create(title=tags[2], artist=artist, album=album,
                                                      duration=int(tags[4]), track_number=int(tags[3]))
                if created:
                    print(f'Created {tags[2]}')
                    song.file = file
                    song.save()
                else:
                    print(f'Already exists {tags[2]}')

                r.close()
                album.duration += song.duration
                album.save(update_fields=['duration'])
                if song.track_number > album.number_of_tracks:
                    album.number_of_tracks=song.track_number
                    album.save()
'''print('type of album.number_of_tracks is ' + str(type(album.number_of_tracks)))
            print('type of song.track_number is ' + str(type(song.track_number)))'''