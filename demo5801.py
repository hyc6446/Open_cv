# -*- coding: utf-8 -*-
"""
Created on 2019/05/08
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#高斯双边滤波 (保持边界清晰的情况下降噪）美颜
def bilateral():
    '''
    :param src :图像源
    :param d ：像素邻域直径
    :param sigmaColor ：空间高斯函数(颜色空间)方差尽量大
    :param sigmaSpace：灰度值相似性高斯函数(坐标空间)方差尽量小/区别边界
    :return:
    '''
    img=cv2.imread('./testimg/img008.jpg')
    dst = cv2.bilateralFilter(img,0,75,15)
    cv2.imshow('img',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bilateral()






