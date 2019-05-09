# -*- coding: utf-8 -*-
"""
Created on 2019/05/08
@author: hyc6446

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

def sobel():
    '''
    Laplaction(拉普拉斯):
    :param src:图像源
    :param ddepth:图像深度cv2.CV_64F(求二阶导)
    :param ksize:算子大小
    Sobel:
    :param src：图像源
    :param ddepth: 图像深度
    :param dx:有0，1，2三个参数表示在X方向求导，最大求二阶导
    :param dy:有0，1，2三个参数表示在Y方向求导，最大求二阶导
    :param ksize:算子大小
    :return: dst: 新图源
    '''
    img = cv2.imread('./testimg/Lena.jpg')
    gaus = cv2.GaussianBlur(img,(3,3),0)
    gray= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    sobelx= cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
    sobely= cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
    x_cv8u= cv2.convertScaleAbs(sobelx)
    y_cv8u= cv2.convertScaleAbs(sobely)
    result= cv2.addWeighted(x_cv8u,0.5,y_cv8u,0.5,0)
    laplaction= cv2.convertScaleAbs(cv2.Laplacian(gray,cv2.CV_64F,ksize=3))
    cv2.imshow('lpls',laplaction)
    cv2.imshow('result',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title('img'),plt.xticks([]),plt.yticks([])
    # plt.subplot(222),plt.imshow(laplaction,cmap='gray'),plt.title('laplaction'),plt.xticks([]),plt.yticks([])
    # plt.subplot(223),plt.imshow(x_cv8u,cmap='gray'),plt.title('sobelx'),plt.xticks([]),plt.yticks([])
    # plt.subplot(224),plt.imshow(sobely,cmap='gray'),plt.title('sobely'),plt.xticks([]),plt.yticks([])

    # plt.show()




sobel()


