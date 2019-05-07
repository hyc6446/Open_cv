# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#透视变换
def warpPerspective():
    '''
    :param src :图像源
    :param M getPerspectiveTransform（pts1,pts2）np.float32格式2x4矩阵
    :param dsize ：变换后的尺寸
    :return:
    '''
    img=cv2.imread('./testimg/dabai.png')
    rows,cols=img.shape[:2]
    pts1=np.float32([[300,0],[500,0],[300,200],[500,200]])
    pts2=np.float32([[0,0],[200,0],[0,200],[200,200]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    res = cv2.warpPerspective(img,M,(200,200))

    plt.subplot(121),plt.imshow(img),plt.title('img')
    plt.subplot(122),plt.imshow(res),plt.title('res')
    plt.show()


if __name__ == '__main__':
    warpPerspective()