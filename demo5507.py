# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#仿射变换
def transform():
    '''
    :param src :图像源
    :param M仿射变换因子getAffineTransform(pts1,pts2),pts1,pts2np.float32格式2x3矩阵
    :param dsize 变换后图像尺寸
    :return:
    '''
    img = cv2.imread('./testimg/img001.jpg')
    rows,cols = img.shape[:2]
    pts1=np.float32([[50,50],[100,50],[50,100]])
    pts2=np.float32([[50,10],[100,100],[50,50]])
    M=cv2.getAffineTransform(pts1,pts2)
    res=cv2.warpAffine(img,M,(cols,rows))

    plt.subplot(121),plt.imshow(img),plt.title('img')
    plt.subplot(122),plt.imshow(res),plt.title('res')
    plt.show()



if __name__ =='__main__':
    transform()