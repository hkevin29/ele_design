#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/6/3

import sys
import cv2
from deepgaze.motion_detection import DiffMotionDetector
from deepgaze.mask_analysis import BinaryMaskAnalyser
from motion_detect.ex_diff_motion_detection import diff_motion_detect
from motion_detect.process import infor_write
from PyQt5.QtWidgets import QApplication, QWidget

# 界面设计中需要返回一个屏幕宽度的变量
####################
# 创建应用程序和对象
# app = QApplication(sys.argv)
# desktop = QApplication.desktop()
# screenRect = desktop.screenGeometry()
# height = screenRect.height()
# width = screenRect.width()
####################

# 读取视频文件
video_capture = cv2.VideoCapture("./video/test.mp4")
# 获取视频的帧率
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')  # 确定opencv的版本号
if int(major_ver) < 3:
    fps = video_capture.get(cv2.cv.CV_CAP_PROP_FPS)
else:
    fps = video_capture.get(cv2.CAP_PROP_FPS)

# 读取首帧
ret, frame = video_capture.read()

# number表示视频的第几帧
number = 1

# 设计对象my_motion_detector和首帧的比较背景
my_motion_detector = DiffMotionDetector()
my_motion_detector.setBackground(frame)

# Declaring the binary mask analyser object
my_mask_analyser = BinaryMaskAnalyser()

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # 输出可视化文件位置
# out = cv2.VideoWriter("./video/test_deepgaze.avi", fourcc, 20.0, (1920, 1080))

# Create the main window and move it
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('video', height, width)
cv2.moveWindow('Video', 20, 20)
is_first_frame = True

deadline_tim = 1  # 第一个时间检测截止时间
biggest_area = [0, 0, 0, 0]  # 统计每个区域出现的次数, 分别为全局、左、中、右

# 首先检测要写入的文件是否为空，不为空则清空
with open('information.txt', 'w+') as f:
    f.seek(0)
    temp0 = f.readline()
    if temp0 == ' ':
        pass
    else:
        f.truncate(0)

while True:
    # 读帧
    ret, frame = video_capture.read()

    if not ret:
        break
    # 进行检测并得出区域信息
    area = diff_motion_detect(my_motion_detector, my_mask_analyser, frame)

    # 帧数加一
    number += 1

    # 写入区域信息
    biggest_area = infor_write(number, fps, area, biggest_area)

    # # 写入输出视频文件
    # out.write(frame)

    # 显示图片
    cv2.imshow('Video', frame)  # show on window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Exit when Q is pressed

# Release the camera
video_capture.release()
print("Bye...")

if __name__ == '__main__':
    video = cv2.VideoCapture("video/test.mp4")

    # 确定opencv的版本号
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    video.release()
