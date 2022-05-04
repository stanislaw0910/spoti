from django.core.files import File
from main.models import Songs, Artists, Albums
'''r = open('/home/stas/PycharmProjects/mp3_module/2009_-_Crack_The_Skye/CD_1/03._Quintessence.mp3', 'rb')
django_file = File(r)
sound = Sounds()
sound.title = '03._Quintessence'
sound.path.save('03._Quintessence.mp3', django_file, save=True)
r.close()
'''
with open('/home/stas/PycharmProjects/mp3_module/soundlist.txt', 'r') as f:
    for line in f:
        tags = line.split(sep=',')
        file = open(tags[-1].strip(), 'rb')
        django_file = File(file)
        song = Songs()
        artist = Artists()
        artist, _ = Artists.objects.get_or_create(name=tags[0])
        album = Albums()
        album, _ = Albums.objects.get_or_create(title=tags[1], genre=tags[5], artist=artist, rec_date=tags[6])
        Songs.objects.get_or_create(title=tags[2], artist=artist, album=album,
                                    file=django_file, duration=tags[4], track_number=tags[3])
        #song.path.save(song.track_number + tags[2], django_file, save=True)

