# -*- coding: utf-8 -*-
"""
Created on 2019/05/08
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#膨胀与腐蚀相反
def dilate():
    '''
    :param
    :return:
    '''
    img = cv2.imread('./testimg/j.png')
    ret,nimg = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3),np.uint8)
    dst = cv2.dilate(nimg,kernel)
    plt.subplot(121),plt.imshow(img)
    plt.subplot(122),plt.imshow(dst)
    plt.show()


dilate()