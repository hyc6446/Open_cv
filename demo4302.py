# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img_path= './testimg/003.jpg'
img = cv2.imread(img_path,0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()











