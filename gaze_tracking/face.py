#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/5/10

import cv2
import dlib


class Face(object):
    def __init__(self,faces):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None
        self.face_detect(faces)

    def face_detect(self,faces):
        self.left = faces.left()
        self.top = faces.top()
        self.right = faces.right()
        self.bottom = faces.bottom()


if __name__ == '__main__':
    img = cv2.imread('C:\\Users\\asus.LAPTOP-KN1PDDA4\\Pictures\\bilibili\\3.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    detector = dlib.get_frontal_face_detector()
    faces = detector(img_gray, 1)

    for index, face in enumerate(faces):
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0))
    cv2.imwrite('E:\\timg1.jpg', img)
