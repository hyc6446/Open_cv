# -*- coding: utf-8 -*-
"""
Created on 2019/05/06
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#均值滤波（模糊）
def blur():
    '''
    :param src:图像源
    :param ksize：卷积(矩阵)核 np.float32格式的 np.ones(?x?)的矩阵
    :return: dst 新的图像
    '''
    img = cv2.imread('./testimg/opencv_logo.jpg')
    blur = cv2.blur(img,(5,5))

    plt.imshow(blur)
    plt.show()


blur()















