#!/usr/bin/env python3
import os
from PIL import Image
#the script and the images dir are in same dir
k = os.listdir('./images')
for i in k:
    o = os.path.splitext(i)[0]
    try:
        with Image.open('./images/'+i).convert('RGB') as im:
            im.thumbnail((128,128))
            im.rotate(270).save('/opt/icons/'+o,'jpeg')
    except OSError:
        print('OSError')
