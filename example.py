"""
此为算法测试文件
不用详细了解
"""
import math
import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()

# p_ref为参考值在手机成像的距离(pixel) d_ref为参考值与屏幕的距离(cm)
p_ref = 81
d_ref = 52

def main1():
    webcam = cv2.VideoCapture(0)

    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)
        # 对帧进行标注
        frame = gaze.annotated_frame()
        text = ""

        if gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 255, 0), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        try:
            # 像素距离
            pixel_distance = math.hypot((left_pupil[0] - right_pupil[0]), (left_pupil[1] - right_pupil[1]))
            # 实际距离
            distance = (p_ref / pixel_distance) * d_ref
        except Exception:
            distance = None
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 1)
        cv2.putText(frame, "Distance: " + str(distance), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 1)

        cv2.imshow("Demo", frame)

        if cv2.waitKey(1) == 27:
            break

if __name__ == '__main__':

    main1()
