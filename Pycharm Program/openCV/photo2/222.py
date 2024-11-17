#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np


# 读取图像
img = cv2.imread('E:\\Pycharm Program\\openCV\\photo2\\222.jpg')

# 将图像从 BGR 转换为 HSV 颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义黄色的范围
min_yellow = np.array([20, 190, 140])
max_yellow = np.array([25, 255, 255])

# 创建黄色的掩码
mask_yellow = cv2.inRange(hsv, min_yellow, max_yellow)

# 将黄色区域标记为红色
img[mask_yellow > 0] = [0, 0, 255]

cv2.imshow('step1', img)

#第一个黄色的路障和后面两个路障的黄色不同，所以我先处理后面两个处在阴影里的路障，再把前面处于阳光下的路障标红
#一下步骤重复前面的，对min_yellow进行了调整
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

min_yellow = np.array([23, 89, 212])
max_yellow = np.array([25, 255, 255])

mask_yellow = cv2.inRange(hsv, min_yellow, max_yellow)

img[mask_yellow > 0] = [0, 0, 255]

cv2.imwrite('E:\\Pycharm Program\\openCV\\photo2\\2.jpg', img)
cv2.imshow('step2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



