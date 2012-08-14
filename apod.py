#!/usr/bin/env python
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

class Apod:
    def apod_wallpaper(self):
        self.soup = BeautifulSoup(urlopen('http://apod.nasa.gov/').read())
        self.pic = self.soup.find('img')
        spot = str(self.pic).find('jpg')
        back = spot + str(self.pic)[spot:].find('"')
        with open('/home/oberon/Pictures/daily', 'wb') as pic_folder:
            pic_folder.write(urlopen('http://apod.nasa.gov/' + str(self.pic)[10:back]).read())
        pic_folder.close()
        return 


Apod().apod_wallpaper()
 




