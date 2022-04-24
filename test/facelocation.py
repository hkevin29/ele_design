#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author: lihua time:2021/5/12


import face_recognition as fr
import cv2
import numpy as np
import dlib
import time
import math
import sys

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
POINTS_NUM_LANDMARK = 68


def _largest_face(dets):
    if len(dets) == 1:
        return 0

    face_areas = [(det.right() - det.left()) * (det.bottom() - det.top()) for det in dets]

    largest_area = face_areas[0]
    largest_index = 0
    for index in range(1, len(dets)):
        if face_areas[index] > largest_area:
            largest_index = index
            largest_area = face_areas[index]

    print("largest_face index is {} in {} faces".format(largest_index, len(dets)))

    return largest_index


def get_image_points_from_landmark_shape(landmark_shape):
    if landmark_shape.num_parts != POINTS_NUM_LANDMARK:
        print("ERROR:landmark_shape.num_parts-{}".format(landmark_shape.num_parts))
        return -1, None
    image_points = np.array([
        (landmark_shape.part(30).x, landmark_shape.part(30).y),
        (landmark_shape.part(8).x, landmark_shape.part(8).y),
        (landmark_shape.part(36).x, landmark_shape.part(36).y),
        (landmark_shape.part(45).x, landmark_shape.part(45).y),
        (landmark_shape.part(48).x, landmark_shape.part(48).y),
        (landmark_shape.part(54).x, landmark_shape.part(54).y)
    ], dtype="double")

    return 0, image_points


def get_image_points(img):
    # gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    dets = detector(img, 0)

    if 0 == len(dets):
        print("ERROR: found no face")
        return -1, None
    largest_index = _largest_face(dets)
    face_rectangle = dets[largest_index]

    landmark_shape = predictor(img, face_rectangle)

    return get_image_points_from_landmark_shape(landmark_shape)


def get_pose_estimation(img_size, image_points):
    model_points = np.array([
        (0.0, 0.0, 0.0),  # Nose tip
        (0.0, -330.0, -65.0),  # Chin
        (-225.0, 170.0, -135.0),  # Left eye left corner
        (225.0, 170.0, -135.0),  # Right eye right corne
        (-150.0, -150.0, -125.0),  # Left Mouth corner
        (150.0, -150.0, -125.0)  # Right mouth corner

    ])

    focal_length = img_size[1]
    center = (img_size[1] / 2, img_size[0] / 2)
    camera_matrix = np.array(
        [[focal_length, 0, center[0]],
         [0, focal_length, center[1]],
         [0, 0, 1]], dtype="double"
    )

    print("Camera Matrix :{}".format(camera_matrix))

    dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
    (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix,
                                                                  dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

    print("Rotation Vector:\n {}".format(rotation_vector))
    print("Translation Vector:\n {}".format(translation_vector))
    return success, rotation_vector, translation_vector, camera_matrix, dist_coeffs


def get_euler_angle(rotation_vector):
    # calculate rotation angles
    theta = cv2.norm(rotation_vector, cv2.NORM_L2)

    # transformed to quaterniond
    w = math.cos(theta / 2)
    x = math.sin(theta / 2) * rotation_vector[0][0] / theta
    y = math.sin(theta / 2) * rotation_vector[1][0] / theta
    z = math.sin(theta / 2) * rotation_vector[2][0] / theta

    ysqr = y * y
    # pitch (x-axis rotation)
    t0 = 2.0 * (w * x + y * z)
    t1 = 1.0 - 2.0 * (x * x + ysqr)
    print('t0:{}, t1:{}'.format(t0, t1))
    pitch = math.atan2(t0, t1)

    # yaw (y-axis rotation)
    t2 = 2.0 * (w * y - z * x)
    if t2 > 1.0:
        t2 = 1.0
    if t2 < -1.0:
        t2 = -1.0
    yaw = math.asin(t2)

    # roll (z-axis rotation)
    t3 = 2.0 * (w * z + x * y)
    t4 = 1.0 - 2.0 * (ysqr + z * z)
    roll = math.atan2(t3, t4)

    print('pitch:{}, yaw:{}, roll:{}'.format(pitch, yaw, roll))

    Y = int((pitch / math.pi) * 180)
    X = int((yaw / math.pi) * 180)
    Z = int((roll / math.pi) * 180)

    return 0, Y, X, Z


def get_pose_estimation_in_euler_angle(landmark_shape, im_szie):
    try:
        ret, image_points = get_image_points_from_landmark_shape(landmark_shape)
        if ret != 0:
            print('get_image_points failed')
            return -1, None, None, None

        ret, rotation_vector, translation_vector, camera_matrix, dist_coeffs = get_pose_estimation(im_szie,
                                                                                                   image_points)
        if ret != True:
            print('get_pose_estimation failed')
            return -1, None, None, None

        ret, pitch, yaw, roll = get_euler_angle(rotation_vector)
        if ret != 0:
            print('get_euler_angle failed')
            return -1, None, None, None

        euler_angle_str = 'Y:{}, X:{}, Z:{}'.format(pitch, yaw, roll)
        print(euler_angle_str)
        return 0, pitch, yaw, roll

    except Exception as e:
        print('get_pose_estimation_in_euler_angle exception:{}'.format(e))
        return -1, None, None, None


if __name__ == '__main__':

    img = cv2.imread('C:\\Users\\asus.LAPTOP-KN1PDDA4\\Pictures\\bilibili\\3.jpg')
    size = img.shape

    if size[0] > 700:
        h = size[0] / 3
        w = size[1] / 3
        img = cv2.resize(img, (int(w), int(h)), interpolation=cv2.INTER_CUBIC)
        size = img.shape

    ret, image_points = get_image_points(img)
    if ret != 0:
        print('get_image_points failed')
    ret, rotation_vector, translation_vector, camera_matrix, dist_coeffs = get_pose_estimation(size, image_points)
    if ret != True:
        print('get_pose_estimation failed')

    ret, pitch, yaw, roll = get_euler_angle(rotation_vector)
    image = fr.load_image_file(filepath)
    facelocation = fr.face_locations(image, 1)
    for t, r, b, l in facelocation:
        top = t
        left = l
        width = r - l
        height = b - t

    yaw_angle = yaw
    pitch_angle = pitch
    roll_angle = roll
    x = img.size[0]
    max = x * 0.85
    min = x * 0.55
    if width > max:
        ret.append({"distance": -1})
    elif width < min:
        ret.append({"distance": 1})
    else:
        ret.append({"distance": 0})

    if yaw_angle < 10 and yaw_angle > -10 and roll_angle < 10 and roll_angle > -10 and pitch_angle < 10 and pitch_angle > -10:
        ret.append({"angle": "ok"})
    else:
        ret.append({"angle": "no"})

    print(json.dumps(ret))

