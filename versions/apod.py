#!/usr/bin/env python

from os import environ
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


class Apod(object):

    def apod_wallpaper(self):
        self.soup = BeautifulSoup(urlopen('http://apod.nasa.gov/').read())
        self.pic = self.soup.find('img')
        spot = str(self.pic).find('jpg')
        back = spot + str(self.pic)[spot:].find('"')
        with open(os.environ['HOME'] + '/Pictures/daily', 'wb') as pic_folder:
            pic_folder.write(urlopen('http://apod.nasa.gov/' + 
                                      str(self.pic)[10:back]).read())
        return 

if __name__ == '__main__':
    ap = Apod()
    ap.apod_wallpaper()
 
