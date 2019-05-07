# -*- coding: utf-8 -*-
"""
Created on 2019/05/06
@author: hyc6446

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#自适应阈值
def adaptive():
    '''
    :param src: 原图像源
    :param maxValue ：超过阈值被赋予的新值
    :param adaptiveMethod： 阈值计算方法
    :param thresholdType：二值化操作类型
    :param blockSize：图片分块大小
    :param C： 计算权重的常数项
    :return: dst 新图源
    '''
    img = cv2.imread('./testimg/98hf.jpg',cv2.IMREAD_GRAYSCALE)
    nimg = cv2.medianBlur(img,3)
    ret,th1 = cv2.threshold(nimg,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(nimg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(nimg,1,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)


    plt.subplot(231),plt.imshow(img),plt.title('img')
    plt.subplot(232),plt.imshow(nimg),plt.title('nimg')
    plt.subplot(233),plt.imshow(th1),plt.title('th1')
    plt.subplot(234),plt.imshow(th2),plt.title('th2')
    plt.subplot(235),plt.imshow(th3),plt.title('th3')
    plt.show()


if __name__=="__main__":
    adaptive()



