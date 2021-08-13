import os
import glob
import eyed3

os.chdir(os.path.join(os.getcwd(), '2009_-_Crack_The_Skye/CD_1'))
path = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '_')))
mp3_dir = []
image = ''
for file in glob.glob("*.jpg"):
    image = os.path.abspath(file)
for file in glob.glob("*.mp3"):
    mp3_dir.append((file, os.path.abspath(file)))
mp3_dir.sort()
print(mp3_dir)
for name in mp3_dir:
    audiofile = eyed3.load(name[0])
    eyed3.log.setLevel("ERROR")
    if audiofile.tag.track_num[0] == 8:
        audiofile.tag.album = u'Crack The Skye'
        audiofile.tag.save()
    mp3_data = (
        artist, album, title, track_num, genre, recording_date, cover, path) = audiofile.tag.artist, \
                                                                        audiofile.tag.album, \
                                                                        audiofile.tag.title, \
                                                                        audiofile.tag.track_num[0], \
                                                                        tuple(str(audiofile.tag.genre).split(' / '))[0], \
                                                                        str(audiofile.tag.recording_date),\
                                                                        image,\
                                                                        name[1]
    print(mp3_data)