#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from os import environ
from BeautifulSoup import BeautifulSoup


class Apod(object):

    def __init__(self):
        apod = 'http://apod.nasa.gov/'
        page = requests.get(apod)
        soup = BeautifulSoup(page.text)
        try:
            link = soup.findAll('img')[0]['src']
            image_link = apod + link
            path = link.replace('/', '-')
            with open(environ['HOME'] + '/pictures/apod/' + path, 'wb') as pic_folder:
                image = requests.get(image_link)
                pic_folder.write(image.content)    
        except IndexError:
            pass

if __name__ == '__main__':
    Apod()
