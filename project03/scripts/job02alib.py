#!/usr/bin/python3 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def grayscale_erode_one_time(image, structuring_element):
    """
    灰度腐蚀操作 一次
    :param image: 输入灰度图像，类型为numpy数组
    :param structuring_element: 结构元，类型为numpy数组
    :return: 腐蚀后的灰度图像
    """
    se_center = (structuring_element.shape[0] // 2, structuring_element.shape[1] // 2)
    padded_image = np.pad(image, ((se_center[0],), (se_center[1],)), mode='edge')
    eroded_image = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + structuring_element.shape[0], j:j + structuring_element.shape[1]]
            eroded_image[i, j] = np.min(region - structuring_element) #生成版本
            # FIXME: 以下是错误的代码 could not work 没想明白(+_+)?
            # region_flap = region.flatten() 
            # se_flap = structuring_element.flatten()
            # for i in range(len(se_flap)):
            #     if se_flap[i] == 0:
            #         region_flap[i] = 255
            # eroded_image[i, j] = np.min(region_flap)
    
    return eroded_image

def grayscale_erode(image, structuring_element, times = 1):
    """
    灰度腐蚀操作
    :param image: 输入灰度图像，类型为numpy数组
    :param structuring_element: 结构元，类型为numpy数组
    :param times: 腐蚀次数
    :return: 腐蚀后的灰度图像
    """
    for i in range(times):
        image = grayscale_erode_one_time(image, structuring_element)
    return image

def grayscale_dilate_one_time(image, structuring_element):
    """
    灰度膨胀操作 一次
    :param image: 输入灰度图像，类型为numpy数组
    :param structuring_element: 结构元，类型为numpy数组
    :return: 膨胀后的灰度图像
    """
    se_center = (structuring_element.shape[0] // 2, structuring_element.shape[1] // 2)
    padded_image = np.pad(image, ((se_center[0],), (se_center[1],)), mode='edge')
    dilated_image = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + structuring_element.shape[0], j:j + structuring_element.shape[1]]
            dilated_image[i, j] = np.max(region + structuring_element) 
            # FIXME: 以下是错误的代码 could not work, 没想明白(+_+)?
            # region_flap = region.flatten()
            # se_flap = structuring_element.flatten()
            # for i in range(len(se_flap)):
            #     if se_flap[i] == 0:
            #         region_flap[i] = 0
            # dilated_image[i, j] = np.max(region_flap)

    return dilated_image

def grayscale_dilate(image, structuring_element, times = 1):
    """
    灰度膨胀操作
    :param image: 输入灰度图像，类型为numpy数组
    :param structuring_element: 结构元，类型为numpy数组
    :param times: 膨胀次数
    :return: 膨胀后的灰度图像
    """
    for i in range(times):
        image = grayscale_dilate_one_time(image, structuring_element)
    return image

def grayscale_open(image, structuring_element, times = 1):
    """
    灰度开运算
    :param image: 输入灰度图像，类型为numpy数组
    :param structuring_element: 结构元，类型为numpy数组
    :return: 开运算后的灰度图像
    """
    eroded = grayscale_erode(image, structuring_element, times)
    opened_image = grayscale_dilate(eroded, structuring_element, times)
    return opened_image

def grayscale_close(image, structuring_element, times = 1):
    """
    灰度闭运算
    :param image: 输入灰度图像，类型为numpy数组
    :param structuring_element: 结构元，类型为numpy数组
    :return: 闭运算后的灰度图像
    """
    dilated = grayscale_dilate(image, structuring_element, times)
    closed_image = grayscale_erode(dilated, structuring_element, times)
    return closed_image

