# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""
import numpy as np
from matplotlib import pyplot as plt
import cv2

img_path= './testimg/img003.png'
img = cv2.imread(img_path)
# imgpx = img[120,70]
# print(imgpx)
# blue = img[100,100,0]
#维度
print(img.shape) # reutrn 行,列,通道
#维数
print(img.ndim)
#像素数目
print(img.size)
#图像数据类型
print(img.dtype)

ball = img[120:240,330:450]#(y,x)
img[100:220,100:220] = ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()