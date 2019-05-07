# -*- coding: utf-8 -*-
"""
Created on 2019/05/07
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

def medianblur():
    '''
    :param src
    :param ksize
    :return:
    '''
    img = cv2.imread('./testimg/img001.jpg')
    dst = cv2.medianBlur(img,3)
    plt.imshow(dst)
    plt.show()

medianblur()












