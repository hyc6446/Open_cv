# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import cv2
import numpy as np

def getHSV():
    co = np.uint8([[[37,233,37]]])
    print(cv2.cvtColor(co,cv2.COLOR_BGR2HSV))
    img = cv2.imread("E://Open_cv/testimg/img006.jpg")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_black = np.array([110,100,100])
    upper_black = np.array([130,255,255])
    lower_pick = np.array([140,100,100])
    upper_pick = np.array([160,255,255])
    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])
    mask_blue = cv2.inRange(hsv,lower_black,upper_black)
    mask_pick = cv2.inRange(hsv,lower_pick,upper_pick)
    mask_green = cv2.inRange(hsv,lower_green,upper_green)
    res_blue=cv2.bitwise_and(img,img,mask=mask_blue)
    res_pick = cv2.bitwise_and(img,img,mask=mask_pick)
    res_green = cv2.bitwise_and(img,img,mask=mask_green)
    res = res_blue+res_pick+res_green
    cv2.imshow('mask',hsv)
    # cv2.imshow('res',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def getMyColor():
    co = np.uint8([[[0,255,0]]])
    hsv_color = cv2.cvtColor(co,cv2.COLOR_BGR2HSV)
    print(hsv_color)

    img = cv2.imread('E://Open_cv/testimg/python_logo.jpg')
    #将图片转换成HSV格式（灰度图）
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #设置查找物体的阈值
    lower_black = np.array([50,100,100])
    upper_black = np.array([70,255,255])
    #根据阈值构建掩膜
    mask = cv2.inRange(hsv,lower_black,upper_black)
    #将原图和掩膜进行按位与计算
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('res',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    getMyColor()