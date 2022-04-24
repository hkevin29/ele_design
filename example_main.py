#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/6/5

import math
import cv2
from gaze_tracking import GazeTracking
from gaze_tracking.tracking import eye_tracking
import time
# 眼动追踪对象
gaze = GazeTracking()
# p_ref为参考值在手机成像的距离(pixel) d_ref为参考值与屏幕的距离(cm)
p_ref, d_ref = 81, 52

# 获取摄像头
webcam = cv2.VideoCapture(0)


def example_main0():
        global face
        global area_looking
        # 获取帧
        _, frame = webcam.read()

        # face表示是否有人脸存在，frame表示处理后的帧， area_looking 表示注视区域, distance表示人脸距离屏幕的距离
        face, frame, area_looking, distance = eye_tracking(gaze, frame, p_ref, d_ref)

        #全局变量赋值
        #print("test:{}".format(all_area_looking))
        #print("test:{}".format(all_face))


        # 显示图片
        cv2.putText(frame, str(area_looking), (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 255, 0), 2)
        cv2.imshow("Demo", frame)
        # if cv2.waitKey(1) == 27:
        #     break
def example_main():
    while (True):
        example_main0()
        # time.sleep(1)  # 每一秒执行一次
        # print("当前注视区域是：{}".format(area_looking))
        # if (face == None):
        #     print("未检测到人脸")
        # else:
        #     print("有人脸")
        if cv2.waitKey(1) == 27:
            break
if __name__ == '__main__':
    example_main()
    # time.sleep(1) #每一秒执行一次
    # print("当前注视区域是：{}".format(area_looking))
    # if(face==None):
    #   print("未检测到人脸")
    # else:
    #    print("有人脸")