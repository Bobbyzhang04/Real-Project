import eyed3
import os
import os.path
import requests
import docx


def get_all_file_path(my_path):
    only_file_names = [
        f for f in os.listdir(my_path)
        if os.path.isfile(os.path.join(my_path, f))
    ]
    i = 0
    all_file_path = []
    while i < len(only_file_names):
        file_path = "%s/%s" % (my_path, only_file_names[i])
        all_file_path.append(file_path)
        i = i + 1
    return all_file_path


def music(source_file_path):
    audio_file = eyed3.load(source_file_path)
    if audio_file.tag == None:
        pass
    else:
        if audio_file.tag.album_artist == None:
            audio_file.tag.album_artist = 'unknown_artist'
        audio_file.tag.album_artist = audio_file.tag.album_artist.replace(
            '/', '-')
        artist_filepath = '/Users/snoopbob/Music/%s' % (
            audio_file.tag.album_artist)
        if not os.path.exists(artist_filepath):
            os.mkdir(artist_filepath)
        if audio_file.tag.album == None:
            audio_file.tag.album = 'unknown_album'
        audio_file.tag.album = audio_file.tag.album.replace('/', '-')
        album_filepath = '%s/%s' % (artist_filepath, audio_file.tag.album)
        if not os.path.exists(album_filepath):
            os.mkdir(album_filepath)
        download_mp3_filepath = source_file_path
        file_name = os.path.basename(source_file_path)
        music_mp3_filepath = '%s/%s' % (album_filepath, file_name)
        while os.path.exists(music_mp3_filepath):
            music_mp3_filepath = '%s %d' % (music_mp3_filepath, 1)
        os.rename(download_mp3_filepath, music_mp3_filepath)


def video(source_file_path):
    mp4_filename = os.path.basename(source_file_path)
    video_mp4_filepath = '/Users/snoopbob/Videos/%s' % (mp4_filename)
    while os.path.exists(video_mp4_filepath):
        video_mp4_filepath = '%s %d' % (video_mp4_filepath, 1)
    os.rename(source_file_path, video_mp4_filepath)


def others(source_file_path):
    others_folder = '/Users/snoopbob/Others'
    split_filename = os.path.basename(source_file_path)
    others_filepath = '%s/%s' % (others_folder, split_filename)
    while os.path.exists(others_filepath):
        others_filepath = '%s %d' % (others_filepath, 1)
    os.rename(source_file_path, others_filepath)


def images(source_file_path):
    api_key = 'acc_b580a33df0d99bb'
    api_secret = '508be5bf54a6c634ee73057797de606f'
    image_filename = os.path.basename(source_file_path)
    upload_info = requests.post(
        'https://api.imagga.com/v2/uploads',
        auth=(api_key, api_secret),
        files={'image': open(source_file_path, 'rb')})
    upload_info = upload_info.json()
    upload_id = upload_info["result"]["upload_id"]
    image_url = 'https://api.imagga.com/v2/categories/personal_photos?image_upload_id=%s' % (
        upload_id)
    image_catagory = requests.post(
        image_url,
        auth=(api_key, api_secret),
        files={'image': open(source_file_path, 'rb')})
    image_catagory = image_catagory.json()
    image_catagorization = image_catagory["result"]["categories"][0]["name"]["en"]
    destination_image_path = "/Users/snoopbob/Pictures/%s/%s" % (image_catagorization, image_filename)
    while os.path.exists(destination_image_path):
        destination_image_path = '%s %d' % (destination_image_path, 1)
    os.rename(source_file_path, destination_image_path)


def text(source_file_path):
    with open(source_file_path) as text:
        document_content = text.readlines()
    return document_content


def msword(source_file_path):
    # get data as one string
    document = docx.Document(source_file_path)
    document_content = ''
    i = 0
    while i < len(document.paragraphs):
        document_content = document_content + document.paragraphs[i].text
        i = i + 1
    return document_content


def categorize_keywords(keywords_list):
    math_science_keywords = [
      'angle',
      'triangle',
      'sqaure',
      'roots',
      'force',
      'mixture',
      'solution',
      'solvent',
      'reaction',
      'equilibrium',
      'speed',
      'acceleration',
      'atom',
      'equation',
      'differenciation',
      'integration',
    ]
    i = 0
    while i < len(keywords_list):
        if keywords_list[i] in math_science_keywords:
            return 'math_science'
        i = i + 1
    return 'everything_else'


def document(source_file_path):
    split_filename = os.path.splitext(source_file_path)
    file_ext = str.lower(split_filename[1])
    ms_ext=[
        '.doc',
        '.docx',
        '.ods',
        '.odt',
    ]
    if file_ext == '.txt':
        text_data = text()
    elif file_ext in ms_ext:
        text_data = msword()

    document_filename = os.path.basename(source_file_path)
    sm_api_key = '7FB201A31A'
    request_body = dict()
    request_body['sm_api_input'] = text_data
    url = "https://api.smmry.com?SM_API_KEY=%s" % (sm_api_key)
    response = requests.post(url, request_body)
    dict_response = response.json()
    keywords = dict_response['sm_api_keyword_array']
    doc_category = categorize_keywords(keywords)
    destination_document_path = "/Users/snoopbob/document/%s/%s" % (doc_category, document_filename)
    while os.path.exists(destination_document_path):
        destination_document_path = '%s %d' % (destination_document_path, 1)
    os.rename(source_file_path, destination_document_path)


def main():
    document_ext=[
        '.doc',
        '.docx',
        '.ods',
        '.odt',
        # '.html',
        # '.htm',
        # '.pdf',
        # '.xls',
        # '.xlsx',
        # '.ppt',
        # '.pptx',
        '.txt',
    ]
    video_ext = [
        '.mp4',
        '.mov',
        '.wmv',
        '.flv',
        '.avi',
        '.avchd',
        '.webm',
        '.mkv',
    ]
    music_ext = [
        '.wav',
        '.mp3',
    ]
    img_ext = [
        '.jpeg',
        '.jpg',
        '.png',
        '.apng',
        '.gif',
        '.jfif',
        '.pjpeg',
        '.pjp',
    ]
    others_ext = [
        '.zip', 
        '.7z', 
        '.msi', 
        '.exe',
    ]
    all_file_path = get_all_file_path('/Users/snoopbob/Downloads')
    i = 0
    while i < len(all_file_path):
        source_file_path = all_file_path[i]
        split_filename = os.path.splitext(source_file_path)
        file_ext = str.lower(split_filename[1])
        if file_ext in music_ext:
            music(source_file_path)
        elif file_ext in video_ext:
            video(source_file_path)
        elif file_ext in img_ext:
            images(source_file_path)
        elif file_ext in others_ext:
            others(source_file_path)
        elif file_ext in document_ext:
            document(source_file_path)
        i = i + 1


if __name__ == '__main__':
    main()
