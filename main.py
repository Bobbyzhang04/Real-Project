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
                if audio_file.tag.album_artist == None:
                    audio_file.tag.album_artist = 'unknownartist'
                    
                    
                    
                    if os.path.exists('/Users/snoopbob/Music/unknownartist'):
                        os.chdir('/Users/snoopbob/Music/unknownartist')
                        if audio_file.tag.album == None:
                            if os.path.exists(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)):
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
                            elif not os.path.exists(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)):
                                path = '/Users/snoopbob/Music/unknownartist/%s' % (
                                    audio_file.tag.album)
                                os.mkdir(path, 0o0755)
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
                    elif not os.path.exists(
                            '/Users/snoopbob/Music/unknownartist'):
                        path = '/Users/snoopbob/Music/unknownartist'
                        os.mkdir(path, 0o0755)
                        os.chdir('/Users/snoopbob/Music/unknownartist')
                        if audio_file.tag.album == None:
                            if os.path.exists(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)):
                                os.chdir(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                    (audio_file.tag.album))
                            elif not os.path.exists(
                                    '/Users/snoopbob/Music/unknownartist/%s' %
                                (audio_file.tag.album)):
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
