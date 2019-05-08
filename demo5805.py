# -*- coding: utf-8 -*-
"""
Created on 2019/05/08
@author: hyc6446

"""
import numpy as np
import cv2
import pytesseract as tess
from matplotlib import pyplot as plt

def tidu():
    '''
    :param src
    :return:
    '''
    img = cv2.imread('./testimg/code/001.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3,3),np.uint8)
    ret,nimg = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
    nimg = cv2.GaussianBlur(nimg,(3,3),0)
    gradient = cv2.morphologyEx(nimg,cv2.MORPH_OPEN,kernel)
    text = tess.image_to_string(gradient)
    print(text)
    cv2.imshow('gradient',gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
tidu()

