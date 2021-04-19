from rubik.cube import Cube
from rubik_solver import utils
import pycuber as pc
import random
class SolveCube:
    def __init__(self, cube):
        self.c = cube

    # Setup Methods:
    def findWhiteEdge(self):
        white_piece = []
        for piece in self.c.pieces:
            if piece.type == "edge":
                if piece.colors[0] == "W" or piece.colors[1] == "W" or piece.colors[2] == "W":
                    white_piece.append([piece.colors, piece.pos])
            # Return Ordered List --> BLUE / GREEN / ORANGE / RED (doesnt work)
        list_copy = white_piece
        print("Original White = ")
        print(white_piece)
        myorder = ['B', 'G', 'O', 'R']
        mysortedlist = []
        for colour in myorder:
            for item in white_piece:
                if colour in item[0]:
                    mysortedlist.append(item)


        return mysortedlist

    def findWhiteCorner(self):
        white_piece = []
        # Loop through the entire cube
        for piece in self.c.pieces:
            # Find all corner pieces
            if piece.type == "corner":
                # Find all corner pieces that have "W" (White) in them - there should only be 4
                if piece.colors[0] == "W" or piece.colors[1] == "W" or piece.colors[2] == "W":
                    # Append the corner pieces to a list, as well as their positions
                    white_piece.append([piece.colors, piece.pos])
        # Return the list.
        return white_piece

    def findMiddleLayerPiece(self, cornerPiece):
        target_colours = []
        target_piece = []
        for val in cornerPiece:
            if val != "W":
                target_colours.append(val)
        target_colours.append(None)
        for piece in self.c.pieces:
            if piece.type == "edge":
                if set(piece.colors).issubset(target_colours):
                    target_piece.append([piece.colors, piece.pos])
        return target_piece

    def convertAlgo(self, algo):
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
    # Commented
    def solveWhiteCross(self):
        white_pieces = self.findWhiteEdge()
        possible_faces = ["B", "G", "O", "R"]
        white_blue_solved = False
        white_green_solved = False
        white_orange_solved = False
        white_red_solved = False
        cross_algorithm = ""
        count = 1
        for val in range(len(white_pieces)):
            print(self.c)
            print("Itter " + str(count + 1))
            # -------------------------------------
            # Now Solving the White / Blue Face
            # -------------------------------------
            if "B" in white_pieces[val][0]:
                # Cases for blue/white being on GREEN Face
                # Case 1 and 1a
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "B":
                    print("Case 1 Found")
                    # New Algorithm: L F D Fi
                    self.c.sequence("L F D Fi")
                    cross_algorithm += " L F D Fi"
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "B":
                    print("Case 2 Found")
                    self.c.sequence("L F F Li Fi Fi")
                    cross_algorithm += " L F F Li Fi Fi"
                # Case 2 and 2a
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "B":
                    print("Case 3 Found")
                    self.c.sequence("Fi Fi L F F")
                    cross_algorithm += " Fi Fi L F F"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "B":
                    print("Case 4 Found")
                    self.c.sequence("Fi Ui F")
                    cross_algorithm += " Fi Ui F"
                # Case 3 and 3a
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "B":
                    print("Case 5 Found")
                    # New = Bi Bi Ri FI U F
                    # Old = Bi Ui Fi L F F
                    self.c.sequence("Bi Bi Ri Fi U F")
                    cross_algorithm += "Bi Bi Ri Fi U F"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "B":
                    print("Case 6 Found")
                    self.c.sequence("Bi Bi R R")
                    cross_algorithm += " Bi Bi R R"
                # Case 4 and 4a
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "B":
                    print("Case 7 Found")
                    self.c.sequence("F D Fi")
                    cross_algorithm += " F D Fi"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "B":
                    print("Case 8 Found")
                    self.c.sequence("F F Li F F")
                    cross_algorithm += " F F Li F F"
                # Cases for blue/white being on RED Face
                # Case 5 and 5a
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "B":
                    print("Case 9 Found")
                    self.c.sequence("D R")
                    cross_algorithm += " D R"
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "B":
                    print("Case 10 Found")
                    self.c.sequence("D F Di Fi")
                    cross_algorithm += " D F Di Fi"
                # Case 6 and 6a
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "B":
                    print("Case 11 Found")
                    self.c.sequence("F Di Fi")
                    cross_algorithm += " F Di Fi"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "B":
                    print("Case 12 Found")
                    self.c.sequence("R")
                    cross_algorithm += " R"
                # Case 7 and 7a
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "B":
                    print("Case 13 Found")
                    self.c.sequence("Di R D")
                    cross_algorithm += " Di R D"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "B":
                    print("Case 14 Found")
                    self.c.sequence("B R R")
                    cross_algorithm += " B R R"
                # Cases for blue/white being on BLUE Face
                # Case 8 and 8a
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "B":
                    print("Case 15 Found")
                    self.c.sequence("R Fi U F")
                    cross_algorithm += " R Fi U F"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "B":
                    print("Case 16 Found")
                    print("CORRECT POSITION")
                # Case 9
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "B":
                    print("Case 17 Found")
                    self.c.sequence("Ri")
                    cross_algorithm += " Ri "
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "B":
                    print("Case 18 Found")
                    self.c.sequence("Fi U F")
                    cross_algorithm += " Fi U F"
                # Case 10
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "B":
                    print("Case 19 Found")
                    self.c.sequence("R R")
                    cross_algorithm += " R R"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "B":
                    print("Case 20 Found")
                    self.c.sequence("Ri Fi U F")
                    cross_algorithm += " Ri Fi U F"
                # Final Cases for Orange and Yellow face....
                # Case 11
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "B":
                    print("Case 21 Found")
                    self.c.sequence("Ui Fi U F")
                    cross_algorithm += " Ui Fi U F"
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "B":
                    print("Case 22 Found")
                    self.c.sequence("Ui Ri")
                    cross_algorithm += " Ui Ri"
                # Case 12
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "B":
                    print("Case 23 Found")
                    self.c.sequence("Bi R R")
                    cross_algorithm += " Bi R R"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "B":
                    print("Case 24 Found")
                    self.c.sequence("Bi Ri Fi U F")
                    cross_algorithm += " Bi Ri Fi U F"
                white_pieces = self.findWhiteEdge()
            # -------------------------------------
            # Now Solving the White / Green Face
            # -------------------------------------

            if "G" in white_pieces[val][0]:
                # Cases for blue/white being on GREEN Face
                # Case 1 and 2
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "G":
                    print("Case25 Found")
                    print("Correct Position No Algorithm")
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "G":
                    print("Case 26 Found")
                    self.c.sequence("L Fi D F")
                    cross_algorithm += " L Fi D F"
                # Case 3 and 4
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "G":
                    print("Case 27 Found")
                    self.c.sequence("F Ui Fi")
                    cross_algorithm += " F Ui Fi"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "G":
                    print("Case 28 Found")
                    self.c.sequence("L")
                    cross_algorithm += " L"
                # Case 5 and 6
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "G":
                    print("Case 29 Found")
                    self.c.sequence("L L")
                    cross_algorithm += " L L"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "G":
                    print("Case 30 Found")
                    self.c.sequence("Li Fi D F")
                    cross_algorithm += " Li Fi D F"
                # Case 7 and 8
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "G":
                    print("Case 31 Found")
                    self.c.sequence("Fi D F")
                    cross_algorithm += " Fi D F"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "G":
                    print("Case 32 Found")
                    self.c.sequence("Li")
                    cross_algorithm += " Li"
                # Case for green/white being on RED SIDE
                # Case 9 and 10
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "G":
                    print("Case 33 Found")
                    self.c.sequence("Di Li")
                    cross_algorithm += " Di Li"
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "G":
                    print("Case 34 Found")
                    self.c.sequence("D Fi Di F")
                    cross_algorithm += " D Fi Di F"
                # Case 11 and 12
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "G":
                    print("Case 35 Found")
                    self.c.sequence("Fi Di F")
                    cross_algorithm += " Fi Di F"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "G":
                    print("Case 36 Found")
                    self.c.sequence("Fi Fi R F F")
                    cross_algorithm += " Fi Fi R F F"
                # Case 13 and 14
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "G":
                    print("Case 37 Found")
                    self.c.sequence("Bi Li Fi D F")
                    cross_algorithm += " Bi Li Fi D F"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "G":
                    print("Case 38 Found")
                    self.c.sequence("Bi L L")
                    cross_algorithm += " Bi L L"
                # Case for green/white being on BLUE SIDE
                # Case 15 and 16
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "G":
                    print("Case 39 Found")
                    self.c.sequence("Ri F F R F F")
                    cross_algorithm += " Ri F F R F F"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "G":
                    print("Case 40 Found")
                    self.c.sequence("R F U Fi")
                    cross_algorithm += " R F U Fi"
                # Case 17 and 18
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "G":
                    print("Case 41 Found")
                    self.c.sequence("F U Fi")
                    cross_algorithm += " F U Fi"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "G":
                    print("Case 42 Found")
                    self.c.sequence("F F Ri F F")
                    cross_algorithm += " F F Ri F F"
                # Case 19 and 20
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "G":
                    print("Case 43 Found")
                    self.c.sequence("B B L L")
                    cross_algorithm += " B B L L"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "G":
                    print("Case 44 Found")
                    self.c.sequence("B B Li Fi D F")
                    cross_algorithm += " B B Li Fi D F"
                # Case 21 and 22
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "G":
                    print("Case 45 Found")
                    self.c.sequence("B Li Fi D F")
                    cross_algorithm += " B Li Fi D F"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "G":
                    print("Case 46 Found")
                    self.c.sequence("B L L")
                    cross_algorithm += " B L L"
                # Final Case (22 and 24)
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "G":
                    print("Case 47 Found")
                    self.c.sequence("U F Ui Fi")
                    cross_algorithm += " U F Ui Fi"
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "G":
                    print("Case 48 Found")
                    self.c.sequence("U L")
                    cross_algorithm += " U L"
                white_pieces = self.findWhiteEdge()
            # -------------------------------------
            # Now Solving the White / Orange Face
            # -------------------------------------
            if "O" in white_pieces[val][0]:
                # Case for White / Orange being on the GREEN FACE
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "O":
                    print("Case 49 Found")
                    self.c.sequence("Fi L F")
                    cross_algorithm += " Fi L F"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "O":
                    print("Case 50 Found")
                    self.c.sequence("Ui")
                    cross_algorithm += " Ui"
                # Case 3 and 4
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "O":
                    print("Case 51 Found")
                    self.c.sequence("Fi L F Ui")
                    cross_algorithm += " Fi L F Ui"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "O":
                    print("Case 52 Found")
                    self.c.sequence("Bi U U")
                    cross_algorithm += " Bi U U"
                # Case 5 and 6
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "O":
                    print("Case 53 Found")
                    self.c.sequence("Fi Li F")
                    cross_algorithm += " Fi Li F"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "O":
                    print("Case 54 Found")
                    self.c.sequence("F F D F F")
                    cross_algorithm += " F F D F F"
                # Case 7 and 8
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "O":
                    print("Case 55 Found")
                    self.c.sequence("Li Ui")  # correct case'
                    cross_algorithm += " Li Ui"
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "O":
                    print("Case 56 Found")
                    self.c.sequence("L Fi Li F")
                    cross_algorithm += " L Fi Li F"
                # White and Orange on RED FACE
                # Case 9 and 10
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "O":
                    print("Case 57 Found")
                    self.c.sequence("M M B B M M")
                    cross_algorithm += " M M B B M M"
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "O":
                    print("Case 58 Found")
                    self.c.sequence(" D F R Fi")
                    cross_algorithm += " D F R Fi"
                # Case 11 and 12
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "O":
                    print("Case 59 Found")
                    self.c.sequence("F R Fi")
                    cross_algorithm += " F R Fi"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "O":
                    print("Case 60 Found")
                    self.c.sequence("F F Di F F")
                    cross_algorithm += " F F Di F F"
                # Case 13 and 14
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "O":
                    print("Case 61 Found")
                    self.c.sequence("B B U U")
                    cross_algorithm += " B B U U"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "O":
                    print("Case 62 Found")
                    self.c.sequence("Di F R Fi")
                    cross_algorithm += " Di F R Fi"
                # Case 15 and 16
                # White and Orange on BLUE FACE
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "O":
                    print("Case 63 Found")
                    self.c.sequence("R U")
                    cross_algorithm += " R U"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "O":
                    print("Case 64 Found")
                    self.c.sequence("Ri F R Fi")
                    cross_algorithm += " Ri F R Fi"
                # Case 17 and 18
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "O":
                    print("Case 65 Found")
                    self.c.sequence("F Ri Fi")
                    cross_algorithm += " F Ri Fi"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "O":
                    print("Case 66 Found")
                    self.c.sequence("U")
                    cross_algorithm += " U "
                # Case 19 and 20
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "O":
                    print("Case 67 Found")
                    self.c.sequence("B U U")
                    cross_algorithm += " B U U"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "O":
                    print("Case 68 Found")
                    # Updated Algorithm: B Ui Fi L F
                    # Old Algorithm: Fi Ri F U
                    self.c.sequence("B Ui Fi L F")
                    cross_algorithm += " B Ui Fi L F"
                # Case 21 and 22
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "O":
                    print("Case 69 Found")
                    print("Correct position")
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "O":
                    print("Case 70 Found")
                    self.c.sequence("U Fi L F")
                    cross_algorithm += " U Fi L F"
                # Case 23 and 24
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "O":
                    print("Case 71 Found")
                    self.c.sequence("Ui Fi L F")
                    cross_algorithm += " Ui Fi L F"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "O":
                    print("Case 72 Found")
                    self.c.sequence("U U")
                    cross_algorithm += " U U"

            white_pieces = self.findWhiteEdge()

            # -------------------------------------
            # Now Solving the White / RED Face
            # -------------------------------------
            if "R" in white_pieces[val][0]:
                # Case for White / Orange being on the GREEN FACE
                # Case 1 and 2
                if white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][0] == "R":
                    print("Case 73 Found")
                    self.c.sequence(" L F Li Fi")
                    cross_algorithm += " L F Li Fi"
                elif white_pieces[val][1] == (-1, 0, 1) and white_pieces[val][0][2] == "R":
                    print("Case 74 Found")
                    self.c.sequence("L D")
                    cross_algorithm += " L D"
                # Case 3 and 4
                if white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][1] == "R":
                    print("Case 75 Found")
                    self.c.sequence("F F Ui F F")
                    cross_algorithm += " F F Ui F F"
                elif white_pieces[val][1] == (-1, 1, 0) and white_pieces[val][0][0] == "R":
                    print("Case 76 Found")
                    self.c.sequence("F L Fi")
                    cross_algorithm += " F L Fi"
                # Case 5 and 6
                if white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][0] == "R":
                    print("Case 77 Found")
                    self.c.sequence("B D D")
                    cross_algorithm += " B D D"
                elif white_pieces[val][1] == (-1, 0, -1) and white_pieces[val][0][2] == "R":
                    print("Case 78 Found")
                    self.c.sequence(" B Di Fi R F")
                    cross_algorithm += " B Di Fi R F"
                # Case 7 and 8
                if white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][1] == "R":
                    print("Case 79 Found")
                    self.c.sequence("D")
                    cross_algorithm += " D"
                elif white_pieces[val][1] == (-1, -1, 0) and white_pieces[val][0][0] == "R":
                    print("Case 80 Found")
                    self.c.sequence("F Li Fi")
                    cross_algorithm += " F Li Fi"
                # Case 9 and 10
                if white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][1] == "R":
                    print("Case 81 Found")
                    print("No algorithm needed")
                elif white_pieces[val][1] == (0, -1, 1) and white_pieces[val][0][2] == "R":
                    print("Case 82 Found")
                    self.c.sequence("D Fi R F")
                    cross_algorithm += " D Fi R F"
                # Case 11  and 12
                if white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][0] == "R":
                    print("Case 83 Found")
                    self.c.sequence("Fi R F")
                    cross_algorithm += " Fi R F"
                elif white_pieces[val][1] == (1, -1, 0) and white_pieces[val][0][1] == "R":
                    print("Case 84 Found")
                    self.c.sequence("Di")
                    cross_algorithm += " Di"
                # Case 13 and 14
                if white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][1] == "R":
                    print("Case 85 Found")
                    self.c.sequence("D D")
                    cross_algorithm += " D D"
                elif white_pieces[val][1] == (0, -1, -1) and white_pieces[val][0][2] == "R":
                    print("Case 86 Found")
                    self.c.sequence("Di Fi R F")
                    cross_algorithm += " Di Fi R F"
                # Case 15 and 16
                if white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][0] == "R":
                    print("Case 87 Found")
                    self.c.sequence("Ri Fi R F")
                    cross_algorithm += " Ri Fi R F"
                elif white_pieces[val][1] == (1, 0, 1) and white_pieces[val][0][2] == "R":
                    print("Case 88 Found")
                    self.c.sequence("Ri Di")
                    cross_algorithm += " Ri Di"
                # Case 17 and 18
                if white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][1] == "R":
                    print("Case 89 Found")
                    self.c.sequence("F F U F F")
                    cross_algorithm += " F F U F F"
                elif white_pieces[val][1] == (1, 1, 0) and white_pieces[val][0][0] == "R":
                    print("Case 90 Found")
                    self.c.sequence("Fi Ri F")
                    cross_algorithm += " Fi Ri F"
                # Case 19 and 20
                if white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][0] == "R":
                    print("Case 91 Found")
                    self.c.sequence("Bi D D")
                    cross_algorithm += " Bi D D"
                elif white_pieces[val][1] == (1, 0, -1) and white_pieces[val][0][2] == "R":
                    print("Case 92 Found")
                    self.c.sequence("Bi Di Fi R F")
                    cross_algorithm += " Bi Di Fi R F"
                # Case 21 and 22
                if white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][1] == "R":
                    print("Case 93 Found")
                    self.c.sequence("U U B B D D")
                    cross_algorithm += " U U B B D D"
                elif white_pieces[val][1] == (0, 1, 1) and white_pieces[val][0][2] == "R":
                    print("Case 94 Found")
                    self.c.sequence("U F F Ui F F")
                    cross_algorithm += " U F F Ui F F"
                # Case 23 and 24 FINAL ONES IM SO HAPPY
                if white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][2] == "R":
                    print("Case 95 Found")
                    self.c.sequence("B B Di Fi R F")
                    cross_algorithm += " B B Di Fi R F"
                elif white_pieces[val][1] == (0, 1, -1) and white_pieces[val][0][1] == "R":
                    print("Case 96 Found")
                    self.c.sequence("B B D D")
                    cross_algorithm += " B B D D"

            print("Cross White / RED = " + cross_algorithm)
            white_pieces = self.findWhiteEdge()
        print(white_pieces)
        print("White Cross Solved")
        print("White Cross Algorithm = ", cross_algorithm)
        return cross_algorithm
    # Commented

    def solveWhiteCorner(self):
        whiteCorners = self.findWhiteCorner()
        whiteCornersAlgorithm = ""

        # Declaring the correct arrangements for each piece.
        correct_arrangements = [['B', 'O', 'W'], ['B', 'R', 'W'], ['G', 'O', 'W'], ['G', 'R', 'W']]

        try:
            # Loop through all white corners
            for val in range(len(whiteCorners)):
                # Checking if piece is on bottom row, else skip onto next step
                # Check if piece is in the correct location
                if whiteCorners[val][1] == (1, 1, 1):
                    # Check if piece is in the correct orientation
                    if whiteCorners[val][0] == correct_arrangements[0]:
                        # If piece is in the correct place and orientation - leave it.
                        print(correct_arrangements[val], " piece In Correct Location")
                    else:
                        # If it is in a corner, but it is the wrong piece, remove it from the corner.
                        self.c.sequence("R B Ri Bi")
                        whiteCornersAlgorithm += " R B Ri Bi"
                        whiteCorners = self.findWhiteCorner()
                if whiteCorners[val][1] == (1, -1, 1):
                    if whiteCorners[val][0] == correct_arrangements[1]:
                        print(correct_arrangements[val], " piece In Correct Location")
                    else:
                        self.c.sequence("Ri Bi R B")
                        whiteCornersAlgorithm += " Ri Bi R B"
                        whiteCorners = self.findWhiteCorner()
                if whiteCorners[val][1] == (-1, 1, 1):
                    if whiteCorners[val][0] == correct_arrangements[2]:
                        print(correct_arrangements[val], " piece In Correct Location")
                    else:
                        self.c.sequence("Li Bi L B")
                        whiteCornersAlgorithm += " Li Bi L B"
                        whiteCorners = self.findWhiteCorner()
                if whiteCorners[val][1] == (-1, -1, 1):
                    if whiteCorners[val][0] == correct_arrangements[3]:
                        print(correct_arrangements[val], " piece In Correct Location")
                    else:
                        self.c.sequence("L B Li Bi")
                        whiteCornersAlgorithm += " L B Li Bi"
                        whiteCorners = self.findWhiteCorner()

                # Second Section
                # The piece we are looking for, is not in a corner any more - so move above desired location.
                # If piece being investigated last vector position = -1, it is in the correct position. (Top row)
                if whiteCorners[val][1][2] == -1:
                    # Check if piece is the white orange and blue corner
                    if set(whiteCorners[val][0]).issubset(['W', 'O', 'B']):
                        # While it is not above the desired location
                        while whiteCorners[val][1] != (1, 1, -1):
                            self.c.sequence("B")
                            whiteCornersAlgorithm += " B"
                            whiteCorners = self.findWhiteCorner()
                            # Move around, one move at a time until it is above the desired location.
                            if whiteCorners[val][1] == (1, 1, -1):
                                whiteCorners = self.findWhiteCorner()
                        # When in the correct location, perform algorithm "R B Ri Bi" until the corner piece is inserted
                        while whiteCorners[val][1] != (1, 1, 1) or whiteCorners[val][0] != ['B', 'O', 'W']:
                            self.c.sequence("R B Ri Bi")
                            whiteCornersAlgorithm += " R B Ri Bi"
                            whiteCorners = self.findWhiteCorner()
                    # Repeat this for every piece
                    if set(whiteCorners[val][0]).issubset(['W', 'R', 'B']):
                        while whiteCorners[val][1] != (1, -1, -1):
                            self.c.sequence("B")
                            whiteCornersAlgorithm += " B"
                            whiteCorners = self.findWhiteCorner()
                            if whiteCorners[val][1] == (1, -1, -1):
                                whiteCorners = self.findWhiteCorner()
                        while whiteCorners[val][1] != (1, -1, 1) or whiteCorners[val][0] != ['B', 'R', 'W']:
                            self.c.sequence("D B Di Bi")
                            whiteCornersAlgorithm += " D B Di Bi"
                            whiteCorners = self.findWhiteCorner()
                    if set(whiteCorners[val][0]).issubset(['W', 'G', 'O']):
                        while whiteCorners[val][1] != (-1, 1, -1):
                            self.c.sequence("B")
                            whiteCornersAlgorithm += " B"
                            whiteCorners = self.findWhiteCorner()
                            if whiteCorners[val][1] == (-1, 1, -1):
                                whiteCorners = self.findWhiteCorner()
                        while whiteCorners[val][1] != (-1, 1, 1) or whiteCorners[val][0] != ['G', 'O', 'W']:
                            self.c.sequence("Li Bi L B")
                            whiteCornersAlgorithm += " Li Bi L B"
                            whiteCorners = self.findWhiteCorner()
                    if set(whiteCorners[val][0]).issubset(['W', 'G', 'R']):
                        while whiteCorners[val][1] != (-1, -1, -1):
                            self.c.sequence("B")
                            whiteCornersAlgorithm += " B"
                            whiteCorners = self.findWhiteCorner()
                            if whiteCorners[val][1] == (-1, -1, -1):
                                whiteCorners = self.findWhiteCorner()
                        while whiteCorners[val][1] != (-1, -1, 1) or whiteCorners[val][0] != ['G', 'R', 'W']:
                            self.c.sequence("L B Li Bi")
                            whiteCornersAlgorithm += " L B Li Bi"
                            whiteCorners = self.findWhiteCorner()
            print("White Corner Solved")
            print("White Corner Algorithm = " + whiteCornersAlgorithm)
            return whiteCornersAlgorithm
        except:
            return None
    # Commenting
    def solveSecondLayer(self):
        second_layer_algorithm = " "
        whiteCorners = self.findWhiteCorner()
        order = ["First - Blue/White/Orange", "Second - Blue/White/Red", "Third - Green/Orange/White",
                 "Fourth - Green/Red/White"]
        try:
            for val in range(len(whiteCorners)):
                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                # Third index being 0 means they sit in the same level... middle layer...
                if currentEdgePiece[0][1] == (1, 1, 0):
                    # Check if in correct place...
                    if set(currentEdgePiece[0][0]).issubset(['B', 'O', None]) and currentEdgePiece[0][0] == ["B", "O",
                                                                                                             None]:
                        print("piece in correct location")
                    else:
                        self.c.sequence("R B Ri Bi Ui Bi U B")
                        currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        second_layer_algorithm += " R B Ri Bi Ui Bi U B"
                if currentEdgePiece[0][1] == (1, -1, 0):
                    if set(currentEdgePiece[0][0]).issubset(['B', 'R', None]) and currentEdgePiece[0][0] == ['B', 'R',
                                                                                                             None]:
                        print("piece in correct location")
                    else:
                        self.c.sequence("D B Di Bi Ri Bi R B")
                        currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        second_layer_algorithm += " D B Di Bi Ri Bi R B"
                if currentEdgePiece[0][1] == (-1, 1, 0):
                    if set(currentEdgePiece[0][0]).issubset(['G', 'O', None]) and currentEdgePiece[0][0] == ['G', 'O',
                                                                                                             None]:
                        print("piece in correct location")
                    else:
                        self.c.sequence("Li Bi L B U B Ui Bi")
                        currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        second_layer_algorithm += " Li Bi L B U B Ui Bi"
                if currentEdgePiece[0][1] == (-1, -1, 0):
                    if set(currentEdgePiece[0][0]).issubset(['G', 'R', None]) and currentEdgePiece[0][0] == ['G', 'R',
                                                                                                             None]:
                        print("piece in correct location")
                    else:
                        self.c.sequence("L B Li Bi Di Bi D B")
                        currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        second_layer_algorithm += " L B Li Bi Di Bi D B"
                if currentEdgePiece[0][1][2] == -1:
                    # Under the assumption that the white corner piece is in the correct place
                    if set(currentEdgePiece[0][0]).issubset(['B', 'O', None]):
                        if currentEdgePiece[0][0] == ["B", None, "O"] or currentEdgePiece[0][0] == [None, "B", "O"]:
                            # Target needs to be (0,-1,-1)
                            while currentEdgePiece[0][1] != (0, -1, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (0, -1, -1):
                                self.c.sequence("Ui Bi U B R B Ri Bi")
                                second_layer_algorithm += " Ui Bi U B R B Ri Bi"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        if currentEdgePiece[0][0] == [None, "O", "B"] or currentEdgePiece[0][0] == ["O", None, "B"]:
                            while currentEdgePiece[0][1] != (-1, 0, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (-1, 0, -1):
                                self.c.sequence("R B Ri Bi Ui Bi U B")
                                second_layer_algorithm += " R B Ri Bi Ui Bi U B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                    if set(currentEdgePiece[0][0]).issubset(['B', 'R', None]):
                        if currentEdgePiece[0][0] == ["B", None, "R"] or currentEdgePiece[0][0] == [None, "B", "R"]:
                            # Target needs to be (0,1,-1)
                            while currentEdgePiece[0][1] != (0, 1, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (0, 1, -1):
                                self.c.sequence("D B Di Bi Ri Bi R B")
                                second_layer_algorithm += " D B Di Bi Ri Bi R B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        if currentEdgePiece[0][0] == [None, "R", "B"] or currentEdgePiece[0][0] == ["R", None, "B"]:
                            while currentEdgePiece[0][1] != (-1, 0, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (-1, 0, -1):
                                self.c.sequence("Ri Bi R B D B Di Bi")
                                second_layer_algorithm += " Ri Bi R B D B Di Bi"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                    if set(currentEdgePiece[0][0]).issubset(['G', 'O', None]):
                        if currentEdgePiece[0][0] == ["O", None, "G"] or currentEdgePiece[0][0] == [None, "O", "G"]:
                            # Target needs to be (1,0,-1)
                            while currentEdgePiece[0][1] != (1, 0, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (1, 0, -1):
                                self.c.sequence("Li Bi L B U B Ui B")
                                second_layer_algorithm += " Li Bi L B U B Ui B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        if currentEdgePiece[0][0] == [None, "G", "O"] or currentEdgePiece[0][0] == ["G", None, "O"]:
                            # Target needs to be (1,0,-1)
                            while currentEdgePiece[0][1] != (0, -1, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (0, -1, -1):
                                self.c.sequence("U B Ui Bi Li Bi L B")
                                second_layer_algorithm += " U B Ui Bi Li Bi L B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                    if set(currentEdgePiece[0][0]).issubset(['G', 'R', None]):
                        if currentEdgePiece[0][0] == ["R", None, "G"] or currentEdgePiece[0][0] == [None, "R", "G"]:
                            # Target  = (1,0,-1)
                            while currentEdgePiece[0][1] != (1, 0, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (1, 0, -1):
                                self.c.sequence("L B Li Bi Di Bi D B")
                                second_layer_algorithm += " L B Li Bi Di Bi D B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                        if currentEdgePiece[0][0] == [None, "G", "R"] or currentEdgePiece[0][0] == ["G", None, "R"]:
                            # Target Location = 0,1,-1
                            while currentEdgePiece[0][1] != (0, 1, -1):
                                self.c.sequence("B")
                                second_layer_algorithm += " B"
                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
                            if currentEdgePiece[0][1] == (0, 1, -1):
                                # c.sequence("D B Di Bi Ri Bi R B")
                                self.c.sequence("Di Bi D B L B Li Bi")
                                second_layer_algorithm += " Di Bi D B L B Li Bi"

                                currentEdgePiece = self.findMiddleLayerPiece(whiteCorners[val][0])
            print("Second Layer Solved")
            print("Second Layer Algorithm = " + second_layer_algorithm)
            return second_layer_algorithm
        except:
            print("An error occured on second layer (F2L)")
            return None

    def solveYellowCross(self):
        # If Y == 2nd index - yellow is pointing up

        yellow_cross_algorithm = ""
        # Check If Cross Already Exists:
        yellowCrossSolved = [
            self.c.get_piece(0, 1, -1).colors[2] == "Y",
            self.c.get_piece(1, 0, -1).colors[2] == "Y",
            self.c.get_piece(0, -1, -1).colors[2] == "Y",
            self.c.get_piece(-1, 0, -1).colors[2] == "Y"]

        # Conditions For First look OLL LINE
        line_condition_one = [
            self.c.get_piece(0, 1, -1).colors[2] == "Y",
            self.c.get_piece(0, 0, -1).colors[2] == "Y",
            self.c.get_piece(0, -1, -1).colors[2] == "Y"
        ]

        line_condition_two = [
            self.c.get_piece(1, 0, -1).colors[2] == "Y",
            self.c.get_piece(0, 0, -1).colors[2] == "Y",
            self.c.get_piece(-1, 0, -1).colors[2] == "Y"
        ]
        # Conditions For First Look OLL L
        # L At Top Right
        l_condition_one = [
            self.c.get_piece(0, 1, -1).colors[2] == "Y",
            self.c.get_piece(0, 0, -1).colors[2] == "Y",
            self.c.get_piece(-1, 0, -1).colors[2] == "Y"]

        # L At Top Left # This is the target
        l_condition_two = [
            self.c.get_piece(0, 1, -1).colors[2] == "Y",
            self.c.get_piece(0, 0, -1).colors[2] == "Y",
            self.c.get_piece(1, 0, -1).colors[2] == "Y"]

        # L at bottom left
        l_condition_three = [
            self.c.get_piece(0, -1, -1).colors[2] == "Y",
            self.c.get_piece(0, 0, -1).colors[2] == "Y",
            self.c.get_piece(1, 0, -1).colors[2] == "Y"]

        # L at bottom Right
        l_condition_four = [
            self.c.get_piece(0, -1, -1).colors[2] == "Y",
            self.c.get_piece(0, 0, -1).colors[2] == "Y",
            self.c.get_piece(-1, 0, -1).colors[2] == "Y"]

        try:
            if all(yellowCrossSolved):
                print("The Yellow Cross Is Already Solved...")
            # Conditions For Line Found
            elif all(line_condition_one) or all(line_condition_two):
                if line_condition_two == [True, True, True]:
                    algorithm = "F R U Ri Ui Fi"
                    newAlgo = self.convertAlgo(algorithm)
                    yellow_cross_algorithm += newAlgo
                    self.c.sequence(newAlgo)
                elif line_condition_one == [True, True, True]:
                    if line_condition_one == [True, True, True]:
                        self.c.sequence("B")
                        yellow_cross_algorithm += " B"
                        algorithm = "F R U Ri Ui Fi"
                        newAlgo = self.convertAlgo(algorithm)
                        yellow_cross_algorithm += newAlgo
                        self.c.sequence(newAlgo)
            # Conditions for L found -
            elif all(l_condition_one) or all(l_condition_two) or all(l_condition_three) or all(
                    l_condition_four) and not all(yellowCrossSolved):
                if l_condition_two == [True, True, True]:
                    self.c.sequence("D B L Bi Li Di")
                    yellow_cross_algorithm += " D B L Bi Li Di"
                elif not l_condition_two == [True, True, True]:
                    if l_condition_one == [True, True, True]:
                        self.c.sequence("Bi D B L Bi Li Di")
                        yellow_cross_algorithm += " Bi D B L Bi Li Di"
                    elif l_condition_three == [True, True, True]:
                        self.c.sequence("B D B L Bi Li Di")
                        yellow_cross_algorithm += " B D B L Bi Li Di"
                    elif l_condition_four == [True, True, True]:
                        self.c.sequence("B B D B L Bi Li Di")
                        yellow_cross_algorithm += " B B D B L Bi Li Di"
            # Dot Scenorio
            elif (not all(l_condition_one) and not all(l_condition_two) and not all(l_condition_three) and not all(
                    l_condition_four)
                  and not all(yellowCrossSolved)
                  and not all(line_condition_two) and not all(line_condition_one)):
                self.c.sequence("U R B Ri Bi Ui")
                self.c.sequence("D B L Bi Li Di")
                yellow_cross_algorithm += " U R B Ri Bi Ui D B L Bi Li Di"
            print("Yellow Cross Solved")
            print("Yellow Cross Algorithm = " + yellow_cross_algorithm)
            return yellow_cross_algorithm
        except:
            return None

    def orientLastLayer(self):
        # Cases
        print(self.c)
        oll_algorithm = " "
        # # Check Full Yellow Face
        if self.c.is_solved():
            return oll_algorithm
        else:
            itter = 0
            for i in range(1, 5):
                itter += 1
                print("itter = " + str(itter))
                self.c.sequence("B")
                oll_algorithm += " B"
                # Anti Sune Case...
                if (self.c.get_piece(-1, 1, -1).colors[1] == "Y" and
                        self.c.get_piece(-1, -1, -1).colors[0] == "Y" and
                        self.c.get_piece(1, -1, -1).colors[1] == "Y" and
                        self.c.get_piece(1, 1, -1).colors[2] == "Y" and
                        self.c.get_piece(0, 1, -1).colors[2] == "Y" and
                        self.c.get_piece(1, 0, -1).colors[2] == "Y" and
                        self.c.get_piece(0, 0, -1).colors[2] == "Y" and
                        self.c.get_piece(-1, 0, -1).colors[2] == "Y" and
                        self.c.get_piece(0, -1, -1).colors[2] == "Y"):
                    self.c.sequence("Li Bi L Bi Li B B L")
                    oll_algorithm += " Li Bi L Bi Li B B L"
                    break
                # Sune Case...
                elif (self.c.get_piece(1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(-1, -1, -1).colors[1] == "Y" and
                      self.c.get_piece(1, -1, -1).colors[0] == "Y" and
                      self.c.get_piece(-1, 1, -1).colors[2] == "Y"):
                    self.c.sequence("R B Ri B R B B Ri")
                    oll_algorithm += " R B Ri B R B B Ri"
                    break
                # Headlights Case
                elif (self.c.get_piece(-1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(1, -1, -1).colors[2] == "Y" and
                      self.c.get_piece(-1, -1, -1).colors[2] == "Y"):
                    self.c.sequence("R R F Ri B B R Fi Ri B B Ri")
                    oll_algorithm += " R R F Ri B B R Fi Ri B B Ri"
                    break
                # H Case
                elif (self.c.get_piece(1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(-1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(-1, -1, -1).colors[1] == "Y" and
                      self.c.get_piece(1, -1, -1).colors[1] == "Y"):
                    self.c.sequence("U R B Ri Bi R B Ri Bi R B Ri Bi Ui")
                    oll_algorithm += " U R B Ri Bi R B Ri Bi R B Ri Bi Ui"
                    break
                # Pi Case
                elif (self.c.get_piece(1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(1, -1, -1).colors[1] == "Y" and
                      self.c.get_piece(-1, 1, -1).colors[0] == "Y" and
                      self.c.get_piece(-1, -1, -1).colors[0] == "Y"):
                    self.c.sequence("R B B Ri Ri Bi R R Bi Ri Ri B B R")
                    oll_algorithm += " R B B Ri Ri Bi R R Bi Ri Ri B B R"
                    break
                # T Case
                elif (self.c.get_piece(1, 1, -1).colors[2] == "Y" and
                      self.c.get_piece(1, -1, -1).colors[2] == "Y" and
                      self.c.get_piece(-1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(-1, -1, -1).colors[1] == "Y"):
                    self.c.sequence("L U Ri Ui Li U R Ui")
                    oll_algorithm += " L U Ri Ui Li U R Ui"
                    break
                # Bow-Tie Case
                elif (self.c.get_piece(-1, 1, -1).colors[1] == "Y" and
                      self.c.get_piece(1, -1, -1).colors[0] == "Y" and
                      self.c.get_piece(1, 1, -1).colors[2] == "Y" and
                      self.c.get_piece(-1, -1, -1).colors[2] == "Y"):
                    self.c.sequence("Ri U R Di Ri Ui R D")
                    oll_algorithm += " Ri U R Di Ri Ui R D"
                    break
                # OLL Already Solved (Yellow Face comeple)
                elif (self.c.get_piece(1, 1, -1).colors[2] and self.c.get_piece(0, 1, -1).colors[2] and
                    self.c.get_piece(-1, 1, -1).colors[2] and self.c.get_piece(1, 0, -1).colors[2] and
                    self.c.get_piece(0, 0, -1).colors[2] and self.c.get_piece(-1, 0, -1).colors[2] and
                    self.c.get_piece(1, -1, -1).colors[2] and self.c.get_piece(0, -1, -1).colors[2] and
                    self.c.get_piece(-1, -1, -1).colors[2]) == "Y":
                    oll_algorithm += ""
                else:
                    if itter == 4:
                        print("We couldn't find any cases....")
                        return None
            print("OLL Solved")
            print("OLL Algorithm = " + oll_algorithm)
            return oll_algorithm

    def solveFinalCorners(self):
        final_corner_algorithm = ""
        if self.c.is_solved():
            return final_corner_algorithm
        else:
            # First check if all corner's match each other:
            if (self.c.get_piece(-1, 1, -1).colors[1] == self.c.get_piece(1, 1, -1).colors[1] and
                    self.c.get_piece(1, 1, -1).colors[0] == self.c.get_piece(1, -1, -1).colors[0] and
                    self.c.get_piece(1, -1, -1).colors[1] == self.c.get_piece(-1, -1, -1).colors[1] and
                    self.c.get_piece(-1, 1, -1).colors[0] == self.c.get_piece(-1, -1, -1).colors[0]):
                print("")
            elif (self.c.get_piece(-1, 1, -1).colors[1] != self.c.get_piece(1, 1, -1).colors[1] and
                  self.c.get_piece(1, 1, -1).colors[0] != self.c.get_piece(1, -1, -1).colors[0] and
                  self.c.get_piece(1, -1, -1).colors[1] != self.c.get_piece(-1, -1, -1).colors[1] and
                  self.c.get_piece(-1, 1, -1).colors[0] != self.c.get_piece(-1, -1, -1).colors[0]):
                self.c.sequence("U R Bi Ri Bi R B Ri Ui R B Ri Bi Ri U R Ui")
                final_corner_algorithm += " U R Bi Ri Bi R B Ri Ui R B Ri Bi Ri U R Ui"
            else:
                if self.c.get_piece(-1, 1, -1).colors[1] == self.c.get_piece(1, 1, -1).colors[1]:
                    self.c.sequence("B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
                    final_corner_algorithm += " B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
                elif self.c.get_piece(1, 1, -1).colors[0] == self.c.get_piece(1, -1, -1).colors[0]:
                    self.c.sequence("B B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
                    final_corner_algorithm += " B B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
                elif self.c.get_piece(1, -1, -1).colors[1] == self.c.get_piece(-1, -1, -1).colors[1]:
                    self.c.sequence("Bi R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
                    final_corner_algorithm += " Bi R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
                elif self.c.get_piece(-1, 1, -1).colors[0] == self.c.get_piece(-1, -1, -1).colors[0]:
                    self.c.sequence("R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui")
                    final_corner_algorithm += " R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui"
                else:
                    print("No Cases Found..")
                    return None
            print("Final Corners Solved")
            print("Final Corners Algorithm = " + final_corner_algorithm)
            return final_corner_algorithm

    def solveFinalEdge(self):
        print(self.c)
        solved_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
        final_edge_algorithm = " "
        if self.c == solved_cube:
            print("Cube Is Already Solved! (Skip Stage 7)")
            return final_edge_algorithm
        # First Check is to check if any entire side matches (corner, edge, corner)
        else:
            # check all values on yellow face == yellow
            if (self.c.get_piece(1, 1, -1).colors[2] == "Y" and
                    self.c.get_piece(0, 1, -1).colors[2] == "Y" and
                    self.c.get_piece(-1, 1, -1).colors[2] == "Y" and
                    self.c.get_piece(1, 0, -1).colors[2] == "Y" and
                    self.c.get_piece(0, 0, -1).colors[2] == "Y" and
                    self.c.get_piece(-1, 0, -1).colors[2] == "Y" and
                    self.c.get_piece(1, -1, -1).colors[2] == "Y" and
                    self.c.get_piece(0, -1, -1).colors[2] == "Y" and
                    self.c.get_piece(-1, -1, -1).colors[2] == "Y"):
                print("All good")
            else:
                return None

            if (self.c.get_piece(-1, 1, -1).colors[1] == self.c.get_piece(1, 1, -1).colors[1] ==
                    self.c.get_piece(0, 1, -1).colors[
                        1] == self.c.get_piece(0, 1, -1).colors[1] and
                    self.c.get_piece(1, 1, -1).colors[0] == self.c.get_piece(1, -1, -1).colors[0] ==
                    self.c.get_piece(1, 0, -1).colors[
                        0] == self.c.get_piece(1, 0, -1).colors[0] and
                    self.c.get_piece(1, -1, -1).colors[1] == self.c.get_piece(-1, -1, -1).colors[1] ==
                    self.c.get_piece(0, -1, -1).colors[1] == self.c.get_piece(0, -1, -1).colors[1] and
                    self.c.get_piece(-1, 1, -1).colors[0] == self.c.get_piece(-1, 0, -1).colors[0] ==
                    self.c.get_piece(-1, -1, -1).colors[0] == self.c.get_piece(-1, -1, -1).colors[0]):

                while self.c.is_solved == False:
                    self.c.sequence("B")
                    final_edge_algorithm += " B"
                return final_edge_algorithm
            # Case For there being a line...
            if (self.c.get_piece(-1, 1, -1).colors[1] == self.c.get_piece(1, 1, -1).colors[1] ==
                    self.c.get_piece(0, 1, -1).colors[
                        1] == self.c.get_piece(0, 1, -1).colors[1] or
                    self.c.get_piece(1, 1, -1).colors[0] == self.c.get_piece(1, -1, -1).colors[0] ==
                    self.c.get_piece(1, 0, -1).colors[
                        0] == self.c.get_piece(1, 0, -1).colors[0] or
                    self.c.get_piece(1, -1, -1).colors[1] == self.c.get_piece(-1, -1, -1).colors[1] ==
                    self.c.get_piece(0, -1, -1).colors[1] == self.c.get_piece(0, -1, -1).colors[1] or
                    self.c.get_piece(-1, 1, -1).colors[0] == self.c.get_piece(-1, 0, -1).colors[0] ==
                    self.c.get_piece(-1, -1, -1).colors[0] == self.c.get_piece(-1, -1, -1).colors[0]):
                if self.c.get_piece(-1, 1, -1).colors[1] == self.c.get_piece(1, 1, -1).colors[1] == \
                        self.c.get_piece(0, 1, -1).colors[
                            1] == self.c.get_piece(0, 1, -1).colors[1]:
                    self.c.sequence("B B")
                    final_edge_algorithm += " B B"
                if self.c.get_piece(1, 1, -1).colors[0] == self.c.get_piece(1, -1, -1).colors[0] == \
                        self.c.get_piece(1, 0, -1).colors[
                            0] == self.c.get_piece(1, 0, -1).colors[0]:
                    self.c.sequence("Bi")
                    final_edge_algorithm += " Bi"
                if self.c.get_piece(1, -1, -1).colors[1] == self.c.get_piece(-1, -1, -1).colors[1] == \
                        self.c.get_piece(0, -1, -1).colors[1] == self.c.get_piece(0, -1, -1).colors[1]:
                    print("Line on Red side (Good)")
                if self.c.get_piece(-1, 1, -1).colors[0] == self.c.get_piece(-1, 0, -1).colors[0] == \
                        self.c.get_piece(-1, -1, -1).colors[0] == self.c.get_piece(-1, -1, -1).colors[0]:
                    self.c.sequence("B")
                    final_edge_algorithm += " B"
                # Now line is on correct side
                # First Case Ub Perm (R  F  Ui  Bi   D  U   Di  R  B  B   Di  B  L  R )
                if (self.c.get_piece(1, 0, -1).colors[0] == self.c.get_piece(1, 1, -1).colors[1] and
                        self.c.get_piece(0, 1, -1).colors[1] == self.c.get_piece(-1, 1, -1).colors[0] and
                        self.c.get_piece(-1, 0, -1).colors[0] == self.c.get_piece(1, 1, -1).colors[0]):
                    self.c.sequence("Mi Mi Bi M Bi Bi Mi Bi Mi Mi")
                    final_edge_algorithm += " Mi Mi Bi M Bi Bi Mi Bi Mi Mi"
                    while self.c.is_solved() == False:
                        self.c.sequence("B")
                        final_edge_algorithm += " B"
                else:
                    self.c.sequence("Mi Mi B M B B Mi B Mi Mi")
                    final_edge_algorithm += " Mi Mi B M B B Mi B Mi Mi"
                    while self.c.is_solved() == False:
                        self.c.sequence("B")
                        final_edge_algorithm += " B"
            # No Line Found
            else:
                print("no lINE found")
                while self.c.get_piece(-1, 1, -1).colors[1] != "O":
                    self.c.sequence("B")
                    final_edge_algorithm += " B"
                if (self.c.get_piece(0, 1, -1).colors[1] == self.c.get_piece(0, -1, 0).colors[1] and
                        self.c.get_piece(0, -1, -1).colors[1] == self.c.get_piece(0, 1, 0).colors[1] and
                        self.c.get_piece(-1, 0, -1).colors[0] == self.c.get_piece(1, 0, 0).colors[0] and
                        self.c.get_piece(1, 0, -1).colors[0] == self.c.get_piece(-1, 0, 0).colors[0]):
                    self.c.sequence("M M Bi M M B B M M Bi M M")
                    final_edge_algorithm += " M M Bi M M B B M M Bi M M"
                else:
                    self.c.sequence("Mi Bi M M Bi M M Bi Mi B B M M")
                    final_edge_algorithm += " Mi Bi M M Bi M M Bi Mi B B M M"
                    while self.c.get_piece(-1, 1, -1).colors[1] != self.c.get_piece(0, 1, -1).colors[1]:
                        self.c.sequence("Mi Bi M M Bi M M Bi Mi B B M M")
                        final_edge_algorithm += " Mi Bi M M Bi M M Bi Mi B B M M"
                    while self.c.is_solved() == False:
                        self.c.sequence("B")
                        final_edge_algorithm += " B"

            if self.c.is_solved():
                print("Final Edge Solved!")
                print("Final Edge Algorithm = " + final_edge_algorithm)
                return final_edge_algorithm
            else:
                return None

    def solveCube(self):
        if self.c.is_solved():
            print("Cube Already Solved")
        else:
            print("----------------------------------------------------------------------------------")
            stage_1 = self.solveWhiteCross()
            if stage_1 == None:
                print("Error Solving White Cross")
                return None
            print(self.c)
            print("----------------------------------------------------------------------------------")
            stage_2 = self.solveWhiteCorner()
            if stage_2 == None:
                print("Error White Corner")
                return None
            print(self.c)
            print("----------------------------------------------------------------------------------")
            stage_3 = self.solveSecondLayer()
            if stage_3 == None:
                print("Error Solving F2L")
                return None
            print(self.c)
            print("----------------------------------------------------------------------------------")
            stage_4 = self.solveYellowCross()
            if stage_4 == None:
                print("Error Solving Yellow Cross")
                return None
            print(self.c)
            print("----------------------------------------------------------------------------------")
            print("OLL")
            stage_5 = self.orientLastLayer()
            if stage_5 == None:
                print("Error Solving OLL")
                return None
            print(self.c)

            print("----------------------------------------------------------------------------------")
            stage_6 = self.solveFinalCorners()
            print(self.c)
            if stage_6 == None:
                print("Error Solving Final Corner")
                return None
            print("----------------------------------------------------------------------------------")
            stage_7 = self.solveFinalEdge()
            if stage_7 == None:
                print("Error Solving Final Edge")
                return None
            print("----------------------------------------------------------------------------------")
            print(self.c)

            solve_list = [stage_1 , stage_2 , stage_3 , stage_4 , stage_5 , stage_6 , stage_7]
            return stage_1 + stage_2 + stage_3 + stage_4 + stage_5 + stage_6 + stage_7, solve_list

    def generateScramble(self):
        notation = [" R ", " U ", " F ", " L ", " B ", "  D ", " Ri ", " Ui ", " Fi ", " Li ", " Bi ", "  Di "]
        scramble = " "
        for i in range(1, 20):
            scramble += str(notation[random.randrange(0, 12)])
        return scramble

    def testSolver(self, testAmount):
        # Test the cube on x number of random scrambles
        cube_scrambles = []
        solve_amount = []
        scrambles_success = 0
        scrambles_failed = 0
        scrambles_failed_list = []
        for i in range(int(testAmount)):
            print("Test Number " + str(testAmount))
            new_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
            scramble = self.generateScramble()
            new_cube.sequence(scramble)
            self.c = new_cube
            self.solveCube()
            if self.c.is_solved():
                scrambles_success += 1
            else:
                scrambles_failed += 1
                scrambles_failed_list.append(scramble)
        cube_scrambles.append(scramble)
        print("Final Results of " + str(testAmount) + " random scrambles")
        print("Success = " + str(scrambles_success))
        print("Failed = " + str(scrambles_failed))
        print("Failed Scrambles = " + str(scrambles_failed_list))




new_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
S = SolveCube(new_cube)
S.testSolver(1)