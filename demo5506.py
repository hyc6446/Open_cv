# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#图像旋转
def matrix():
    '''
    :param pic 图像源
    :param M( center 旋转中心,angle 选择角度,scale 缩放因子)
    :param dsize 变换后图像尺寸
    :return: 变幻后图像
    '''
    img = cv2.imread('./testimg/img001.jpg')
    rows,cols = img.shape[:2]
    M=cv2.getRotationMatrix2D((cols/2,rows/2),-90,0.9)

    res = cv2.warpAffine(img,M,(cols,rows))
    plt.subplot(121),plt.imshow(img),plt.title('img')
    plt.subplot(122),plt.imshow(res),plt.title('res')
    plt.show()
if __name__ == '__main__':
    matrix()