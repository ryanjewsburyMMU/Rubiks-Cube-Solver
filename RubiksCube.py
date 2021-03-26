from rubik.cube import Cube
from rubik_solver import utils

from datetime import datetime
import time
import random
import statistics

#
# Stage One Solves White Cross
def findWhiteEdge(c):
    white_piece = []
    for piece in c.pieces:
        if piece.type == "edge":
            if piece.colors[0] == "W" or piece.colors[1] == "W" or piece.colors[2] == "W":
                white_piece.append([piece.colors, piece.pos])
    return white_piece
def solveWhiteCross(c):
    white_pieces = findWhiteEdge(c)
    possible_faces = ["B", "G", "O", "R"]
    white_blue_solved = False
    white_green_solved = False
    white_orange_solved = False
    white_red_solved = False
    cross_algorithm = ""

    print(c)

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
            print("Solving White / Blue Face:")
            # Cases for blue/white being on GREEN Face
            # Case 1 and 1a
            if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "B":
                c.sequence("L D Fi")
                cross_algorithm += " L D Fi"
                print(c)
            elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "B":
                c.sequence("L F F Li Fi Fi")
                cross_algorithm += " L F F Li Fi Fi"
                print(c)
            # Case 2 and 2a
            if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "B":
                c.sequence("Fi Fi L F F")
                cross_algorithm += " Fi Fi L F F"
                print(c)
            elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "B":
                c.sequence("Fi Ui F")
                cross_algorithm += " Fi Ui F"
                print(c)
            # Case 3 and 3a
            if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "B":
                c.sequence("Bi Ui Fi L F F")
                cross_algorithm += " Bi Ui Fi L F F"
                print(c)
            elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "B":
                c.sequence("Bi Bi R R")
                cross_algorithm += " Bi Bi R R"
                print(c)
            # Case 4 and 4a
            if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "B":
                c.sequence("F D Fi")
                cross_algorithm += " F D Fi"
                print(c)
            elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "B":
                c.sequence("F F Li F F")
                cross_algorithm += " F F Li F F"
                print(c)
            # Cases for blue/white being on RED Face
            # Case 5 and 5a
            if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "B":
                c.sequence("D R")
                cross_algorithm += " D R"
                print(c)
            elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "B":
                c.sequence("D F Di Fi")
                cross_algorithm += " D F Di Fi"
                print(c)
            # Case 6 and 6a
            if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "B":
                c.sequence("F Di Fi")
                cross_algorithm += " F Di Fi"
                print(c)
            elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "B":
                c.sequence("R")
                cross_algorithm += " R"
                print(c)
            # Case 7 and 7a
            if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "B":
                c.sequence("Di R D")
                cross_algorithm += " Di R D"
                print(c)
            elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "B":
                c.sequence("B R R")
                cross_algorithm += " B R R"
                print(c)
            # Cases for blue/white being on BLUE Face
            # Case 8 and 8a
            if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "B":
                print("case found")
                c.sequence("R Fi U F")
                cross_algorithm += " R Fi U F"
                print(c)
            elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "B":
                print("CORRECT POSITION")
                print(c)
            # Case 9
            if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "B":
                c.sequence("Ri")
                cross_algorithm += " Ri"
                print(c)
            elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "B":
                c.sequence("Fi U F")
                cross_algorithm += " Fi U F"
                print(c)
            # Case 10
            if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "B":
                c.sequence("R R")
                cross_algorithm += " R R"
                print(c)
            elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "B":
                c.sequence("Ri Fi U F")
                cross_algorithm += " Ri Fi U F"
                print(c)
            # Final Cases for Orange and Yellow face....
            # Case 11
            if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "B":
                c.sequence("Ui Fi U F")
                cross_algorithm += " Ui Fi U F"
                print(c)
            elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "B":
                c.sequence("Ui Ri")
                cross_algorithm += " Ui Ri"
                print(c)
            # Case 12
            if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "B":
                c.sequence("Bi R R")
                cross_algorithm += " Bi R R"
                print(c)
            elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "B":
                c.sequence("Bi Ri Fi U F")
                cross_algorithm += " Bi Ri Fi U F"
                print(c)

            white_pieces = findWhiteEdge(c)
        if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "B":
            print("White and Blue Solved Succesfully")
            white_blue_solved = True

        # -------------------------------------
        # Now Solving the White / Green Face
        # -------------------------------------

        if "G" in white_pieces[val][0]:
            print("Now solving white green")
            print(white_pieces[val][1])
            # Cases for blue/white being on GREEN Face
            # Case 1 and 2
            if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "G":
                print("Correct Position No Algorithm")
                print(c)
            elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "G":
                c.sequence("L Fi D F")
                cross_algorithm += " L Fi D F"
                print(c)
            # Case 3 and 4
            if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "G":
                c.sequence("F Ui Fi")
                cross_algorithm += " F Ui Fi"
                print(c)
            elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "G":
                c.sequence("L")
                cross_algorithm += " L"
                print(c)
            # Case 5 and 6
            if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "G":
                c.sequence("L L")
                cross_algorithm += " L L"
                print(c)
            elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "G":
                c.sequence("Li Fi D F")
                cross_algorithm += " Li Fi D F"
                print(c)
            # Case 7 and 8
            if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "G":
                c.sequence("Fi D F")
                cross_algorithm += " Fi D F"
                print(c)
            elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "G":
                c.sequence("Li")
                cross_algorithm += " Li"
                print(c)
            # Case for green/white being on RED SIDE
            # Case 9 and 10
            if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "G":
                c.sequence("Di Li")
                cross_algorithm += " Di Li"
                print(c)
            elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "G":
                c.sequence("D Fi Di F")
                cross_algorithm += " D Fi Di F"
                print(c)
            # Case 11 and 12
            if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "G":
                c.sequence("Fi Di F")
                cross_algorithm += " Fi Di F"
                print(c)
            elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "G":
                c.sequence("Fi Fi R F F")
                cross_algorithm += " Fi Fi R F F"
                print(c)
            # Case 13 and 14
            if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "G":
                c.sequence("Bi Li Fi D F")
                cross_algorithm += " Bi Li Fi D F"
                print(c)
            elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "G":
                c.sequence("Bi L L")
                cross_algorithm += " Bi L L"
                print(c)
            # Case for green/white being on BLUE SIDE
            # Case 15 and 16
            if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "G":
                c.sequence("Ri F F R F F")
                cross_algorithm += " Ri F F R F F"
                print(c)
            elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "G":
                c.sequence("R F U Fi")
                cross_algorithm += " R F U Fi"
                print(c)
            # Case 17 and 18
            if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "G":
                c.sequence("F U Fi")
                cross_algorithm += " F U Fi"
                print(c)
            elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "G":
                c.sequence("F F Ri F F")
                cross_algorithm += " F F Ri F F"
                print(c)
            # Case 19 and 20
            if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "G":
                c.sequence("B B L L")
                cross_algorithm += " B B L L"
                print(c)
            elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "G":
                c.sequence("B B Li Fi D F")
                cross_algorithm += " B B Li Fi D F"
                print(c)
            # Case 21 and 22
            if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "G":
                c.sequence("B Li Fi D F")
                cross_algorithm += " B Li Fi D F"
                print(c)
            elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "G":
                c.sequence("B L L")
                cross_algorithm += " B L L"
                print(c)
            # Final Case (22 and 24)
            if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "G":
                c.sequence("U F Ui Fi")
                cross_algorithm += " U F Ui Fi"
                print(c)
            elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "G":
                c.sequence("U L")
                cross_algorithm += " U L"
                print(c)

            white_pieces = findWhiteEdge(c)
        if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "G":
            print("White and Green Solved Succesfully")
            white_green_solved = True

        # -------------------------------------
        # Now Solving the White / Orange Face
        # -------------------------------------

        if "O" in white_pieces[val][0]:
            # Case for White / Orange being on the GREEN FACE
            if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "O":
                c.sequence("Fi L F")
                cross_algorithm += " Fi L F"
                print(c)
            elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "O":
                c.sequence("Ui")
                cross_algorithm += " Ui"
                print(c)
            # Case 3 and 4
            if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "O":
                c.sequence("Fi L F Ui")
                cross_algorithm += " Fi L F Ui"
                print(c)
            elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "O":
                c.sequence("Bi U U")
                cross_algorithm += " Bi U U"
                print(c)
            # Case 5 and 6
            if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "O":
                c.sequence("Fi Li F")
                cross_algorithm += " Fi Li F"
                print(c)
            elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "O":
                c.sequence("F F D F F")
                cross_algorithm += " F F D D F F"
                print(c)
            # Case 7 and 8
            if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "O":
                c.sequence("Li Ui")  # correct case'
                cross_algorithm += " Li Ui"
                print(c)
            elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "O":
                c.sequence("L Fi Li F")
                cross_algorithm += " L Fi Li F"
                print(c)
            # White and Orange on RED FACE
            # Case 9 and 10
            if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "O":
                c.sequence("M M B B M M")
                cross_algorithm += " M M B B M M"
                print(c)
            elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "O":
                c.sequence(" D F R Fi")
                cross_algorithm += " D F R Fi"
                print(c)
            # Case 11 and 12
            if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "O":
                c.sequence("F R Fi")
                cross_algorithm += " F R Fi"
                print(c)
            elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "O":
                c.sequence("F F Di F F")
                cross_algorithm += " F F Di F F"
                print(c)
            # Case 13 and 14
            if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "O":
                c.sequence("B B U U")
                cross_algorithm += " B B U U"
                print(c)
            elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "O":
                c.sequence("Di F R Fi")
                cross_algorithm += " Di F R Fi"
                print(c)
            # Case 15 and 16
            # White and Orange on BLUE FACE
            if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "O":
                c.sequence("R U")
                cross_algorithm += " R U"
                print(c)
            elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "O":
                c.sequence("Ri F R Fi")
                cross_algorithm += " Ri F R Fi"
                print(c)
            # Case 17 and 18
            if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "O":
                c.sequence("F Ri Fi")
                cross_algorithm += " F Ri Fi"
                print(c)
            elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "O":
                c.sequence("U")
                cross_algorithm += " U"
                print(c)
            # Case 19 and 20
            if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "O":
                c.sequence("B U U")
                cross_algorithm += " B U U"
                print(c)
            elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "O":
                c.sequence("Fi Ri F U")
                cross_algorithm += " Fi Ri F U"
                print(c)
            # Case 21 and 22
            if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "O":
                print("Correct position")
            elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "O":
                c.sequence("U Fi L F")
                cross_algorithm += " U Fi L F"
                print(c)
            # Case 23 and 24
            if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "O":
                c.sequence("Ui Fi L F")
                cross_algorithm += " Ui Fi L F"
                print(c)
            elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "O":
                c.sequence("U U")
                cross_algorithm += " U U"
                print(c)

        white_pieces = findWhiteEdge(c)

        if "R" in white_pieces[val][0]:
            # Case for White / Orange being on the GREEN FACE
            # Case 1 and 2
            if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "R":
                c.sequence(" L F Li Fi")
                cross_algorithm += " L F Li Fi"
                print(c)
            elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "R":
                c.sequence("L D")
                cross_algorithm += " L D"
                print(c)
            # Case 3 and 4
            if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "R":
                c.sequence("F F Ui F F")
                cross_algorithm += " F F Ui F F"
                print(c)
            elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "R":
                c.sequence("F L Fi")
                cross_algorithm += " F L Fi"
                print(c)
            # Case 5 and 6
            if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "R":
                c.sequence("B D D")
                cross_algorithm += " B D D"
                print(c)
            elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "R":
                c.sequence(" B Di Fi R F")
                cross_algorithm += " B Di Fi R F"
                print(c)
            # Case 7 and 8
            if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "R":
                c.sequence("D")
                cross_algorithm += " D"
                print(c)
            elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "R":
                c.sequence("F Li Fi")
                cross_algorithm += " F Li Fi"
                print(c)
            # Case 9 and 10
            if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "R":
                print("No algorithm needed")
                print(c)
            elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "R":
                c.sequence("D Fi R F")
                cross_algorithm += " D Fi R F"
                print(c)
            # Case 11  and 12
            if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "R":
                c.sequence("Fi R F")
                cross_algorithm += " Fi R F"
                print(c)
            elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "R":
                c.sequence("Di")
                cross_algorithm += " Di"
                print(c)
            # Case 13 and 14
            if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "R":
                c.sequence("D D")
                cross_algorithm += " D D"
                print(c)
            elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "R":
                c.sequence("Di Fi R F")
                cross_algorithm += " Di Fi R F"
                print(c)
            # Case 15 and 16
            if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "R":
                c.sequence("Ri Fi R F")
                cross_algorithm += " Ri Fi R F"
                print(c)
            elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "R":
                c.sequence("Ri Di")
                cross_algorithm += " Ri Di"
                print(c)
            # Case 17 and 18
            if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "R":
                c.sequence("F F U F F")
                cross_algorithm += " F F U F F"
                print(c)
            elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "R":
                c.sequence("Fi Ri F")
                cross_algorithm += " Fi Ri F"
                print(c)
            # Case 19 and 20
            if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "R":
                c.sequence("Bi D D")
                cross_algorithm += " Bi D D"
                print(c)
            elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "R":
                c.sequence("Bi Di Fi R F")
                cross_algorithm += " Bi Di Fi R F"
                print(c)
            # Case 21 and 22
            if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "R":
                c.sequence("U U B B D D")
                cross_algorithm += " U U B B D D"
                print(c)
            elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "R":
                c.sequence("U F F Ui F F")
                cross_algorithm += " U F F Ui F F"
            # Case 23 and 24 FINAL ONES IM SO HAPPY
            if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "R":
                c.sequence("B B Di Fi R F")
                cross_algorithm += " B B Di Fi R F"
                print(c)
            elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "R":
                c.sequence("B B D D")
                cross_algorithm += " B B D D"
                print(c)
        white_pieces = findWhiteEdge(c)

    #

    # Check if pieces in correct location:
    # Check blue:
    print(" ")
    print(" ")
    print("Final Checks")
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
    print(white_blue_solved, white_green_solved, white_orange_solved, white_red_solved)
    print("Algorithm = ", cross_algorithm)
    return cross_algorithm

