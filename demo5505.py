# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
#平移
def warpAffine():
    '''
    :param src :图像源
    :param M : 移动距离矩阵(2x3) 可以说会用numpy np.float32格式构建
    :param dsize: 生成的新图像尺寸 元组格式
    :return: 新图像
    '''
    img = cv2.imread('./testimg/img001.jpg')
    moveSize = np.float32([[1,0,50],[0,1,50]])
    rows,cols = img.shape[:2]
    res = cv2.warpAffine(img,moveSize,(rows,cols))

    plt.subplot(121),plt.imshow(img),plt.title('img')
    plt.subplot(122),plt.imshow(res),plt.title('res')
    plt.show()


if __name__ == "__main__":
    warpAffine()