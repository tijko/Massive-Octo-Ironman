#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup

class Apod(object):

    def __init__(self):
        page = requests.get('http://apod.nasa.gov')
        soup = BeautifulSoup(page.text)
        link = soup.findAll('a')[1]
        link = str(link)
        link = link[link.find('"') + 1:]
        link = link[:link.find('"')]
        image_link = 'http://apod.nasa.gov/' + link
        with open('/home/oberon/Pictures/daily', 'wb') as pic_folder:
            image = requests.get(image_link)
            pic_folder.write(image.content)    
        pic_folder.close()
        return

if __name__ == '__main__':
    apd = Apod
    apd()

