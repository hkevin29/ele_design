from __future__ import division
import os
import cv2
import dlib
from .eye import Eye
from .calibration import Calibration
from .face import Face
import math


class GazeTracking(object):
    """
    This class tracks the user's gaze.
    It provides useful information like the position of the eyes
    and pupils and allows to know if the eyes are open or closed
    """

    def __init__(self):
        self.frame = None
        self.face = None
        self.eye_left = None
        self.eye_right = None
        self.calibration = Calibration()

        # _face_detector is used to detect faces
        self._face_detector = dlib.get_frontal_face_detector()

        # _predictor is used to get facial landmarks of a given face
        cwd = os.path.abspath(os.path.dirname(__file__))
        model_path = os.path.abspath(os.path.join(cwd, "trained_models/shape_predictor_68_face_landmarks.dat"))
        self._predictor = dlib.shape_predictor(model_path)

    @property
    def pupils_located(self):
        """Check that the pupils have been located"""
        try:
            int(self.eye_left.pupil.x)
            int(self.eye_left.pupil.y)
            int(self.eye_right.pupil.x)
            int(self.eye_right.pupil.y)
            return True
        except Exception:
            return False

    def _analyze(self):
        """Detects the face and initialize Eye objects"""
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self._face_detector(frame)

        try:
            self.face = Face(faces[0])

            landmarks = self._predictor(frame, faces[0])
            self.eye_left = Eye(frame, landmarks, 0, self.calibration)
            self.eye_right = Eye(frame, landmarks, 1, self.calibration)

        except IndexError:
            self.face = None
            self.eye_left = None
            self.eye_right = None

    def refresh(self, frame):
        """Refreshes the frame and analyzes it.

        Arguments:
            frame (numpy.ndarray): The frame to analyze
        """
        self.frame = frame
        self._analyze()

    def pupil_left_coords(self):
        """Returns the coordinates（坐标） of the left pupil"""
        if self.pupils_located:
            x = self.eye_left.origin[0] + self.eye_left.pupil.x
            y = self.eye_left.origin[1] + self.eye_left.pupil.y
            return (x, y)

    def pupil_right_coords(self):
        """Returns the coordinates of the right pupil"""
        if self.pupils_located:
            x = self.eye_right.origin[0] + self.eye_right.pupil.x
            y = self.eye_right.origin[1] + self.eye_right.pupil.y
            return (x, y)

    # horizontal_ratio 确定左边、右边、中间
    def horizontal_ratio(self):
        if self.pupils_located:
            pupil_left_dist = math.hypot((self.eye_left.pupil.x - self.eye_left.center[0]), (self.eye_left.pupil.y - self.eye_left.center[1]))
            pupil_right_dist = math.hypot((self.eye_right.pupil.x - self.eye_right.center[0]), (self.eye_right.pupil.y - self.eye_right.center[1]))
            if pupil_left_dist - pupil_right_dist > 1:
                main_pupil = 1
            elif pupil_right_dist - pupil_left_dist > 1:
                main_pupil = 2
            else:
                main_pupil = 0
            return main_pupil
            # pupil_left = self.eye_left.pupil.x / (self.eye_left.center[0] * 2 - 10)
            # pupil_right = self.eye_right.pupil.x / (self.eye_right.center[0] * 2 - 10)
            # return (pupil_left + pupil_right) / 2

    def is_right(self):
        """Returns true if the user is looking to the right"""
        if self.pupils_located:
            return self.horizontal_ratio() == 2

    def is_left(self):
        """Returns true if the user is looking to the left"""
        if self.pupils_located:
            return self.horizontal_ratio() == 1

    def is_center(self):
        """Returns true if the user is looking to the center"""
        if self.pupils_located:
            return self.horizontal_ratio() == 0
            # self.is_right() is not True and self.is_left() is not True

    # def is_blinking(self):
    #     """Returns true if the user closes his eyes"""
    #     if self.pupils_located:
    #         blinking_ratio = (self.eye_left.blinking + self.eye_right.blinking) / 2
    #         return blinking_ratio > 3.8

    def annotated_frame(self):
        """Returns the main frame with pupils face and eyes highlighted"""
        frame = self.frame.copy()

        if self.face:
            cv2.rectangle(frame, (self.face.left, self.face.top), (self.face.right, self.face.bottom), (0, 255, 0))
        if self.eye_left:
            cv2.rectangle(frame, self.eye_left.origin, self.eye_left.end, (0, 0, 255))
            cv2.line(frame, (int((self.eye_left.origin[0] + self.eye_left.end[0])/2), self.eye_left.origin[1]),
                     (int((self.eye_left.origin[0] + self.eye_left.end[0])/2), self.eye_left.end[1]), (0, 0, 255))
            cv2.line(frame, (self.eye_left.origin[0], int((0.6 * self.eye_left.origin[1] + 0.4 * self.eye_left.end[1]))),
                     (self.eye_left.end[0], int((0.6 * self.eye_left.origin[1] + 0.4 * self.eye_left.end[1]))), (0, 0, 255))
        if self.eye_right:
            cv2.rectangle(frame, self.eye_right.origin, self.eye_right.end, (0, 0, 255))
            cv2.line(frame, (int((self.eye_right.origin[0] + self.eye_right.end[0]) / 2), self.eye_right.origin[1]),
                     (int((self.eye_right.origin[0] + self.eye_right.end[0]) / 2), self.eye_right.end[1]), (0, 0, 255))
            cv2.line(frame, (self.eye_right.origin[0], int((0.6 * self.eye_right.origin[1] + 0.4 * self.eye_right.end[1]))),
                     (self.eye_right.end[0], int((0.6 * self.eye_right.origin[1] + 0.4 * self.eye_right.end[1]))), (0, 0, 255))

        if self.pupils_located:
            color = (0, 255, 0)
            x_left, y_left = self.pupil_left_coords()
            x_right, y_right = self.pupil_right_coords()
            cv2.line(frame, (x_left - 5, y_left), (x_left + 5, y_left), color)
            cv2.line(frame, (x_left, y_left - 5), (x_left, y_left + 5), color)
            cv2.line(frame, (x_right - 5, y_right), (x_right + 5, y_right), color)
            cv2.line(frame, (x_right, y_right - 5), (x_right, y_right + 5), color)

        return frame
