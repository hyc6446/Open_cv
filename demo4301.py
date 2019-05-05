# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""
import numpy as np
import cv2

img_path= './testimg/001.jpg'
img = cv2.imread(img_path,0)
cv2.imshow('img002',img)
k = cv2.waitKey(0)&0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('./testimg/img002.jpg',img)
    cv2.destroyAllWindows()
