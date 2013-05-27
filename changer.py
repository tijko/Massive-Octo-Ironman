#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import choice
from subprocess import Popen


def back_drop_change():
    link = "/usr/share/slim/themes/default/background.jpg"
    os.remove(link)
    image_selection = list()
    for di, _, fi in os.walk("/home/triton/pictures/apod"):
        for f in fi:
            image_selection.append(di + "/" + f)
    bck_img = choice(image_selection)
    Popen(["ln", "-s", bck_img, link])

if __name__ == "__main__":
    back_drop_change() 
