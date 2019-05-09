# -*- coding: utf-8 -*-
"""
Created on 2019/05/09
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#边界检测
def nothing(x):
    print(x)
    img = cv2.imread('./testimg/Lena.jpg', 0)
    dst = cv2.Canny(img, 100, 200)


def canny():
    '''
    :param src:图像源
    :param threshold1:最小阈值 （非极大值抑制）
    :param threshold2:最大阈值 （非极大值抑制）
    :return: dst
    '''
    img = cv2.imread('./testimg/Lena.jpg',0)
    dst = cv2.Canny(img,100,200)

    cv2.namedWindow('dst')
    cv2.createTrackbar('minval','dst',0,127,nothing)
    cv2.createTrackbar('maxval','dst',127,255,nothing)
    switch= '0:OFF\n1:On'
    cv2.createTrackbar(switch,'dst',0,1,nothing)
    stat= True
    while(1):

        cv2.imshow('dst',dst)
        k=cv2.waitKey(1)&0xFF
        if k==27:
            break
        minval = cv2.getTrackbarPos('minval', 'dst')
        maxval = cv2.getTrackbarPos('maxval', 'dst')
        s = cv2.getTrackbarPos(switch,'dst')

        dst= cv2.Canny(img,minval,maxval)
    cv2.destroyAllWindows()

canny()