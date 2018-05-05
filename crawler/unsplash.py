#-*-encoding:utf-8-*-
import os, shutil
import requests
from bs4 import BeautifulSoup
import json
import threading

Url = 'https://unsplash.com/'
Start = 'https://unsplash.com/napi/feeds/home?after=95cc4cd0-4529-11e8-8080-8001050033a3'
Pattern = 'https://unsplash.com/napi/feeds/home?after=xxx'
Auth = {'Authorization':'Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09'}
Des = 'data'
Pages = 50


def GetJson(target):
    req = requests.get(target, headers=Auth, verify=False)
    if req.status_code == 200:
        return req.json()
    else:
        print('response error: ', req.status_code)

def SavePhoto(photo, regular_size=True):
    target = photo['m_size']
    if not regular_size:
        target = photo['l_size']
    req = requests.get(target, headers=Auth, verify=False)
    file = os.path.join(Des, photo['name'])
    file = file + '.jpg'
    with open(file, 'wb') as f:
        f.write(req.content)

if __name__ == '__main__':
    os.chdir(os.curdir)
    if not os.path.exists(Des):
        os.mkdir(Des)

    js = GetJson(Start)
    cur_page = 1
    while cur_page < Pages:
        print('saving page: ', cur_page)
        after_value = js['next_page'].split('=')[1]
        next_target = Pattern.replace('xxx', after_value)
        photos = []
        for photo in js['photos']:
            pt = {}
            pt['id'] = photo['id']
            pt['m_size'] = photo['urls']['regular']
            pt['l_size'] = photo['urls']['full']

            pt['name'] = photo['id']
            photos.append(pt)
        threads = [threading.Thread(target=SavePhoto, args=(photo, )) for photo in photos]
        for t in threads:
            t.start()
        # for t in threads:
        #     t.join()
        js = GetJson(next_target)
        cur_page += 1
