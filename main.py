import eyed3

def music():
    with open('name.artist.album.mp3') as music_info_file:
    #dont know how to get matadata
        music_info = []
        for line in user_info_file:
            split_line = line.split(',')
            album = split_line[2].replace('\n', '')
            artist = split_line[1].replace('\n', '')
            song_name = split_line[0]
            music = {
                'album': album,
                'artist': artist,
                'song_name': song_name,
            }
            music_info.append(music)
    i = 0
    while i < len(artist_list):#dont know how to create a artist list
        if artist_list[i] == music_info['artist']:
            j = 0
            while j < len(album_list):
                if album_list[j] == music_info['album']:
                    k = 0
                    while k < len(song_list):
                        if album_list[k] == music_info['song_name']:
                            music_info['song_name'] = music_info['song_name'].append('1')
                        else:
                            song_list.append(#thatsong)
                else:
                    