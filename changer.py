#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from random import choice
from subprocess import Popen


def back_drop_change():
    link = "/usr/share/slim/themes/default/background.jpg"
    images = os.environ["HOME"] + "/pictures/apod/"
    os.remove(link)
    image_selection = [images + f for _, _, fi in os.walk(images) for f in fi]
    bck_img = choice(image_selection)
    Popen(["ln", "-s", bck_img, link])

if __name__ == "__main__":
    back_drop_change() 
