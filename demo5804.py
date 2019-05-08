# -*- coding: utf-8 -*-
"""
Created on 2019/05/08
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
#开运算与闭运算
def morphology():
    '''
    :param src ：图像源
    :param op ：运算方式
    :param kernel ：卷积核尺寸
    :return: dst :新图像源
    '''
    img=cv2.imread('./testimg/98hf.jpg',cv2.IMREAD_GRAYSCALE)
    nimg = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,13,0)
    nimg = cv2.medianBlur(nimg,3)
    ret,limg = cv2.threshold(img,230,255,cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(nimg,cv2.MORPH_OPEN,kernel)
    closeing = cv2.morphologyEx(limg,cv2.MORPH_CLOSE,kernel)
    plt.subplot(311),plt.imshow(limg)
    plt.subplot(312),plt.imshow(opening)
    plt.subplot(313),plt.imshow(closeing)
    plt.show()




morphology()