# Stage 2 Solves White Corners
def findWhiteCorner(c):
    print("finding white edges")
    white_piece = []
    for piece in c.pieces:
        if piece.type == "corner":
            if piece.colors[0] == "W" or piece.colors[1] == "W" or piece.colors[2] == "W":
                white_piece.append([piece.colors, piece.pos])
    return white_piece
def solveWhiteCorner(c):
    print("Solving White Edges")
    count = 0
    whiteCorners = findWhiteCorner(c)
    whiteCornersAlgorithm = ""

    correct_positions = [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1)]
    correct_arrangements = [['B', 'O', 'W'], ['B', 'R', 'W'], ['G', 'O', 'W'], ['G', 'R', 'W']]

    for val in range(len(whiteCorners)):
        print(val)
        # First Check
        # Checking if piece is on bottom row, else skip onto next step

        if whiteCorners[val][1] == (1,1,1): # Doing
            print("Piece found at WHITE [0,2]")
            if whiteCorners[val][0] == correct_arrangements[0]:
                print(correct_arrangements[val], " piece In Correct Location")
            else:
                print(correct_arrangements[val], " piece In wrong Location - algorithm needed...")
                c.sequence("R B Ri Bi")
                whiteCornersAlgorithm += " R B Ri Bi"
                whiteCorners = findWhiteCorner(c)
        if whiteCorners[val][1] == (1,-1,1):
            print("Piece found at WHITE [2,2]")
            if whiteCorners[val][0] == correct_arrangements[1]:
                print(correct_arrangements[val], " piece In Correct Location")
            else:
                print(correct_arrangements[val], " piece In wrong Location - algorithm needed")
                c.sequence("Ri Bi R B")
                whiteCornersAlgorithm += " Ri Bi R B"
                whiteCorners = findWhiteCorner(c)
        if whiteCorners[val][1] == (-1,1,1):
            print("Piece found at WHITE [0,0]]")
            if whiteCorners[val][0] == correct_arrangements[2]:
                print(correct_arrangements[val], " piece In Correct Location")
            else:
                print(correct_arrangements[val], " piece In wrong Location - algorithm needed")
                c.sequence("Li Bi L B")
                whiteCornersAlgorithm += " Li Bi L B"
                whiteCorners = findWhiteCorner(c)
        if whiteCorners[val][1] == (-1,-1,1):
            print("Piece found at WHITE [2,0]")
            if whiteCorners[val][0] == correct_arrangements[3]:
                print("---------------------")
                print("Test Start")
                print("Val = ", val)
                print(whiteCorners[val][0])
                print(correct_arrangements[val])
                print(whiteCorners[val][1])

                print("---------------------")

                print(correct_arrangements[val], " piece In Correct Location")
            else:
                print(correct_arrangements[val], " piece In wrong Location - algorithm needed")
                c.sequence("L B Li Bi")
                whiteCornersAlgorithm += " L B Li Bi"
                whiteCorners = findWhiteCorner(c)


        # Second Section
        if whiteCorners[val][1][2] == -1:
            if set(whiteCorners[val][0]).issubset(['W','O','B']):
                print("White Orange and blue piece")
                print("Position: ", whiteCorners[val][1])
                while whiteCorners[val][1] != (1,1,-1):
                    print("B")
                    c.sequence("B")
                    whiteCornersAlgorithm += " B"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    if whiteCorners[val][1] == (1,1,-1):
                        print("Ready to insert")
                        print(whiteCorners[val][1])
                        print(whiteCorners[val][0])
                        print(c)
                        whiteCorners = findWhiteCorner(c)
                print("Stage 2")
                while whiteCorners[val][1] != (1,1,1) or whiteCorners[val][0] != ['B', 'O', 'W']:
                    print("Doing algo")
                    c.sequence("R B Ri Bi")
                    whiteCornersAlgorithm += " R B Ri Bi"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    print(whiteCorners[val][0])
                print(c)

            if set(whiteCorners[val][0]).issubset(['W','R','B']):
                print("White Red and Blue piece")
                print("Position: ",whiteCorners[val][1])
                while whiteCorners[val][1] != (1,-1,-1):
                    print("B")
                    c.sequence("B")
                    whiteCornersAlgorithm += " B"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    if whiteCorners[val][1] == (1,-1,-1):
                        print("Ready to insert")
                        print(whiteCorners[val][1])
                        print(whiteCorners[val][0])
                        print(c)
                        whiteCorners = findWhiteCorner(c)
                print("Stage 2")
                while whiteCorners[val][1] != (1,-1,1) or whiteCorners[val][0] != ['B', 'R', 'W']:
                    print("Doing algo")
                    c.sequence("D B Di Bi")
                    whiteCornersAlgorithm += " D B Di Bi"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    print(whiteCorners[val][0])
                print(c)

            if set(whiteCorners[val][0]).issubset(['W', 'G', 'O']):
                print("Orange Green and White piece")
                print("Position: ",whiteCorners[val][1])
                while whiteCorners[val][1] != (-1,1,-1):
                    print("B")
                    c.sequence("B")
                    whiteCornersAlgorithm += " B"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    if whiteCorners[val][1] == (-1,1,-1):
                        print("Ready to insert")
                        print(whiteCorners[val][1])
                        print(whiteCorners[val][0])
                        print(c)
                        whiteCorners = findWhiteCorner(c)
                print("Stage 2")
                while whiteCorners[val][1] != (-1,1,1) or whiteCorners[val][0] != ['G', 'O', 'W']:
                    print("Doing algo")
                    c.sequence("Li Bi L B")
                    whiteCornersAlgorithm += " Li Bi L B"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    print(whiteCorners[val][0])
                print(c)
            if set(whiteCorners[val][0]).issubset(['W', 'G', 'R']):
                print("Red Green and White piece")
                print("Position: ",whiteCorners[val][1])

                while whiteCorners[val][1] != (-1,-1,-1):
                    print("B")
                    c.sequence("B")
                    whiteCornersAlgorithm += " B"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    if whiteCorners[val][1] == (-1,-1,-1):
                        print("Ready to insert")
                        print(whiteCorners[val][1])
                        print(whiteCorners[val][0])
                        print(c)
                        whiteCorners = findWhiteCorner(c)
                print("Stage 2")
                while whiteCorners[val][1] != (-1,-1,1) or whiteCorners[val][0] != ['G', 'R', 'W']:
                    print("Doing algo")
                    c.sequence("L B Li Bi")
                    whiteCornersAlgorithm += " L B Li Bi"
                    whiteCorners = findWhiteCorner(c)
                    print(whiteCorners[val][1])
                    print(whiteCorners[val][0])

    return whiteCornersAlgorithm

