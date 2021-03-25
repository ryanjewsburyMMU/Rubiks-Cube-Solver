# OpenCV Colour detection Test

import cv2
import time
import numpy as np
import webcolors

import gui_test

# import segmentation
# import scanCube
# import first_attempt
# import RubiksCube
# image = cv2.imread("./venv/data/image2.bmp")
# import CubeScanner
# # https://stackoverflow.com/questions/52083797/opencv-detecting-color-ranges-and-display-on-console
#
# # https://stackoverflow.com/questions/60051941/find-the-coordinates-in-an-image-where-a-specified-colour-is-detected
#
# # Collect data of colours
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# # cv2.imshow("Frame", image[:, :, 0])
#
#
# # gap top = 160
# cv2.rectangle(image, (480, 200), (530, 250), (192, 192, 192), thickness=3)
# cv2.rectangle(image, (615, 200), (665, 250), (192, 192, 192), thickness=3)
# cv2.rectangle(image, (750, 200), (800, 250), (192, 192, 192), thickness=3)
#
# cv2.rectangle(image, (480, 335), (530, 385), (192, 192, 192), thickness=3)
# cv2.rectangle(image, (615, 335), (665, 385), (192, 192, 192), thickness=3)
# cv2.rectangle(image, (750, 335), (800, 385), (192, 192, 192), thickness=3)
#
# cv2.rectangle(image, (480, 470), (530, 520), (192, 192, 192), thickness=3)
# cv2.rectangle(image, (615, 470), (665, 520), (192, 192, 192), thickness=3)
# cv2.rectangle(image, (750, 470), (800, 520), (192, 192, 192), thickness=3)
#
# # gab bottom = 160
#
#
#
# cv2.imshow("Frame", image)
#
#
# # Testing Cropped Image
#
# # Top Layer
# # Top Left
# cv2.imshow("Top Left", image[200:250, 480:530, :])
# print("Top Left: ", np.median(image[200:250, 480:530,:], axis=(0,1)))
#
# # Top Center
# cv2.imshow("Top Middle", image[200:250, 615:665, :])
# print("Top Center: ",np.median(image[200:250, 615:665,:], axis=(0,1)))
#
# # Top Center
# cv2.imshow("Top Right", image[200:250, 750:800, :])
# # print("Top Right: ", np.median(image[200:250, 750:800,:], axis=(0,1)))
#
#
# # Center Section
#
# # Center left
# cv2.imshow("Center Left", image[335:385, 480:530, :])
# # print("Center Left: ",np.median(image[335:385, 615:665,:], axis=(0,1)))
#
# # Center Piece
# cv2.imshow("Center Piece", image[335:385, 615:665, :])
# # print("Center Piece: ",np.median(image[335:385, 615:665,:], axis=(0,1)))
#
# # Center Right
# cv2.imshow("Center Right", image[335:385, 750:800, :])
# # print("Center Right: ",np.median(image[335:385, 750:800,:], axis=(0,1)))
#
#
# # Bottom left
# cv2.imshow("Bottom Left", image[470:520, 480:530, :])
# # print("Bottom Left: ",np.median(image[470:520, 615:665,:], axis=(0,1)))
#
# # Bottom Piece
# cv2.imshow("Bottom Piece", image[470:520, 615:665, :])
# # print("Bottom Center: ",np.median(image[470:520, 615:665,:], axis=(0,1)))
#
# # Bottom Right
# cv2.imshow("Bottom Right", image[470:520, 750:800, :])
# # print("Bottom Right: ", np.median(image[470:520, 750:800,:], axis=(0,1)))
#
#
#
#
# cv2.waitKey(1000000)
#
# key = cv2.waitKey(1)
#
#
#
#
