import cv2
import numpy as np

# 读取图片
image = cv2.imread('E:\\Pycharm Program\\openCV\\photo\\111.png')
cv2.imshow('source', image)
cv2.waitKey(0)
#  转换为灰度图
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image_gray', image_gray)
cv2.waitKey(0)

# 二值化处理
# 并利用OTsU方法方法寻找最合适的阈值
# 处理后的图像命名为 dst1
t1 , dst1 = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('dst1', dst1)
cv2.waitKey(0)

# 去除噪点
# 采用开运算，先腐蚀再膨胀。这里的核k（kernel）采用4x4的像素块，我试了一下，3x3的状态下处理不干净
k = np.ones((4,4),np.uint8)
# 腐蚀，处理后的图像命名 dst2 ，iterations默认为1
dst2 = cv2.erode(dst1 , k , iterations=1)
# 膨胀，处理后的图像命名 dst3 ，iterations默认为1
dst3 = cv2.dilate(dst2, k , iterations=1)

# 保存并显示结果
cv2.imwrite('E:\\Pycharm Program\\photo\\1.png', dst3)
cv2.imshow('Final', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()


