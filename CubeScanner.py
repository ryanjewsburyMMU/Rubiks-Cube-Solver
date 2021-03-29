import cv2
import time
import numpy as np
import webcolors
import time


class CubeScanner():
    # Variable Dec
    # Dataset of Colours
    def scan(self):
        white_mean = [207.06666667, 221.26666667, 231.02222222]
        red_mean = [40.9, 33.73333333, 233.73333333]
        yellow_mean = [79.06666667, 234.05555556, 216.5]
        orange_mean = [50.98888889, 93.65555556, 253.1]
        green_mean = [75, 194, 27]
        blue_mean = [123.22222222, 107.22222222, 92.55555556]

        # Variable Dec
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Cube Faces
        face_list = ["White", "Green", "Yellow", "Blue", "Red", "Orange"]
        face_index = 0

        white_face = []
        green_face = []
        yellow_face = []
        blue_face = []
        red_face = []
        orange_face = []

        rubiks_cube = [white_face, green_face, yellow_face, blue_face, red_face, orange_face]

        # Digital Cube Colours
        top_left_color = (255, 255, 255)
        top_middle_color = (255, 255, 255)
        top_right_color = (255, 255, 255)

        middle_left_color = (255, 255, 255)
        middle_middle_color = (255, 255, 255)
        middle_right_color = (255, 255, 255)

        bottom_left_color = (255, 255, 255)
        bottom_middle_color = (255, 255, 255)
        bottom_right_color = (255, 255, 255)

        window_name = cv2.namedWindow("Test")

        text = "Please Scan The " + face_list[face_index] + " Face"

        cap = cv2.VideoCapture(0)

        def drawCube():
            cv2.rectangle(frame, (10, 10), (50, 50), top_left_color, -1)
            cv2.rectangle(frame, (60, 10), (100, 50), top_middle_color, -1)
            cv2.rectangle(frame, (110, 10), (150, 50), top_right_color, -1)

            cv2.rectangle(frame, (10, 60), (50, 100), middle_left_color, -1)
            cv2.rectangle(frame, (60, 60), (100, 100), middle_middle_color, -1)
            cv2.rectangle(frame, (110, 60), (150, 100), middle_right_color, -1)

            cv2.rectangle(frame, (10, 110), (50, 150), bottom_left_color, -1)
            cv2.rectangle(frame, (60, 110), (100, 150), bottom_middle_color, -1)
            cv2.rectangle(frame, (110, 110), (150, 150), bottom_right_color, -1)

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

            if (smallestValue == 0):
                return "White"
            elif (smallestValue == 1):
                return "Red"
            elif (smallestValue == 2):
                return "Yellow"
            elif (smallestValue == 3):
                return "Orange"
            elif (smallestValue == 4):
                return "Green"
            elif (smallestValue == 5):
                return "Blue"


        while True:
            ret, frame = cap.read()
            text_size = cv2.getTextSize(text, font, 1, 2)[0]
            textX = (frame.shape[1] - text_size[0]) // 2
            textY = (frame.shape[0] + text_size[1]) // 6

            cv2.putText(frame, text, (textX, textY), font, 1, (0, 0, 0), 2)
            cv2.rectangle(frame, (480, 200), (530, 250), (192, 192, 192), thickness=3)
            cv2.rectangle(frame, (615, 200), (665, 250), (192, 192, 192), thickness=3)
            cv2.rectangle(frame, (750, 200), (800, 250), (192, 192, 192), thickness=3)

            cv2.rectangle(frame, (480, 335), (530, 385), (192, 192, 192), thickness=3)
            cv2.rectangle(frame, (615, 335), (665, 385), (192, 192, 192), thickness=3)
            cv2.rectangle(frame, (750, 335), (800, 385), (192, 192, 192), thickness=3)

            cv2.rectangle(frame, (480, 470), (530, 520), (192, 192, 192), thickness=3)
            cv2.rectangle(frame, (615, 470), (665, 520), (192, 192, 192), thickness=3)
            cv2.rectangle(frame, (750, 470), (800, 520), (192, 192, 192), thickness=3)

            drawCube()
            cv2.imshow("Frame", frame)

            ret, frame = cap.read()
            key = cv2.waitKey(1)

            if key == 32:
                text = "Press ENTER to Confirm"

                top_left = np.median(frame[200:250, 480:530, :], axis=(0, 1))

                top_middle = np.median(frame[200:250, 615:665, :], axis=(0, 1))

                top_right = np.median(frame[200:250, 750:800, :], axis=(0, 1))

                middle_left = np.median(frame[335:385, 480:530, :], axis=(0, 1))

                middle_center = np.median(frame[335:385, 615:665, :], axis=(0, 1))

                middle_right = np.median(frame[335:385, 750:800, :], axis=(0, 1))

                bottom_left = np.median(frame[470:520, 480:530, :], axis=(0, 1))

                bottom_center = np.median(frame[470:520, 615:665, :], axis=(0, 1))

                bottom_right = np.median(frame[470:520, 750:800, :], axis=(0, 1))

                top_layer = np.array((makePrediction(top_left), makePrediction(top_middle), makePrediction(top_right)))
                middle_layer = np.array(
                    (makePrediction(middle_left), makePrediction(middle_center), makePrediction(middle_right)))
                bottom_layer = np.array(
                    (makePrediction(bottom_left), makePrediction(bottom_center), makePrediction(bottom_right)))

                full_cube = np.vstack((top_layer, middle_layer, bottom_layer,))
                cv2.rectangle(frame, (10, 10), (100, 100), (192, 192, 192), thickness=3)

                middle_right_color = (255, 0, 255)

                target = webcolors.name_to_rgb(full_cube[0, 0])
                top_left_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[0, 1])
                top_middle_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[0, 2])
                top_right_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[1, 0])
                middle_left_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[1, 1])
                middle_middle_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[1, 2])
                middle_right_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[2, 0])
                bottom_left_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[2, 1])
                bottom_middle_color = (target[2], target[1], target[0])

                target = webcolors.name_to_rgb(full_cube[2, 2])
                bottom_right_color = (target[2], target[1], target[0])

            if key == 13:
                if face_index == 5:
                    text = "You have scanned your cube - exiting in 5 seconds"
                    rubiks_cube[face_index] = full_cube
                    return rubiks_cube

                elif full_cube[1, 1] == face_list[face_index]:
                    rubiks_cube[face_index] = full_cube
                    face_index += 1
                    text = "Please Scan The " + face_list[face_index] + " Face"
                else:
                    text = "Please Scan the " + face_list[face_index] + " Face"

    # def createCubeString(self, cube):
    #     return cube


# c = CubeScanner()
# fullcube = c.scan()
# cubeString = c.createCubeString(fullcube)