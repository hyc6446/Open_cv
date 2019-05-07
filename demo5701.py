# -*- coding: utf-8 -*-
"""
Created on 2019/05/06
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#otsu 最大方差（大律法）针对直方图为双峰图
def otsu():
    '''
    :param
    :return:
    '''
    img = cv2.imread('./testimg/img006.jpg',0)
    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    gsblurimg = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(gsblurimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    blurimg = cv2.blur(img,(3,3))
    ret4,th4 = cv2.threshold(blurimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    mdblurimg =cv2.medianBlur(img,3)
    ret5,th5 = cv2.threshold(mdblurimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    plt.subplot(231),plt.imshow(img),plt.title('img')
    plt.subplot(232),plt.imshow(th1),plt.title('th1')
    plt.subplot(233),plt.imshow(th2),plt.title('th2')
    plt.subplot(234),plt.imshow(th3),plt.title('th3')
    plt.subplot(235),plt.imshow(th4),plt.title('th4')
    plt.subplot(236),plt.imshow(th5),plt.title('th5')
    plt.show()

if __name__ == "__main__":
    otsu()



