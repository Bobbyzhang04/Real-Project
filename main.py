import eyed3
import os
import os.path


def get_all_file_path(my_path):
    only_files = [
        f for f in os.listdir(my_path)
        if os.path.isfile(os.path.join(my_path, f))
    ]
    return only_files


def music():
    all_file_path = get_all_file_path('/Users/snoopbob/Downloads')
    i = 0
    while i < len(all_file_path):
        mp3_filename = all_file_path[i]
        split_filename = os.path.splitext(mp3_filename)
        file_ext = str.lower(split_filename[1])
        if file_ext == '.mp3':
            audio_file = eyed3.load('/Users/snoopbob/Downloads/%s' %
                                    (all_file_path[i]))
            if audio_file.tag == None:
                pass
                # TODO: Use API
            else:
                if audio_file.tag.album_artist == None:
                    audio_file.tag.album_artist = 'unknown_artist'
                artist_filepath = '/Users/snoopbob/Music/%s' % (audio_file.tag.album_artist)
                if not os.path.exists(artist_filepath):
                    os.mkdir(artist_filepath)
                if audio_file.tag.album == None:
                    audio_file.tag.album = 'unknown_album'
                album_filepath = '%s/%s' % (artist_filepath, audio_file.tag.album)
                if not os.path.exists(album_filepath):
                    os.mkdir(album_filepath)
                download_mp3_filepath = '/Users/snoopbob/Downloads/%s' % (mp3_filename)
                music_mp3_filepath = '%s/%s' % (album_filepath, mp3_filename)
                while os.path.exists(music_mp3_filepath):
                    music_mp3_filepath = '%s %d' % (music_mp3_filepath, 1)
                os.rename(download_mp3_filepath, music_mp3_filepath)
        i = i + 1


def main():
    music()


if __name__ == '__main__':
    main()
