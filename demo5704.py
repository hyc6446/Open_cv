# -*- coding: utf-8 -*-
"""
Created on 2019/05/06
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#
def boxfilter():
    '''
    :param src:图像源
    :param ddepth ：目标图像深度
    :param dsize ：卷积核尺寸
    :param normalize：是否使用卷积框归一化 如果为true则与blur（均值滤波）效果相同
    :return: dst
    '''
    img = cv2.imread('./testimg/opencv_logo.jpg')
    dst = cv2.boxFilter(img,-1,(3,3),normalize=False)

    plt.imshow(dst)
    plt.show()

boxfilter()