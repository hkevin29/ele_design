#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/5/10

import numpy as np
import matplotlib as plt
import cv2

img = np.zeros((1080, 1920, 3), np.uint8)
area1 = np.array([[250, 200], [300, 100], [750, 800], [100, 1000]])
area2 = np.array([[1000, 200], [1500, 200], [1500, 400], [1000, 400]])

new_img = cv2.fillPoly(img, [area1, area2], (255, 255, 255))

cv2.imshow("Image", img)
cv2.waitKey (0)