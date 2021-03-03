# OpenCV Colour detection Test

import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

# https://stackoverflow.com/questions/52083797/opencv-detecting-color-ranges-and-display-on-console

# https://stackoverflow.com/questions/60051941/find-the-coordinates-in-an-image-where-a-specified-colour-is-detected

# ASK RYAN ABOUT ONLY DETECTING COLOUR IN CERTIAN RANGE - FOR EXAMPLE BOX IN CENTER OF SCREEN
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red Colour
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    # Blue Colour
    low_blue = np.array([90, 60, 0])
    high_blue = np.array([121, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_red, high_red)

    # Display Camera
    cv2.putText(frame, 'Rubiks Cube Solver - v1.0', (10, 1050), font, 1, (200,200,200), 2, cv2.LINE_AA)

    cv2.rectangle(frame, (725, 300), (825, 400), (255, 0, 0), 2)
    # Center of each colour
    color = frame[775, 350]  # row major, like in opencv
    print("Color at 100x100: ", (color[0] << 16) + (color[1] << 8) + (color[2]))
    center_x = print((725 + 825) / 2)
    center_y = print((300 + 400) / 2)


    cv2.rectangle(frame, (900, 300), (1000, 400), (255, 0, 0), 2)
    cv2.rectangle(frame, (1085, 300), (1185, 400), (255, 0, 0), 2)

    cv2.rectangle(frame, (725, 500), (825, 600), (255, 0, 0), 2)
    cv2.rectangle(frame, (900, 500), (1000, 600), (255, 0, 0), 2)
    cv2.rectangle(frame, (1085, 500), (1185, 600), (255, 0, 0), 2)

    cv2.rectangle(frame, (725, 700), (825, 800), (255, 0, 0), 2)
    cv2.rectangle(frame, (900, 700), (1000, 800), (255, 0, 0), 2)
    cv2.rectangle(frame, (1085, 700), (1185, 800), (255, 0, 0), 2)


    cv2.imshow("blue mask", blue_mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break



#    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])