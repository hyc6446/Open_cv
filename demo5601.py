# -*- coding: utf-8 -*-
"""
Created on 2019/05/06
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#简单阈值
def threshold():
    '''
    :param src :图像源
    :param thresh ：阈值
    :param maxval ：高于(低于)阈值被赋予的新值
    :param type ：阈值方法
    :return:
    '''
    img = cv2.imread('./testimg/img001.jpg')
    ret,thresh = cv2.threshold(img,175,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(img,175,255,cv2.THRESH_BINARY_INV)
    ret3,thresh3 = cv2.threshold(img,240,255,cv2.THRESH_TRUNC)
    ret4,thresh4 = cv2.threshold(img,175,255,cv2.THRESH_TOZERO)
    ret5,thresh5 = cv2.threshold(img,175,0,cv2.THRESH_TOZERO_INV)
    plt.subplot(231),plt.imshow(thresh),plt.title('thresh')
    plt.subplot(232),plt.imshow(thresh2),plt.title('thresh2')
    plt.subplot(233),plt.imshow(thresh3),plt.title('thresh3')
    plt.subplot(234),plt.imshow(thresh4),plt.title('thresh4')
    plt.subplot(235),plt.imshow(thresh5),plt.title('thresh5')
    plt.show()


if __name__ == "__main__":
    threshold()





