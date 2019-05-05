# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt


def bitwise():
    img1 = cv2.imread('E://Open_cv/testimg/img003.jpg')
    img2 = cv2.imread('E://Open_cv/testimg/opencv_logo.jpg')
    # 获取img2（较小的图片）尺寸、纬度
    rows, cols, channels = img2.shape
    # 对img1按照img尺寸截取
    roi = img1[0:rows, 0:cols]
    #===创建掩膜===#
    # 将图片转换为灰度图
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  #
    # 将灰度图片进行二值化
    ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
    #     ret,mask1 = cv2.threshold(img2gray,190,255,cv2.THRESH_BINARY_INV)  #二值化取反
    # 对图像进行按位计算取反(颠倒黑白)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst
    # plt.subplot(131), plt.imshow(mask_inv, 'gray'), plt.title('img1_bg')
    # plt.subplot(132), plt.imshow(img2_fg, 'gray'), plt.title('img2_fg')
    # plt.subplot(133), plt.imshow(dst, 'gray'), plt.title('dst')
    cv2.imshow('res', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    bitwise()