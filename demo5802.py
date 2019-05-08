# -*- coding: utf-8 -*-
"""
Created on 2019/05/08
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

#腐蚀（针对白色/取结构元素覆盖下的原图像素较小值）
def erode():
    '''
    :param src :图像源
    :param kernel ：卷积核尺寸(结构元素)
    :return: dst
    '''
    img=cv2.imread('./testimg/j.png')
    ret,nimg = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3),np.uint8)
    dst = cv2.erode(nimg,kernel)
    plt.subplot(121),plt.imshow(nimg),plt.title('img')
    plt.subplot(122),plt.imshow(dst),plt.title('dst')
    plt.show()

erode()


