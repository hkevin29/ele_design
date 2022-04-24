#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/6/5

import math
import cv2
from gaze_tracking import GazeTracking


def eye_tracking(gaze, frame, p_ref, d_ref):
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)
    # # 对帧进行标注
    # frame = gaze.annotated_frame()

    # 确定注视区域
    if gaze.is_left():
        area_looking = 1
    elif gaze.is_center():
        area_looking = 2
    elif gaze.is_right():
        area_looking = 3
    else:
        area_looking = 0

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    try:
        # 像素距离
        pixel_distance = math.hypot((left_pupil[0] - right_pupil[0]), (left_pupil[1] - right_pupil[1]))
        # 实际距离
        distance = (p_ref / pixel_distance) * d_ref
    except Exception:
        distance = None

    # 返回 frame表示处理后的帧， area_looking 表示注视区域, distance表示人脸距离屏幕的距离
    return gaze.face, frame, area_looking, distance