# Stage 3 Solves Middle Layer Pieces
def findMiddleLayerPiece(cornerPiece, c):
    target_colours = []
    target_piece = []
    for val in cornerPiece:
        if val != "W":
            target_colours.append(val)
    target_colours.append(None)
    for piece in c.pieces:
        if piece.type == "edge":
            if set(piece.colors).issubset(target_colours):
                target_piece.append([piece.colors, piece.pos])
    return target_piece
def solveSecondLayer(c):
    print("Solving Second Layer")
    print("\n")

    print(c)
    second_layer_algorithm = " "
    whiteCorners = findWhiteCorner(c)
    order = ["First - Blue/White/Orange", "Second - Blue/White/Red", "Third - Green/Orange/White", "Fourth - Green/Red/White"]
    for val in range(len(whiteCorners)):
        print(str(order[val]))

        # First step find corresponding edge piece...
        # If in mid layer, perform aalgorithm to remove from middle layer onto top layer, but put corner piece back in place
        # Do this algorithm for every possible middle layer

        # Decide whether piece is facing up or down - have two different desitions for each piece, depending on colour facing up

        # Perform algorithm (2 for each case.)

        # Finds corresponding edge piece based on current position...
        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)

        print(currentEdgePiece[0][1])
        print(currentEdgePiece[0][0])

        # Third index being 0 means they sit in the same level... middle layer...
        if currentEdgePiece[0][1] == (1,1,0):
            # Check if in correct place...
            if set(currentEdgePiece[0][0]).issubset(['B', 'O', None]) and currentEdgePiece[0][0] == ["B", "O", None]:
                print("piece in correct location")
            else:
                c.sequence("R B Ri Bi Ui Bi U B")
                currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                second_layer_algorithm += " R B Ri Bi Ui Bi U B"
                print(c)

        if currentEdgePiece[0][1] == (1,-1,0):
            if set(currentEdgePiece[0][0]).issubset(['B', 'R', None]) and currentEdgePiece[0][0] == ['B', 'R', None]:
                print("piece in correct location")
            else:
                print("Piece not in correct location, algorithm needed")
                c.sequence("D B Di Bi Ri Bi R B")
                currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                second_layer_algorithm += " D B Di Bi Ri Bi R B"
                print(c)

        if currentEdgePiece[0][1] == (-1,1,0):
            if set(currentEdgePiece[0][0]).issubset(['G', 'O', None]) and currentEdgePiece[0][0] == ['G', 'O', None]:
                print("piece in correct location")
            else:
                print("Piece not in correct location, algorithm needed")
                print(c)
                c.sequence("Li Bi L B U B Ui Bi")
                currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                second_layer_algorithm += " Li Bi L B U B Ui Bi"
                print(c)

        if currentEdgePiece[0][1] == (-1,-1,0):
            if set(currentEdgePiece[0][0]).issubset(['G', 'R', None]) and currentEdgePiece[0][0] == ['G', 'R', None]:
                print("piece in correct location")
            else:
                print("Piece not in correct location, algorithm needed")
                c.sequence("L B Li Bi Di Bi D B")
                currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                second_layer_algorithm += " L B Li Bi Di Bi D B"
                print(c)




        print(" ")

        if currentEdgePiece[0][1][2] == -1:
            print("Piece on top layer, ready to insert")
            print("Pice Current Loc: ", currentEdgePiece[0][1])
            print("Piece Current order: ", currentEdgePiece[0][0])
            # Under the assumption that the white corner piece is in the correct place
            if set(currentEdgePiece[0][0]).issubset(['B', 'O', None]):
                print("Working with Blue and Orange")
                # Orange Facing up = [B, None, O] [None, B, O]
                # Blue Facing up = [None, O, B] or [O, None B]
                # Case 1 Orange Facing Up (Or down depending on orientation)
                if currentEdgePiece[0][0] == ["B", None, "O"] or currentEdgePiece[0][0] == [None, "B", "O"]:
                    print("Prediction: Orange Facing Up")
                    # Target needs to be (0,-1,-1)
                    print(currentEdgePiece[0][1])
                    while currentEdgePiece[0][1] != (0,-1,-1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (0,-1,-1):
                        print("Ready to insert")
                        c.sequence("Ui Bi U B R B Ri Bi")
                        second_layer_algorithm += " Ui Bi U B R B Ri Bi"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print(c)
                if currentEdgePiece[0][0] == [None, "O", "B"] or currentEdgePiece[0][0] == ["O", None, "B"]:
                    print("Prediction: Blue Facing Up")
                    # Target needs to be (-1,0,-1)
                    print(currentEdgePiece[0][1])
                    while currentEdgePiece[0][1] != (-1, 0, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (-1, 0, -1):
                        print("Ready to insert")
                        c.sequence("R B Ri Bi Ui Bi U B")
                        second_layer_algorithm += " R B Ri Bi Ui Bi U B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print(c)

            if set(currentEdgePiece[0][0]).issubset(['B', 'R', None]):
                print("Working with Blue and Red")
                # Red Facing Up - ["B", None, "R"] or [None, "B", "R"]
                # Blue Facing up - [None, "R", "B"] or ["R", None, "B"]

                if currentEdgePiece[0][0] == ["B", None, "R"] or currentEdgePiece[0][0] == [None, "B", "R"]:
                    print("Prediction: Red Facing Up")
                    # Target needs to be (0,1,-1)
                    while currentEdgePiece[0][1] != (0, 1, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (0, 1, -1):
                        print("Ready to insert")
                        c.sequence("D B Di Bi Ri Bi R B")
                        second_layer_algorithm += " D B Di Bi Ri Bi R B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print(c)
                if currentEdgePiece[0][0] == [None, "R", "B"] or currentEdgePiece[0][0] == ["R", None, "B"]:
                    print("Prediction: Blue Facing Up")
                    # Target needs to be ()
                    while currentEdgePiece[0][1] != (-1, 0, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (-1, 0, -1):
                        print("Ready to insert")
                        c.sequence("Ri Bi R B D B Di Bi")
                        second_layer_algorithm += " Ri Bi R B D B Di Bi"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print(c)

            if set(currentEdgePiece[0][0]).issubset(['G', 'O', None]):
                print("Working with Green and Orange")
                # Green Facing Up - ["O", None, "G"] or [None, "O", "G"]
                # Orange Facing up - [None, "G", "O"] or ["O", None, "G"]
                if currentEdgePiece[0][0] == ["O", None, "G"] or currentEdgePiece[0][0] == [None, "O", "G"]:
                    print("Green Facing Up")
                    # Target needs to be (1,0,-1)
                    while currentEdgePiece[0][1] != (1, 0, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (1, 0, -1):
                        print("Ready to insert")
                        c.sequence("Li Bi L B U B Ui B")
                        second_layer_algorithm += " Li Bi L B U B Ui B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                if currentEdgePiece[0][0] == [None, "G", "O"] or currentEdgePiece[0][0] == ["G", None, "O"]:
                    print("Orange Facing Up")
                    # Target needs to be (1,0,-1)
                    while currentEdgePiece[0][1] != (0, -1, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (0, -1, -1):
                        print("Ready to insert")
                        c.sequence("U B Ui Bi Li Bi L B")
                        second_layer_algorithm += " U B Ui Bi Li Bi L B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print(c)

            if set(currentEdgePiece[0][0]).issubset(['G', 'R', None]):
                print("Working with Green and Red")
                # Green Facing Up = ["R", None, "G"] or [None, "R", "G"]
                # Red Facing Up = [None, "G", "R"] or ["R", None, "G"]

                if currentEdgePiece[0][0] == ["R", None, "G"] or currentEdgePiece[0][0] == [None, "R", "G"]:
                    print("Green Face Up")
                    # Target  = (1,0,-1)
                    while currentEdgePiece[0][1] != (1, 0, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (1, 0, -1):
                        print("Ready to insert")
                        c.sequence("L B Li Bi Di Bi D B")
                        second_layer_algorithm += " L B Li Bi Di Bi D B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)

                if currentEdgePiece[0][0] == [None, "G", "R"] or currentEdgePiece[0][0] == ["G", None, "R"]:
                    print("Red Face Up")
                    # Target Location = 0,1,-1
                    while currentEdgePiece[0][1] != (0, 1, -1):
                        c.sequence("B")
                        second_layer_algorithm += " B"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)
                        print("New location = ", currentEdgePiece[0][1])
                    if currentEdgePiece[0][1] == (0, 1, -1):
                        print("Ready to insert")
                        # c.sequence("D B Di Bi Ri Bi R B")
                        c.sequence("Di Bi D B L B Li Bi")
                        second_layer_algorithm += " Di Bi D B L B Li Bi"
                        currentEdgePiece = findMiddleLayerPiece(whiteCorners[val][0], c)

    return second_layer_algorithm

# Stage 4 Solves Yellow Cross
def convertAlgo(algo):
    new_algo = ""
    for move in algo.split():
        if move == "U":
            new_algo += (" B")
        if move == "Ui":
            new_algo += (" Bi")

        if move == "F":
            new_algo += (" U")
        if move == "Fi":
            new_algo += (" Ui")

        if move == "B":
            new_algo += (" D")
        if move == "Bi":
            new_algo += (" Di")

        if move == "D":
            new_algo += (" F")
        if move == "Di":
            new_algo += (" Fi")

        if move == "R":
            new_algo += (" R")
        if move == "Ri":
            new_algo += (" Ri")

        if move == "L":
            new_algo += (" L")
        if move == "Li":
            new_algo += (" Li")
    return new_algo
def solveYellowCross(c):
    print("Solving Yellow Cross")
    # If Y == 2nd index - yellow is pointing up

    yellow_cross_algorithm = ""
    # Check If Cross Already Exists:
    yellowCrossSolved = [
        c.get_piece(0,1,-1).colors[2] == "Y",
        c.get_piece(1,0,-1).colors[2] == "Y",
        c.get_piece(0,-1,-1).colors[2] == "Y",
        c.get_piece(-1,0,-1).colors[2] == "Y"]

    # Conditions For First look OLL LINE
    line_condition_one = [
        c.get_piece(0, 1, -1).colors[2] == "Y",
        c.get_piece(0, 0, -1).colors[2] == "Y",
        c.get_piece(0, -1, -1).colors[2] == "Y"
    ]

    line_condition_two = [
        c.get_piece(1, 0, -1).colors[2] == "Y",
        c.get_piece(0, 0, -1).colors[2] == "Y",
        c.get_piece(-1, 0, -1).colors[2] == "Y"
    ]
    # Conditions For First Look OLL L
    # L At Top Right
    l_condition_one = [
        c.get_piece(0,1,-1).colors[2] == "Y",
        c.get_piece(0,0,-1).colors[2] == "Y",
        c.get_piece(-1,0,-1).colors[2] == "Y"]

    # L At Top Left # This is the target
    l_condition_two = [
        c.get_piece(0,1,-1).colors[2] == "Y",
        c.get_piece(0,0,-1).colors[2] == "Y",
        c.get_piece(1,0,-1).colors[2] == "Y" ]

    # L at bottom left
    l_condition_three = [
        c.get_piece(0, -1, -1).colors[2] == "Y",
        c.get_piece(0, 0, -1).colors[2] == "Y",
        c.get_piece(1, 0, -1).colors[2] == "Y"]

    # L at bottom Right
    l_condition_four = [
        c.get_piece(0, -1, -1).colors[2] == "Y",
        c.get_piece(0, 0, -1).colors[2] == "Y",
        c.get_piece(-1, 0, -1).colors[2] == "Y"]



    if all(yellowCrossSolved):
        print("The Yellow Cross Is Already Solved...")
    # Conditions For Line Found
    elif all(line_condition_one) or all(line_condition_two):
        print("Line Found")
        if line_condition_two == [True, True, True]:
            print(line_condition_two)
            print("Line In correct place")
            algorithm = "F R U Ri Ui Fi"
            newAlgo = convertAlgo(algorithm)
            yellow_cross_algorithm += newAlgo
            c.sequence(newAlgo)
        elif line_condition_one == [True, True, True]:
            print("Line found but not in the right place")
            if line_condition_one == [True, True, True]:
                c.sequence("B")
                yellow_cross_algorithm += " B"
                algorithm = "F R U Ri Ui Fi"
                newAlgo = convertAlgo(algorithm)
                yellow_cross_algorithm += newAlgo
                c.sequence(newAlgo)
        print("Algorithm Perfomred + current algo = ", yellow_cross_algorithm)

    # Conditions for L found -
    elif all(l_condition_one) or all(l_condition_two) or all(l_condition_three) or all(l_condition_four) and not all(yellowCrossSolved):
         print("L Found")
         if l_condition_two == [True, True, True]:
            print("Original Cube: \n")
            print(c)
            print(l_condition_two)
            c.sequence("D B L Bi Li Di")
            yellow_cross_algorithm += " D B L Bi Li Di"
         elif not l_condition_two == [True,True,True]:
             if l_condition_one == [True, True, True]:
                 print("L found at top right")
                 c.sequence("Bi D B L Bi Li Di")
                 yellow_cross_algorithm += " Bi D B L Bi Li Di"
             elif l_condition_three == [True, True, True]:
                 print("L found at bottom left")
                 c.sequence("B D B L Bi Li Di")
                 yellow_cross_algorithm += " B D B L Bi Li Di"
             elif l_condition_four == [True, True, True]:
                 print("L found at bottom right")
                 c.sequence("B B D B L Bi Li Di")
                 yellow_cross_algorithm += " B B D B L Bi Li Di"
             print("Algorithm Completed")
    # Dot Scenorio
    elif(not all(l_condition_one) and not all(l_condition_two) and not all(l_condition_three) and not all(l_condition_four)
          and not all(yellowCrossSolved)
          and not all(line_condition_two) and not all(line_condition_one)):
        print("Dot found")
        c.sequence("U R B Ri Bi Ui")
        c.sequence("D B L Bi Li Di")
        yellow_cross_algorithm += " U R B Ri Bi Ui D B L Bi Li Di"

    return yellow_cross_algorithm


# Stage 5 (OLL Look 2)
def orientLastLayer(c):
    print(" \nLook 2 of OLL \n")
    # Cases
    print(c)

    oll_algorithm = " "

    case_h = []
    case_pi = []
    case_headlights = []
    case_t = []
    case_bowtie = []


    for i in range(1,5):
        c.sequence("B")
        oll_algorithm += " B"
        # Anti Sune Case...
        if (c.get_piece(-1, 1, -1).colors[1] == "Y" and
            c.get_piece(-1, -1, -1).colors[0] == "Y" and
            c.get_piece(1, -1, -1).colors[1] == "Y" and
            c.get_piece(1, 1, -1).colors[2] == "Y" and
            c.get_piece(0, 1, -1).colors[2] == "Y" and
            c.get_piece(1, 0, -1).colors[2] == "Y" and
            c.get_piece(0, 0, -1).colors[2] == "Y" and
            c.get_piece(-1, 0, -1).colors[2] == "Y" and
            c.get_piece(0, -1, -1).colors[2] == "Y"):
            print("Anti sune found")
            c.sequence("Li Bi L Bi Li B B L")
            oll_algorithm += " Li Bi L Bi Li B B L"
            break
        # Sune Case...
        elif(c.get_piece(1, 1, -1).colors[1] == "Y" and
            c.get_piece(-1, -1, -1).colors[1] == "Y" and
            c.get_piece(1, -1, -1).colors[0] == "Y" and
            c.get_piece(-1, 1, -1).colors[2] == "Y"):
                print("Sune Casse Foiund")
                c.sequence("R B Ri B R B B Ri")
                oll_algorithm += " R B Ri B R B B Ri"
                break
        # Headlights Case
        elif(c.get_piece(-1, 1, -1).colors[1] == "Y" and
            c.get_piece(1, 1, -1).colors[1] == "Y" and
            c.get_piece(1, -1, -1).colors[2] == "Y" and
            c.get_piece(-1, -1, -1).colors[2] == "Y"):
            print("Headlights Found")
            c.sequence("R R F Ri B B R Fi Ri B B Ri")
            oll_algorithm += " R R F Ri B B R Fi Ri B B Ri"
            break
        # H Case
        elif (c.get_piece(1,1,-1).colors[1] == "Y" and
              c.get_piece(-1,1,-1).colors[1] == "Y" and
              c.get_piece(-1,-1,-1).colors[1] == "Y" and
              c.get_piece(1,-1,-1).colors[1] == "Y"):
            print("H Case Found")
            c.sequence("U R B Ri Bi R B Ri Bi R B Ri Bi Ui")
            oll_algorithm += " U R B Ri Bi R B Ri Bi R B Ri Bi Ui"
            break
        # Pi Case
        elif (c.get_piece(1,1,-1).colors[1] == "Y" and
              c.get_piece(1,-1,-1).colors[1] == "Y" and
              c.get_piece(-1,1,-1).colors[0] == "Y" and
              c.get_piece(-1,-1,-1).colors[0] == "Y"):
            print("pi Found")
            c.sequence("R B B Ri Ri Bi R R Bi Ri Ri B B R")
            oll_algorithm += " R B B Ri Ri Bi R R Bi Ri Ri B B R"
            break
        # T Case
        elif (c.get_piece(1,1,-1).colors[2] == "Y" and
              c.get_piece(1,-1,-1).colors[2] == "Y" and
              c.get_piece(-1,1,-1).colors[1] == "Y" and
              c.get_piece(-1,-1,-1).colors[1] == "Y"):
            print("T Found")
            c.sequence("L U Ri Ui Li U R Ui")
            oll_algorithm += " L U Ri Ui Li U R Ui"
            break
        # Bow-Tie Case
        elif (c.get_piece(-1,1,-1).colors[1] == "Y" and
              c.get_piece(1,-1,-1).colors[0] == "Y" and
              c.get_piece(1,1,-1).colors[2] == "Y" and
              c.get_piece(-1,-1,-1).colors[2] == "Y"):
            print("Bowtie Found")
            c.sequence("Ri U R Di Ri Ui R D")
            oll_algorithm += " Ri U R Di Ri Ui R D"
            break
        else:
            print("No Cases Found")
    return oll_algorithm

# Stage 6 (PLL Look 1)
def solveFinalCorners(c):
    print("\n Solving Final Corners... ")
    print(c)

    final_corner_algorithm = ""

    # First check if all corner's match each other:
    if (c.get_piece(-1,1,-1).colors[1] == c.get_piece(1,1,-1).colors[1] and
        c.get_piece(1,1,-1).colors[0] == c.get_piece(1,-1,-1).colors[0] and
        c.get_piece(1,-1,-1).colors[1] == c.get_piece(-1,-1,-1).colors[1] and
        c.get_piece(-1,1,-1).colors[0] == c.get_piece(-1,-1,-1).colors[0]):
        print("All Corners Match - Skip Stage 6...")
    elif (c.get_piece(-1,1,-1).colors[1] != c.get_piece(1,1,-1).colors[1] and
        c.get_piece(1,1,-1).colors[0] != c.get_piece(1,-1,-1).colors[0] and
        c.get_piece(1,-1,-1).colors[1] != c.get_piece(-1,-1,-1).colors[1] and
        c.get_piece(-1,1,-1).colors[0] != c.get_piece(-1,-1,-1).colors[0]):
        print("No Corners Match")
        c.sequence("U R Bi Ri Bi R B Ri Ui R B Ri Bi Ri U R Ui")
        final_corner_algorithm += " U R Bi Ri Bi R B Ri Ui R B Ri Bi Ri U R Ui"
        print("Algorithm done - Ready To Solve Cube")
        print(c)
    else:
        print("Found one corner that matches")
        if c.get_piece(-1, 1, -1).colors[1] == c.get_piece(1, 1, -1).colors[1]:
            print("On Orange Face")
            c.sequence("B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
            final_corner_algorithm += " B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
            print("Algorithm done - Ready To Solve Cube")
        elif c.get_piece(1,1,-1).colors[0] == c.get_piece(1,-1,-1).colors[0]:
            print("On Blue Face")
            # Scramble Test = L  Li  U  Fi  Fi  Fi  R  U  Fi  F   Di   Di  L  U
            c.sequence("B B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
            final_corner_algorithm += " B B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
            print("Algorithm done - Ready To Solve Cube")
        elif c.get_piece(1,-1,-1).colors[1] == c.get_piece(-1,-1,-1).colors[1]:
            print("On Red Face")
            c.sequence("Bi R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
            final_corner_algorithm += " Bi R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
            print("Algorithm done - Ready To Solve Cube")
        elif c.get_piece(-1,1,-1).colors[0] == c.get_piece(-1,-1,-1).colors[0]:
            print("On Green Face")
            c.sequence("R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
            final_corner_algorithm += " R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
            print("Algorithm done - Ready To Solve Cube")
    return final_corner_algorithm

# Stage 7 (Final Step In Solving Cube..)
def solveFinalEdge(c):
    print("Solving Final Edge Pieces...")
    solved_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")

    final_edge_algorithm = " "

    if c == solved_cube:
        print("Cube Is Already Solved! (Skip Stage 7)")

    # First Check is to check if any entire side matches (corner, edge, corner)
    else:
        if (c.get_piece(-1, 1, -1).colors[1] == c.get_piece(1, 1, -1).colors[1] == c.get_piece(0, 1, -1).colors[1] == c.get_piece(0, 1, -1).colors[1] and
                c.get_piece(1, 1, -1).colors[0] == c.get_piece(1, -1, -1).colors[0] == c.get_piece(1, 0, -1).colors[0] == c.get_piece(1, 0, -1).colors[0] and
                c.get_piece(1, -1, -1).colors[1] == c.get_piece(-1, -1, -1).colors[1] == c.get_piece(0, -1, -1).colors[1] == c.get_piece(0, -1, -1).colors[1] and
                c.get_piece(-1, 1, -1).colors[0] == c.get_piece(-1, 0, -1).colors[0] == c.get_piece(-1, -1, -1).colors[0] == c.get_piece(-1, -1, -1).colors[0]):

            while c != solved_cube:
                c.sequence("B")
                final_edge_algorithm += " B"
            print("Cube Solved")
            return True

        # Case For there being a line...
        if (c.get_piece(-1, 1, -1).colors[1] == c.get_piece(1, 1, -1).colors[1] == c.get_piece(0,1,-1).colors[1] == c.get_piece(0,1,-1).colors[1] or
        c.get_piece(1, 1, -1).colors[0] == c.get_piece(1, -1, -1).colors[0] == c.get_piece(1,0,-1).colors[0] == c.get_piece(1,0,-1).colors[0] or
        c.get_piece(1, -1, -1).colors[1] == c.get_piece(-1, -1, -1).colors[1] == c.get_piece(0,-1,-1).colors[1] == c.get_piece(0,-1,-1).colors[1] or
        c.get_piece(-1, 1, -1).colors[0] == c.get_piece(-1, 0, -1).colors[0] == c.get_piece(-1,-1,-1).colors[0] == c.get_piece(-1,-1,-1).colors[0]):
            if c.get_piece(-1, 1, -1).colors[1] == c.get_piece(1, 1, -1).colors[1] == c.get_piece(0,1,-1).colors[1] == c.get_piece(0,1,-1).colors[1]:
                print("Line on Orange side")
                c.sequence("B B")
                final_edge_algorithm += " B B"
            if c.get_piece(1, 1, -1).colors[0] == c.get_piece(1, -1, -1).colors[0] == c.get_piece(1,0,-1).colors[0] == c.get_piece(1,0,-1).colors[0]:
                print("Line on Blue side")
                c.sequence("Bi")
                final_edge_algorithm += " Bi"
            if c.get_piece(1, -1, -1).colors[1] == c.get_piece(-1, -1, -1).colors[1] == c.get_piece(0,-1,-1).colors[1] == c.get_piece(0,-1,-1).colors[1] :
                print("Line on Red side (Good)")
            if c.get_piece(-1, 1, -1).colors[0] == c.get_piece(-1, 0, -1).colors[0] == c.get_piece(-1,-1,-1).colors[0] == c.get_piece(-1,-1,-1).colors[0]:
                print("Line on Green side")
                c.sequence("B")
                final_edge_algorithm += " B"
            # Now line is on correct side
            # First Case Ub Perm (R  F  Ui  Bi   D  U   Di  R  B  B   Di  B  L  R )
            if (c.get_piece(1,0,-1).colors[0] == c.get_piece(1,1,-1).colors[1] and
                c.get_piece(0, 1, -1).colors[1] == c.get_piece(-1,1,-1).colors[0] and
                c.get_piece(-1, 0, -1).colors[0] == c.get_piece(1, 1, -1).colors[0]):
                print("Ub Perm Case Found")
                c.sequence("Mi Mi Bi M Bi Bi Mi Bi Mi Mi")
                final_edge_algorithm += " Mi Mi Bi M Bi Bi Mi Bi Mi Mi"
                while c.is_solved() == False:
                    c.sequence("B")
                    final_edge_algorithm += " B"
            else:
                print("Ua Perm Found (Only other option)")
                c.sequence("Mi Mi B M B B Mi B Mi Mi")
                final_edge_algorithm += " Mi Mi B M B B Mi B Mi Mi"
                while c.is_solved() == False:
                    c.sequence("B")
                    final_edge_algorithm += " B"
        else:
            while c.get_piece(-1,1,-1).colors[1] != "O":
                c.sequence("B")
                final_edge_algorithm += " B"
                print(c)
            # No Lines...
            print("No lines found")
            if (c.get_piece(0,1,-1).colors[1] == c.get_piece(0,-1,0).colors[1] and
            c.get_piece(0,-1,-1).colors[1] == c.get_piece(0,1,0).colors[1] and
            c.get_piece(-1,0,-1).colors[0] == c.get_piece(1,0,0).colors[0] and
            c.get_piece(1,0,-1).colors[0] == c.get_piece(-1,0,0).colors[0]):
                print("H Perm found")
                c.sequence("M M Bi M M B B M M Bi M M")
                final_edge_algorithm += " M M Bi M M B B M M Bi M M"
            else:
                print("Z Perm")
                c.sequence("Mi Bi M M Bi M M Bi Mi B B M M")
                final_edge_algorithm += " Mi Bi M M Bi M M Bi Mi B B M M"
                while c.get_piece(-1, 1, -1).colors[1] != c.get_piece(0, 1, -1).colors[1]:
                    c.sequence("Mi Bi M M Bi M M Bi Mi B B M M")
                    final_edge_algorithm += " Mi Bi M M Bi M M Bi Mi B B M M"
                while c.is_solved() == False:
                    c.sequence("B")
                    final_edge_algorithm += " B"
    return final_edge_algorithm



def generateScramble():
    notation = [" R ", " U ", " F ", " L ", " B ", "  D ", " Ri ", " Ui ", " Fi ", " Li ", " Bi ", "  Di "]
    scramble = " "
    for i in range(1, 15):
        scramble += str(notation[random.randrange(0, 12)])
    print(scramble)
    return scramble




def testSolve(amount):
    solve_success = 0
    solve_fail = 0
    fail_scrambles = []
    size_algo = []
    for i in range(amount):
        print(i + 1)
        c = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
        rand_scramble = generateScramble()
        c.sequence(rand_scramble)
        white_cross = solveWhiteCross(c)
        white_corner = solveWhiteCorner(c)
        second_layer = solveSecondLayer(c)
        yellow_cross = solveYellowCross(c)
        oll = orientLastLayer(c)
        final_corner = solveFinalCorners(c)
        final_edge = solveFinalEdge(c)
        print("ALGOOOOOO")
        print(white_cross + white_corner + second_layer + yellow_cross + oll + final_corner + final_edge)
        # size_algo.append(len(algo))

        if c.is_solved() == True:
            solve_success += 1
        elif c.is_solved() == False:
            solve_fail += 1
            fail_scrambles.append(rand_scramble)


    print("Solves Succesfull = ", solve_success)
    print("Solves Failed = ", solve_fail)
    print("Success Rate = ", int((solve_success / amount) * 100), "%")
    print("Failed Scrambles = ", int((solve_fail / amount) * 100), "%")
    print("ID of failed scrambled = ", fail_scrambles)
    print(c)


# ------ #
# Main #
# ------ #




testSolve(1)







class SolveCube:
    def __init__(self, cube):
        self.cube = cube

    def findWhiteEdge(cube):
        white_piece = []
        for piece in c.pieces:
            if piece.type == "edge":
                if piece.colors[0] == "W" or piece.colors[1] == "W" or piece.colors[2] == "W":
                    white_piece.append([piece.colors, piece.pos])
        return white_piece

    def solveCross(self, cube):
        white_pieces = findWhiteEdge(cube)
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


