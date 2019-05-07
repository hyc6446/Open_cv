# -*- coding: utf-8 -*-
"""
Created on 2019/05/06
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 2D卷积
def filter2d():

    '''
    :param src :原图源
    :param ddepth ：目标图像深度
    :param kernel ：卷积核
    :return:
    '''
    img= cv2.imread('./testimg/98hf.jpg')
    kernel = np.ones((2,2),np.float32)/4

    dst = cv2.filter2D(img,-1,kernel)

    plt.subplot(121),plt.imshow(img),plt.title('img')
    plt.subplot(122),plt.imshow(dst),plt.title('dst')
    plt.show()

if __name__ =="__main__":
    filter2d()



















