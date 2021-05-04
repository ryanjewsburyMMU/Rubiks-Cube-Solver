# Ryan Jewsbury Image Processing Rubik's Cube Solver
from CubeScanner import CubeScanner
from Solver import SolveCube
from rubik.cube import Cube


def main():
    print("Rubik's Cube Solver By Ryan Jewsbury (Python 3.8.2, Solver 1.0)")
    import main_gui


def test_scanner():
    print("Testing Scanner")
    Scanner = CubeScanner()
    Scanner.scan()


def test_solver():
    # Edit your cube here:
    test_cube = Cube("YRGGOGYYYBWBRORGYOYBOOGOBWBYBOGYWGGRWWOWRWORRBBGRRYWWB")  # Refer to README
    print(test_cube, "\n")
    S = SolveCube(test_cube)
    algorithm = S.solveCube()
    stages = ["White Cross", "White Corners", "Second Layer", "Yellow Cross", "OLL", "Yellow Corners", "Yellow Edge"]
    for i in range(len(algorithm[1])):
        print(stages[i] + ": " + str(algorithm[1][i]))
        if i == 6:
            print("\n")
    print(test_cube)

    # Bulk Testing - Tests on test_amount number of random cubes:
    # test_amount = 100
    # S.testSolver(test_amount)


# test_solver()

test_scanner()

# main()
