# -*- coding: utf-8 -*-
"""
Created on 2019/05/07
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#中值模糊（用于去除椒盐噪点）
def medianblur():
    '''
    :param src
    :param ksize
    :return:
    '''
    img = cv2.imread('./testimg/img007.jpg')
    dst = cv2.medianBlur(img,9)
    cv2.imshow('img',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # plt.show()

medianblur()












