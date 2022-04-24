#!/usr/bin/env python

import numpy as np
import cv2
from timeit import default_timer as timer
from deepgaze.motion_detection import DiffMotionDetector
from deepgaze.mask_analysis import BinaryMaskAnalyser


# 将显著性区域映射为三个分区
def salient_area(frame, x, y, w, h):
    center = np.array([x + w / 2, y + h / 2])  # 显著性区域的中心点
    if center[0] <= frame.shape[1]/3:
        # 认为处于左区域1
        return 1
    elif center[0] <= 2 * frame.shape[1] / 3:
        # 认为处于中区域2
        return 2
    elif center[0] <= frame.shape[1]:
        # 认为处于右区域3
        return 3
    else:
        # 认为处于全局区域
        return 0


def diff_motion_detect(my_motion_detector, my_mask_analyser, frame):
    frame_mask = my_motion_detector.returnMask(frame)
    if (my_mask_analyser.returnNumberOfContours(frame_mask) > 0):  # 如果算法检测到存在显著性区域
        background_image = frame
        my_motion_detector.setBackground(background_image)  # 重新设置背景图
        x, y, w, h = my_mask_analyser.returnMaxAreaRectangle(frame_mask)  # 返回显著性区域的坐标

        cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 2)  # 框出显著性区域

        area = salient_area(frame, x, y, w, h)  # 返回区域值

        return area
    else:
        return 0  # 返回全局区域


if __name__ == '__main__':

    pass
