# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

imgpath= './testimg/img003.png'
img = cv2.imread(imgpath)
# b,g,r = cv2.split(img)#效率没有numpy操作块
# img = cv2.merge(b,g,r)
b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2]

# img[:,:,2] = 0
# img[:,:,1] = 0
img = np.where(img>235,0,img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

