# Rubiks-Cube-Solver

Rubiks Cube Solver Using OpenCV. 

# Please note:
This program was developed on macOS, and not tested on Windows. 

Ensure you have the following packages installed:

    pip install opencv-python
    pip install numpy
    pip install webcolors
    pip install rubik-cube
    pip install tk
    pip install macosx
    pip install pygame
    
# Testing The Scanner & Solver

Testing individual aspects of the program. 

You can still test and use the program, without the GUI.

If you want to test the features individually you can: 

    Test the solver:
    
    1). Open main.py
    
    2). Un-comment test_solver()
        
    3). Where it says "Test Your Cube Here", enter your cube in the following format: 
    
    (A face is represented by the center piece on that particular face, being a specific colour)

                   ----------------
                   | 0  | 1  | 2  |
                   ----------------
      WHITE FACE   | 3  | 4  | 5  |  < ORANGE FACE
               \   ----------------
                \  | 6  | 7  | 8  |
                 \ ----------------
    -------------------------------------------------------------
    | 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
    -------------------------------------------------------------
    | 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 | < YELLOW FACE
    -------------------------------------------------------------
    | 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
    -------------------------------------------------------------
         /\        ----------------      /\
     GREEN FACE    | 45 | 46 | 47 |   BLUE FACE
                   ----------------
                   | 48 | 49 | 50 |
                   ----------------
                   | 51 | 52 | 53 |
                   ----------------
                          /\
                       RED FACE
                       

    "OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR" is an example of a solved cube in this format.
    
    4). Run main.py with adjusted code


Now for testing the Scanner: 

    Please note, lighting conditions may affect results. 
    Use in a well lit room, with warm lighting. 
    
    Testing the Scanner:
    
    1). Open main.py
    
    2). Un-comment test_scanner()
    
    3). Run main.py
    
    4). Have a Rubik's cube ready, and follow on-screen instructions.  

# Project Directory:
The project directory is organised as the following: 

Full File Structure Available Here:

https://stummuac-my.sharepoint.com/:f:/g/personal/18006190_stu_mmu_ac_uk/El_RWux9DYZEgaYnKTOlnG8B5nsDj9YbB17rCD-vvNJuNQ?e=C4C2Jy


       root
         - Development
           -- (Contains Files showing development of project)
         - Images
           -- (Contains Images used in project)
         - SoundEffects
           --- (Contans Sound Effects used in project)
         - Text
           -- (Contains The Text used in project)
           
         Main Documents Used:
         - CubeScanner.py
         - main.py
         - Solver.py
         - README.md
         - main_gui.py

# About the Program:
- Average Time (seconds) for solver to solve any given cube: 0.03 seconds

- Average Move Count Per Solve: 158 moves

- Average Time for Scanner to process cube face: 0.019 seconds



