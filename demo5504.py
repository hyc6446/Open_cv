# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import cv2
import numpy as np

#图像缩放
def resize():
    '''
    :param img: 图像源
    :param dsize：缩放尺寸（与fx,fy设置一个即可）
    :param fx：x轴缩放因子
    :param fy：Y轴缩放因子
    :param interpolation：插值方法
    :return: img
    '''

    img = cv2.imread("./testimg/img001.jpg")
    res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

    h,w = img.shape[:2]
    res1 = cv2.resize(img,(w*3,h*3),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('res',res)
    cv2.imshow('res1',res1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    resize()