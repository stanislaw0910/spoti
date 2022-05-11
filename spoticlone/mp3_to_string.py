import os
import glob
import eyed3


# this script takes main information from mp3 file tags and create tuple of strings for using in DB


def duration_from_seconds(s):
    s = s
    m, s = divmod(s, 60)
    timelapse = "{:01d}:{:02d}".format(int(m), int(s))
    return timelapse


def main_func(work_dir='media'):
    cwd = os.getcwd()
    os.chdir(os.path.join(os.getcwd(), work_dir))
    mp3_dir=[]
    for file in glob.glob("*.mp3"):
        mp3_dir.append((file, os.path.abspath(file)))
    mp3_dir.sort()
    song_list = []
    os.chdir(cwd)
    f = open('soundlist.txt', 'w')
    os.chdir(work_dir)
    album_duration = 0
    for name in mp3_dir:
        audiofile = eyed3.load(name[0])
        eyed3.log.setLevel("ERROR")

        duration = str(int(audiofile.info.time_secs))
        mp3_data = audiofile.tag.artist, \
                   audiofile.tag.album, \
                   audiofile.tag.title, \
                   str(audiofile.tag.track_num[0]), \
                   duration, \
                   tuple(str(audiofile.tag.genre).split(' / '))[0], \
                   str(audiofile.tag.recording_date), \
                   name[1], \
                   audiofile.tag.images[0].image_data
        f.write(','.join(mp3_data[:-1]) + '\n')
        song_list.append(mp3_data[:-1])
    f.close()
    print(song_list)
    print(duration_from_seconds(album_duration))
if __name__ == "__main__":
    main_func()
