#!/usr/bin/python3 
import cv2
import numpy as np
print("Hello, World!")

root_path = '/root/DIVP_project/'
image_path = "project01/scripts/1.jpg"

#读取图片如果图片是彩色的，则同时显示三基色分量图像
img = cv2.imread(root_path+image_path, cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

