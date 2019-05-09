# -*- coding: utf-8 -*-
"""
Created on 2019/05/09
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt
#图像金字塔
def octave():
    '''
    pyrUp（src）:向下
    pyrDown(src):向上
    :param src :图像源
    :return: dst
    '''
    img=cv2.imread('./testimg/Lena.jpg',0)
    lower_reso= cv2.pyrDown(img)
    higher_reso = cv2.pyrUp(img)
    higher_reso2 = cv2.pyrUp(lower_reso)
    img_reso= img-higher_reso2
    cv2.imshow('img',img)
    # cv2.imshow('down',lower_reso)
    # cv2.imshow('up',higher_reso)
    # cv2.imshow('down-up',higher_reso2)
    cv2.imshow('down-up',img_reso)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

octave()