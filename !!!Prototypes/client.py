import requests
import json
import os
import shutil

def get_req():
    s = requests.get('https://retrowave.ru/api/v1/tracks?cursor=1&limit=1')
    data = s.json()
    print('JSON: ', data)
    print('\nGET: ', s)
    title = str(data['body']['tracks'][0]['title']).strip()
    audio = str(data['body']['tracks'][0]['streamUrl']).strip()
    pic = str(data['body']['tracks'][0]['artworkUrl']).strip()
    return title, audio, pic

def download(title, audio, pic):
    os_path = 'd://retrowave.ru/'
    retrowave = 'https://retrowave.ru'
    os.makedirs(os_path + title)
    (dirname, filename) = os.path.split(retrowave + pic)
    mp3 = requests.get(retrowave + audio, stream = True)
    jpg = requests.get(retrowave + pic, stream = True)
    print(mp3.status_code)
    print(jpg.status_code)
    if mp3.status_code == 200 and jpg.status_code == 200:
        with open(os_path + title + '/' + title + '.mp3', 'wb') as fileOS:
            mp3.raw.decode_content = True
            shutil.copyfileobj(mp3.raw, fileOS)
        with open(os_path + title + '/' + filename, 'wb') as filePIC:
            jpg.raw.decode_content = True
            shutil.copyfileobj(jpg.raw, filePIC)
    print('Files are downloaded')

download(*get_req())