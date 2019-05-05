# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""
import numpy as np
from matplotlib import pyplot as plt
import cv2

imgpath= './testimg/img001.jpg'
img = cv2.imread(imgpath)
replicate = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,0,0])

plt.subplot(2,3,1),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect_101,'gray'),plt.title('reflect_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
plt.show()



