# OpenCV Colour detection Test

import cv2
import time
import numpy as np
import webcolors

cap = cv2.VideoCapture(0)

# https://stackoverflow.com/questions/52083797/opencv-detecting-color-ranges-and-display-on-console

# https://stackoverflow.com/questions/60051941/find-the-coordinates-in-an-image-where-a-specified-colour-is-detected

blueArr = []


def appendToList(currentArr):
    currentArr = list(map(int, currentArr))
    blueArr.append(currentArr)
    print(blueArr)


white_mean = [207.06666667, 221.26666667, 231.02222222]
white_std = [9.21930342, 3.78828604, 6.72801403]

red_mean = [40.9, 33.73333333, 233.73333333]
red_std = [6.96028416, 11.89005186, 8.80883395]

yellow_mean = [79.06666667, 234.05555556, 216.5]
yellow_std = [3.58329457, 3.68287663, 8.28552955]

orange_mean = [50.98888889, 93.65555556, 253.1]
orange_std = [6.33946097, 9.57213678, 4.49209182]

green_mean = [100.96666667, 210.32222222, 10.21111111]
green_std = [5.83752231, 7.29052319, 14.46489578]

blue_mean = [111.81111111, 104.03333333, 96.55555556]
blue_std = [7.11320282, 11.0919891, 17.43439201]


def makePrediction(currentMean):
    colourResult = []
    # First calculate std for every one and take smallest index
    white_chance = np.sum((np.array(currentMean) - np.array(white_mean)) ** 2)
    colourResult.append(white_chance)

    red_chance = np.sum((np.array(currentMean) - np.array(red_mean)) ** 2)
    colourResult.append(red_chance)

    yellow_chance = np.sum((np.array(currentMean) - np.array(yellow_mean)) ** 2)
    colourResult.append(yellow_chance)

    orange_chance = np.sum((np.array(currentMean) - np.array(orange_mean)) ** 2)
    colourResult.append(orange_chance)

    green_chance = np.sum((np.array(currentMean) - np.array(green_mean)) ** 2)
    colourResult.append(green_chance)

    blue_chance = np.sum((np.array(currentMean) - np.array(blue_mean)) ** 2)
    colourResult.append(blue_chance)

    smallestValue = np.argmin(colourResult)

    if(smallestValue == 0 ):
        print("White")
        return "White"
    elif(smallestValue == 1):
        print("Red")
        return "Red"
    elif(smallestValue == 2):
        print("Yellow")
        return "Yellow"
    elif(smallestValue == 3):
        print("Orange")
        return "Orange"
    elif(smallestValue == 4):
        print("Green")
        return "Green"
    elif(smallestValue == 5):
        print("Blue")
        return "Blue"


font = cv2.FONT_HERSHEY_SIMPLEX

image_index = 0

while True:
    # print(image_index)
    filename = "blueImage" + str(image_index)
    ret, frame = cap.read()

    # pixel = frame[150, 150]
    # print(pixel)

    cv2.rectangle(frame, (480, 200), (530, 250), (192, 192, 192), thickness=3)
    cv2.rectangle(frame, (615, 200), (665, 250), (192, 192, 192), thickness=3)
    cv2.rectangle(frame, (750, 200), (800, 250), (192, 192, 192), thickness=3)

    cv2.rectangle(frame, (480, 335), (530, 385), (192, 192, 192), thickness=3)
    cv2.rectangle(frame, (615, 335), (665, 385), (192, 192, 192), thickness=3)
    cv2.rectangle(frame, (750, 335), (800, 385), (192, 192, 192), thickness=3)

    cv2.rectangle(frame, (480, 470), (530, 520), (192, 192, 192), thickness=3)
    cv2.rectangle(frame, (615, 470), (665, 520), (192, 192, 192), thickness=3)
    cv2.rectangle(frame, (750, 470), (800, 520), (192, 192, 192), thickness=3)

    cv2.imshow("Frame", frame)

    ret, frame = cap.read()
    key = cv2.waitKey(1)

    if key == 32:
        image_index += 1
        cv2.imwrite('./venv/data/blueData' + filename + ".bmp", frame)

        print("Current Image")

        # Top Layer
        # Top Left
        cv2.imshow("Top Left", frame[200:250, 480:530, :])
        print("Top Left: ", np.median(frame[200:250, 480:530, :], axis=(0, 1)))
        arr = np.median(frame[200:250, 480:530, :], axis=(0, 1))
        appendToList(arr)
        makePrediction(arr)

        # Top Center
        cv2.imshow("Top Middle", frame[200:250, 615:665, :])
        print("Top Center: ", np.median(frame[200:250, 615:665, :], axis=(0, 1)))
        arr = np.median(frame[200:250, 615:665, :], axis=(0, 1))
        appendToList(arr)

        # Top Center
        cv2.imshow("Top Right", frame[200:250, 750:800, :])
        print("Top Right: ", np.median(frame[200:250, 750:800, :], axis=(0, 1)))
        arr = np.median(frame[200:250, 750:800, :], axis=(0, 1))
        appendToList(arr)

        # Center Section

        # Center left
        cv2.imshow("Center Left", frame[335:385, 480:530, :])
        print("Center Left: ", np.median(frame[335:385, 615:665, :], axis=(0, 1)))
        arr = np.median(frame[335:385, 615:665, :], axis=(0, 1))
        appendToList(arr)

        # Center Piece
        cv2.imshow("Center Piece", frame[335:385, 615:665, :])
        print("Center Piece: ", np.median(frame[335:385, 615:665, :], axis=(0, 1)))
        arr = np.median(frame[335:385, 615:665, :], axis=(0, 1))
        appendToList(arr)

        # Center Right
        cv2.imshow("Center Right", frame[335:385, 750:800, :])
        print("Center Right: ", np.median(frame[335:385, 750:800, :], axis=(0, 1)))
        arr = np.median(frame[335:385, 750:800, :], axis=(0, 1))
        appendToList(arr)

        # Bottom left
        cv2.imshow("Bottom Left", frame[470:520, 480:530, :])
        print("Bottom Left: ", np.median(frame[470:520, 615:665, :], axis=(0, 1)))
        arr = np.median(frame[470:520, 615:665, :], axis=(0, 1))
        appendToList(arr)

        # Bottom Piece
        cv2.imshow("Bottom Piece", frame[470:520, 615:665, :])
        print("Bottom Center: ", np.median(frame[470:520, 615:665, :], axis=(0, 1)))
        arr = np.median(frame[470:520, 615:665, :], axis=(0, 1))
        appendToList(arr)

        # Bottom Right
        cv2.imshow("Bottom Right", frame[470:520, 750:800, :])
        print("Bottom Right: ", np.median(frame[470:520, 750:800, :], axis=(0, 1)))
        arr = np.median(frame[470:520, 750:800, :], axis=(0, 1))
        appendToList(arr)

        print("current median = ", np.mean(blueArr, axis=0))
        print("current std = ", np.std(blueArr, axis=0))
