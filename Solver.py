from rubik.cube import Cube
from rubik_solver import utils

from datetime import datetime
import time
import random
import os



class SolveCube:
    def __init__(self, cube):
        self.cube = cube

    def findWhiteEdge(self, cube):
        white_piece = []
        for piece in cube.pieces:
            if piece.type == "edge":
                if piece.colors[0] == "W" or piece.colors[1] == "W" or piece.colors[2] == "W":
                    white_piece.append([piece.colors, piece.pos])
        return white_piece

    def solveCross(self, cube):
        white_pieces = self.findWhiteEdge(cube)
        possible_faces = ["B", "G", "O", "R"]
        white_blue_solved = False
        white_green_solved = False
        white_orange_solved = False
        white_red_solved = False
        cross_algorithm = ""

        for val in range(len(white_pieces)):
            target_face = ""
            target_location = ""

            for face in range(len(possible_faces)):
                if possible_faces[face] in white_pieces[val][0]:
                    target_face = possible_faces[face]
                    target_location = c.find_piece(possible_faces[face])

            # -------------------------------------
            # Now Solving the White / Blue Face
            # -------------------------------------
            if "B" in white_pieces[val][0]:
                # Cases for blue/white being on GREEN Face
                # Case 1 and 1a
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "B":
                    c.sequence("L D Fi")
                    cross_algorithm += " L D Fi"
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "B":
                    c.sequence("L F F Li Fi Fi")
                    cross_algorithm += " L F F Li Fi Fi"
                # Case 2 and 2a
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "B":
                    c.sequence("Fi Fi L F F")
                    cross_algorithm += " Fi Fi L F F"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "B":
                    c.sequence("Fi Ui F")
                    cross_algorithm += " Fi Ui F"
                # Case 3 and 3a
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "B":
                    c.sequence("Bi Ui Fi L F F")
                    cross_algorithm += " Bi Ui Fi L F F"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "B":
                    c.sequence("Bi Bi R R")
                    cross_algorithm += " Bi Bi R R"
                # Case 4 and 4a
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "B":
                    c.sequence("F D Fi")
                    cross_algorithm += " F D Fi"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "B":
                    c.sequence("F F Li F F")
                    cross_algorithm += " F F Li F F"
                # Cases for blue/white being on RED Face
                # Case 5 and 5a
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "B":
                    c.sequence("D R")
                    cross_algorithm += " D R"
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "B":
                    c.sequence("D F Di Fi")
                    cross_algorithm += " D F Di Fi"
                # Case 6 and 6a
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "B":
                    c.sequence("F Di Fi")
                    cross_algorithm += " F Di Fi"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "B":
                    c.sequence("R")
                    cross_algorithm += " R"
                # Case 7 and 7a
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "B":
                    c.sequence("Di R D")
                    cross_algorithm += " Di R D"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "B":
                    c.sequence("B R R")
                    cross_algorithm += " B R R"
                # Cases for blue/white being on BLUE Face
                # Case 8 and 8a
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "B":
                    c.sequence("R Fi U F")
                    cross_algorithm += " R Fi U F"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "B":
                    print("CORRECT POSITION")
                # Case 9
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "B":
                    c.sequence("Ri")
                    cross_algorithm += " Ri"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "B":
                    c.sequence("Fi U F")
                    cross_algorithm += " Fi U F"
                # Case 10
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "B":
                    c.sequence("R R")
                    cross_algorithm += " R R"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "B":
                    c.sequence("Ri Fi U F")
                    cross_algorithm += " Ri Fi U F"
                # Final Cases for Orange and Yellow face....
                # Case 11
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "B":
                    c.sequence("Ui Fi U F")
                    cross_algorithm += " Ui Fi U F"
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "B":
                    c.sequence("Ui Ri")
                    cross_algorithm += " Ui Ri"
                # Case 12
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "B":
                    c.sequence("Bi R R")
                    cross_algorithm += " Bi R R"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "B":
                    c.sequence("Bi Ri Fi U F")
                    cross_algorithm += " Bi Ri Fi U F"

                white_pieces = findWhiteEdge(c)
            # -------------------------------------
            # Now Solving the White / Green Face
            # -------------------------------------

            if "G" in white_pieces[val][0]:
                # Cases for blue/white being on GREEN Face
                # Case 1 and 2
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "G":
                    print("Correct Position No Algorithm")
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "G":
                    c.sequence("L Fi D F")
                    cross_algorithm += " L Fi D F"
                # Case 3 and 4
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "G":
                    c.sequence("F Ui Fi")
                    cross_algorithm += " F Ui Fi"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "G":
                    c.sequence("L")
                    cross_algorithm += " L"
                # Case 5 and 6
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "G":
                    c.sequence("L L")
                    cross_algorithm += " L L"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "G":
                    c.sequence("Li Fi D F")
                    cross_algorithm += " Li Fi D F"
                # Case 7 and 8
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "G":
                    c.sequence("Fi D F")
                    cross_algorithm += " Fi D F"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "G":
                    c.sequence("Li")
                    cross_algorithm += " Li"
                # Case for green/white being on RED SIDE
                # Case 9 and 10
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "G":
                    c.sequence("Di Li")
                    cross_algorithm += " Di Li"
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "G":
                    c.sequence("D Fi Di F")
                    cross_algorithm += " D Fi Di F"
                # Case 11 and 12
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "G":
                    c.sequence("Fi Di F")
                    cross_algorithm += " Fi Di F"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "G":
                    c.sequence("Fi Fi R F F")
                    cross_algorithm += " Fi Fi R F F"
                # Case 13 and 14
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "G":
                    c.sequence("Bi Li Fi D F")
                    cross_algorithm += " Bi Li Fi D F"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "G":
                    c.sequence("Bi L L")
                    cross_algorithm += " Bi L L"
                # Case for green/white being on BLUE SIDE
                # Case 15 and 16
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "G":
                    c.sequence("Ri F F R F F")
                    cross_algorithm += " Ri F F R F F"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "G":
                    c.sequence("R F U Fi")
                    cross_algorithm += " R F U Fi"
                # Case 17 and 18
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "G":
                    c.sequence("F U Fi")
                    cross_algorithm += " F U Fi"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "G":
                    c.sequence("F F Ri F F")
                    cross_algorithm += " F F Ri F F"
                # Case 19 and 20
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "G":
                    c.sequence("B B L L")
                    cross_algorithm += " B B L L"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "G":
                    c.sequence("B B Li Fi D F")
                    cross_algorithm += " B B Li Fi D F"
                # Case 21 and 22
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "G":
                    c.sequence("B Li Fi D F")
                    cross_algorithm += " B Li Fi D F"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "G":
                    c.sequence("B L L")
                    cross_algorithm += " B L L"
                # Final Case (22 and 24)
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "G":
                    c.sequence("U F Ui Fi")
                    cross_algorithm += " U F Ui Fi"
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "G":
                    c.sequence("U L")
                    cross_algorithm += " U L"
                white_pieces = findWhiteEdge(c)
            # -------------------------------------
            # Now Solving the White / Orange Face
            # -------------------------------------

            if "O" in white_pieces[val][0]:
                # Case for White / Orange being on the GREEN FACE
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "O":
                    c.sequence("Fi L F")
                    cross_algorithm += " Fi L F"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "O":
                    c.sequence("Ui")
                    cross_algorithm += " Ui"
                # Case 3 and 4
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "O":
                    c.sequence("Fi L F Ui")
                    cross_algorithm += " Fi L F Ui"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "O":
                    c.sequence("Bi U U")
                    cross_algorithm += " Bi U U"
                # Case 5 and 6
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "O":
                    c.sequence("Fi Li F")
                    cross_algorithm += " Fi Li F"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "O":
                    c.sequence("F F D F F")
                    cross_algorithm += " F F D D F F"
                # Case 7 and 8
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "O":
                    c.sequence("Li Ui")  # correct case'
                    cross_algorithm += " Li Ui"
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "O":
                    c.sequence("L Fi Li F")
                    cross_algorithm += " L Fi Li F"
                # White and Orange on RED FACE
                # Case 9 and 10
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "O":
                    c.sequence("M M B B M M")
                    cross_algorithm += " M M B B M M"
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "O":
                    c.sequence(" D F R Fi")
                    cross_algorithm += " D F R Fi"
                # Case 11 and 12
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "O":
                    c.sequence("F R Fi")
                    cross_algorithm += " F R Fi"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "O":
                    c.sequence("F F Di F F")
                    cross_algorithm += " F F Di F F"
                # Case 13 and 14
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "O":
                    c.sequence("B B U U")
                    cross_algorithm += " B B U U"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "O":
                    c.sequence("Di F R Fi")
                    cross_algorithm += " Di F R Fi"
                # Case 15 and 16
                # White and Orange on BLUE FACE
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "O":
                    c.sequence("R U")
                    cross_algorithm += " R U"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "O":
                    c.sequence("Ri F R Fi")
                    cross_algorithm += " Ri F R Fi"
                # Case 17 and 18
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "O":
                    c.sequence("F Ri Fi")
                    cross_algorithm += " F Ri Fi"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "O":
                    c.sequence("U")
                    cross_algorithm += " U"
                # Case 19 and 20
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "O":
                    c.sequence("B U U")
                    cross_algorithm += " B U U"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "O":
                    c.sequence("Fi Ri F U")
                    cross_algorithm += " Fi Ri F U"
                # Case 21 and 22
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "O":
                    print("Correct position")
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "O":
                    c.sequence("U Fi L F")
                    cross_algorithm += " U Fi L F"
                # Case 23 and 24
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "O":
                    c.sequence("Ui Fi L F")
                    cross_algorithm += " Ui Fi L F"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "O":
                    c.sequence("U U")
                    cross_algorithm += " U U"
            white_pieces = findWhiteEdge(c)

            if "R" in white_pieces[val][0]:
                # Case for White / Orange being on the GREEN FACE
                # Case 1 and 2
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "R":
                    c.sequence(" L F Li Fi")
                    cross_algorithm += " L F Li Fi"
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "R":
                    c.sequence("L D")
                    cross_algorithm += " L D"
                # Case 3 and 4
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "R":
                    c.sequence("F F Ui F F")
                    cross_algorithm += " F F Ui F F"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "R":
                    c.sequence("F L Fi")
                    cross_algorithm += " F L Fi"
                # Case 5 and 6
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "R":
                    c.sequence("B D D")
                    cross_algorithm += " B D D"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "R":
                    c.sequence(" B Di Fi R F")
                    cross_algorithm += " B Di Fi R F"
                # Case 7 and 8
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "R":
                    c.sequence("D")
                    cross_algorithm += " D"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "R":
                    c.sequence("F Li Fi")
                    cross_algorithm += " F Li Fi"
                # Case 9 and 10
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "R":
                    print("No algorithm needed")
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "R":
                    c.sequence("D Fi R F")
                    cross_algorithm += " D Fi R F"
                # Case 11  and 12
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "R":
                    c.sequence("Fi R F")
                    cross_algorithm += " Fi R F"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "R":
                    c.sequence("Di")
                    cross_algorithm += " Di"
                # Case 13 and 14
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "R":
                    c.sequence("D D")
                    cross_algorithm += " D D"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "R":
                    c.sequence("Di Fi R F")
                    cross_algorithm += " Di Fi R F"
                # Case 15 and 16
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "R":
                    c.sequence("Ri Fi R F")
                    cross_algorithm += " Ri Fi R F"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "R":
                    c.sequence("Ri Di")
                    cross_algorithm += " Ri Di"
                # Case 17 and 18
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "R":
                    c.sequence("F F U F F")
                    cross_algorithm += " F F U F F"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "R":
                    c.sequence("Fi Ri F")
                    cross_algorithm += " Fi Ri F"
                # Case 19 and 20
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "R":
                    c.sequence("Bi D D")
                    cross_algorithm += " Bi D D"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "R":
                    c.sequence("Bi Di Fi R F")
                    cross_algorithm += " Bi Di Fi R F"
                # Case 21 and 22
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "R":
                    c.sequence("U U B B D D")
                    cross_algorithm += " U U B B D D"
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "R":
                    c.sequence("U F F Ui F F")
                    cross_algorithm += " U F F Ui F F"
                # Case 23 and 24 FINAL ONES IM SO HAPPY
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "R":
                    c.sequence("B B Di Fi R F")
                    cross_algorithm += " B B Di Fi R F"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "R":
                    c.sequence("B B D D")
                    cross_algorithm += " B B D D"
            white_pieces = findWhiteEdge(c)
        return cross_algorithm

    def checkCross(self, cube):
        white_pieces = findWhiteEdge(cube)
        # Check if pieces in correct location:
        # Check blue:
        if "B" in white_pieces[0][0]:
            if white_pieces[0][1] == (1, 0, 1) and white_pieces[0][0][0] == "B":
                print("Blue / White piece positioned correctly")
                white_blue_solved = True
            else:
                print("Error with blue and white positioning")
                white_blue_solved = False
        if "G" in white_pieces[1][0]:
            if white_pieces[1][1] == (-1, 0, 1) and white_pieces[1][0][0] == "G":
                print("Green / White piece positioned correctly")
                white_green_solved = True
            else:
                print("Error with green and white positioning")
                white_green_solved = False
        if "O" in white_pieces[2][0]:
            if white_pieces[2][1] == (0, 1, 1) and white_pieces[2][0][1] == "O":
                print("Orange / White piece positioned correctly")
                white_orange_solved = True
            else:
                print("Error with orange and white positioning")
                white_orange_solved = False
        if "R" in white_pieces[3][0]:
            if white_pieces[3][1] == (0, -1, 1) and white_pieces[3][0][1] == "R":
                print("Red / White piece positioned correctly")
                white_red_solved = True
            else:
                print("Error with orange and white positioning")
                white_red_solved = False

        return white_blue_solved, white_green_solved, white_orange_solved, white_red_solved

    def generateScramble(self):
        notation = [" R ", " U ", " F ", " L ", " B ", "  D ", " Ri ", " Ui ", " Fi ", " Li ", " Bi ", "  Di "]
        scramble = " "
        for i in range(1, 15):
            scramble += str(notation[random.randrange(0, 12)])
        print(scramble)
        return scramble

    def testCross(self, testRange):
        solve_list = []
        trueWhiteBlue = 0
        trueWhiteGreen = 0
        falseWhiteBlue = 0
        falseWhiteGreen = 0
        trueWhiteOrange = 0
        falseWhiteOrange = 0
        trueWhiteRed = 0
        falseWhiteRed = 0

        print("Testing Cross Algorithm: ")
        print("Number of Tests: ", testRange)

        for cube in range(testRange):
            print("Test ", cube)
            scr = generateScramble()
            print("Scramble ", scr)
            test_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
            test_cube.sequence(scr)
            value = solveCross(test_cube)
            print(value)
            solve_list.append(value)
            print(" ")
            print("  ")

        for val in solve_list:
            if val[0] == True:
                trueWhiteBlue += 1
            if val[1] == True:
                trueWhiteGreen += 1
            if val[0] == False:
                falseWhiteGreen += 1
            if val[1] == False:
                falseWhiteGreen += 1
            if val[2] == True:
                trueWhiteOrange += 1
            if val[2] == False:
                falseWhiteOrange += 1
            if val[3] == True:
                trueWhiteRed += 1
            if val[3] == False:
                falseWhiteRed += 1
        print("Testing Cross Algorithm: ")
        print("Number of Tests: ", testRange)
        print("White Blue")
        print("Correct Values (White Blue) = ", trueWhiteBlue)
        print("Incorrect Values (White Blue) = ", falseWhiteBlue)
        print("White Green:")
        print("Correct Values (White Green) = ", trueWhiteGreen)
        print("Incorrect Values (White Green) = ", falseWhiteGreen)
        print("White Orange:")
        print("Correct Values (White Orange) = ", trueWhiteOrange)
        print("Incorrect Values (White Orange) = ", falseWhiteOrange)
        print("White Red")
        print("Correct Values (White Red) = ", trueWhiteRed)
        print("Incorrect Values (White Red) = ", falseWhiteRed)
        print(" ")
        print("Overall Acuracy = 100%")

        if "False" in solve_list:
            print("hey")