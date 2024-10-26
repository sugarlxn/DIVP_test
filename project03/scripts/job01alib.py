#!/usr/bin/python3 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def binarize_image(image, threshold=128):
    """
    将图像转为二值图像
    :param image: PIL图像对象
    :param threshold: 二值化阈值
    :return: 二值化后的图像
    """
    
    image = image.convert('L')  # 转为灰度图
    binary_image = np.zeros_like(image)
    binary_image = np.array(image) > threshold  # 二值化
    return binary_image.astype('bool')

def apply_structuring_element(binary_image, structuring_element, operation='dilation'):
    """
    对二值图像应用结构元，进行膨胀或腐蚀操作
    :param binary_image: 二值图像
    :param structuring_element: 结构元
    :param operation: 'dilation'膨胀 或 'erosion'腐蚀
    :return: 处理后的二值图像
    """
    output_image = np.zeros_like(binary_image)
    se_center = (structuring_element.shape[0] // 2, structuring_element.shape[1] // 2)
    rows, cols = binary_image.shape
    
    for i in range(se_center[0], rows - se_center[0]):
        for j in range(se_center[1], cols - se_center[1]):
            region = binary_image[i - se_center[0]:i + se_center[0] + 1, j - se_center[1]:j + se_center[1] + 1]
            if operation == 'dilation':
                output_image[i, j] = np.any(region & structuring_element)
            elif operation == 'erosion':
                output_image[i, j] = np.all(region | ~structuring_element)
    
    return np.array(output_image).astype('bool')

# 膨胀操作
def dilate(binary_image, structuring_element, times=1):
    # 对二值图像进行膨胀操作
    for i in range(times):
        binary_image = apply_structuring_element(binary_image, structuring_element, 'dilation')
    return binary_image

# 腐蚀操作
def erode(binary_image, structuring_element, times=1):
    for i in range(times):
        binary_image = apply_structuring_element(binary_image, structuring_element, 'erosion')
    return binary_image

# 形态学开运算
def open_image(binary_image, structuring_element, times = 1):
    # 先腐蚀后膨胀
    eroded_image = erode(binary_image, structuring_element, times=times)
    dilate_image = dilate(eroded_image, structuring_element, times=times)
    return dilate_image

# 形态学闭运算
def close_image(binary_image, structuring_element, times = 1):
    # 先膨胀后腐蚀
    dilate_image = dilate(binary_image, structuring_element, times=times)
    eroded_image = erode(dilate_image, structuring_element, times=times)
    return eroded_image

# 击中击不中操作
def hit_or_miss(binary_image, structuring_element1, structuring_element2, times=1):
    """
    实现击中击不中操作
    :param binary_image: 二值图像
    :param structuring_element1: 击中部分的结构元
    :param structuring_element2: 击不中部分的结构元
    :return: 击中击不中后的二值图像
    """
    hit = erode(binary_image, structuring_element1, times=times)
    miss = erode(~binary_image, structuring_element2, times=times)
    # hit 与 miss 异或操作
    # return hit ^ miss
    return hit & ~miss

# 将numpy数组转为PIL图像
def to_pil_image(binary_image: np.array )-> Image:
    """
    将二值numpy数组转回PIL图像
    """
    return Image.fromarray((binary_image * 255).astype(np.uint8))