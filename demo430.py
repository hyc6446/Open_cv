# -*- coding: utf-8 -*-
"""
Created on 2019/04/30
@author: hyc6446

"""
import numpy as np
import  cv2

img_bath= './testimg/001.jpg'

#读取图片
img = cv2.imread(img_bath,0)

#显示图像
cv2.namedWindow('im001',cv2.WINDOW_NORMAL)
cv2.imshow('im001',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#保存图像
cv2.imwrite('./testimg/save001.jpg',img)
print(img)
