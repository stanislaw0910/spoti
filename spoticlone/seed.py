from django.core.files import File
from main.models import Sounds
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
        r = open(tags[-1].strip(), 'rb')
        django_file = File(r)
        sound = Sounds()
        sound.title = tags[2]
        if len(tags[3]) == 1:
            number = '0' + tags[3]
        else:
            number = tags[3]
        sound.path.save(number+tags[2], django_file, save=True)
        r.close()

