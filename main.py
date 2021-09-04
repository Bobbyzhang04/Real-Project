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
        split_filename = os.path.splitext(all_file_path[i])
        file_ext = str.lower(split_filename[1])
        if file_ext == '.mp3':
            audio_file = eyed3.load('/Users/snoopbob/Downloads/%s' %
                                    (all_file_path[i]))
            if audio_file.tag == None:
                pass
                # TODO: Use API
            else:
                print(audio_file.tag.album)
                print(audio_file.tag.album_artist)
                print(audio_file.tag.title)
                print(audio_file.tag.track_num)
                if audio_file.tag.album_artist == None:
                    if os.path.exist(
                            '/Users/snoopbob/Music/unknownartist') == True:
                        os.chdir('/Users/snoopbob/Music/unknownartist')
                        if audio_file.tag.album == None:
                            if os.path.exist(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)) == True:
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
                            elif os.path.exist(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)) == False:
                                path = '/Users/snoopbob/Music/unknownartist/%s' % (
                                    audio_file.tag.album)
                                os.mkdir(path, 0o0755)
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
                    elif os.path.exist(
                            '/Users/snoopbob/Music/unknownartist') == False:
                        path = '/Users/snoopbob/Music/unknownartist'
                        os.mkdir(path, 0o0755)
                        os.chdir('/Users/snoopbob/Music/unknownartist')
                        if audio_file.tag.album == None:
                            if os.path.exist(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)) == True:
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
                            elif os.path.exist(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)) == False:
                                path = '/Users/snoopbob/Music/unknownartist/%s' % (
                                    audio_file.tag.album)
                                os.mkdir(path, 0o0755)
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
        i = i + 1


def main():
    music()


if __name__ == '__main__':
    main()
