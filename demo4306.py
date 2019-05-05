# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""
from matplotlib import pyplot as plt
import numpy as np
import cv2

imgpath= './testimg/001.jpg'
img = cv2.imread(imgpath)
img1 = cv2.imread('./testimg/img003.jpg')
img2 = cv2.imread('./testimg/img003_1.jpg')
#图像相加
def cv2add():
    newimg = cv2.add(img,255)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#图像混合权重计算
def cv2addWeighted():
    dst = cv2.addWeighted(img1,0.3,img2,0.7,0)
    cv2.imshow('dst',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#图像按位运算
def bitwise():
    img1 = cv2.imread('./testimg/python_logo.jpg')
    img2 = cv2.imread('./testimg/opencv_logo.jpg')
    rows,cols,channels = img2.shape
    roi = img1[0:rows,0:cols]

    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,mask = cv2.threshold(img2gray,180,255,cv2.THRESH_BINARY)
    # ret, thresh2 = cv2.threshold(img2gray, 127, 255, cv2.THRESH_BINARY_INV)
    # ret, thresh3 = cv2.threshold(img2gray, 127, 255, cv2.THRESH_TRUNC)
    # ret, thresh4 = cv2.threshold(img2gray, 127, 255, cv2.THRESH_TOZERO)
    # ret, thresh5 = cv2.threshold(img2gray, 127, 255, cv2.THRESH_TOZERO_INV)
    # titles = ['img2','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    # imgs=[img2,mask, thresh2, thresh3, thresh4, thresh5,]
    # for i in range(6):
    #     plt.subplot(2,3,i+1),plt.imshow(imgs[i],'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    # plt.show()
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
    img2_bg = cv2.bitwise_and(img2,img2,mask=mask_inv)
    print(roi)
    #
    dst = cv2.add(img1_bg,img2_bg)
    img1[0:rows,0:cols]=dst

    # cv2.imshow('res',img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()




if __name__ =="__main__":
    bitwise()





