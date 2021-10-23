import random
import os
import numpy as np
import cv2
from PIL import Image
from PIL import  ImageFile
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import glob

import time
import xml.etree.ElementTree as ET


imagepath="D:/github desktop/daihu-ye.github.io/resources/PersonalInformation/photos/rawimage"
imgsavepath="D:/github desktop/daihu-ye.github.io/resources/PersonalInformation/photos/resized/"

for name in os.listdir(imagepath):
    if(name.split(".")[-1]=="jpg"):
        print(name)
        img=Image.open(imagepath+name)
        out=img.resize((84,127))
        out.save(imgsavepath+name)
