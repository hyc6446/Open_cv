# -*- coding: utf-8 -*-
"""
Created on 2019/05/05
@author: hyc6446

"""
import numpy as np
from matplotlib import pyplot as plt
import cv2


def ronghe():
    img1 = cv2.imread('E://Open_cv/testimg/img004.jpg')
    img = cv2.imread('E://Open_cv/testimg/img005.jpg')
    rows,cols,channel = img1.shape
    img2 = cv2.resize(img,(cols,rows),interpolation=cv2.INTER_AREA)
    newimg = cv2.addWeighted(img1, 0.4, img2, 0.6, 50)
    cv2.imshow('newimg', newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


ronghe()