from rubik.cube import Cube
from tkinter import *
from tkinter import messagebox


# import RPi.GPIO as GPIO
from datetime import *
import time

root = Tk()  # Draws the window



# These next lines define size, position and title of tkinter window
root.geometry('1400x740+10+10')  # width x height + xpos + ypos
root.title("Cube Solver")

# Frame and its contents
mainFrame = Frame(root, width=200, height=200)
mainFrame.grid(row=0, column=0, padx=10, pady=2)


cubeCanvas = Canvas(mainFrame, width=1000, height=720, bg='black')
cubeCanvas.grid(row=0, column=0, padx=0, pady=2)




c = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
c.sequence("Ri  F  F  Li   D  Bi   D  Li  L  L  L  Fi  R  Fi")
# Scramble
# Ri  F  F  Li   D  Bi   D  Li  L  L  L  Fi  R  Fi
# Solve
#  R Fi U F B B U U B B B R B Ri Bi B D B Di Bi D B Di Bi D B Di Bi Li Bi L B Li Bi L B Li Bi L B Li Bi L B Li Bi L B  L B Li Bi Di Bi D B B Ui Bi U B R B Ri Bi B B Ri Bi R B D B Di Bi B B B Li Bi L B U B Ui B B B L B Li Bi Di Bi D B B U R B Ri Bi Ui  B B R B B Ri Ri Bi R R Bi Ri Ri B B R B B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui  Mi Mi Bi M Bi Bi Mi Bi Mi Mi B B

def makeMove(move):
    print("Making move")
    c.sequence(move)
    updateCubeColours()

def performAlgorithm(algo):
    for move in algo.split():
        try:
            c.sequence(move)
            print(c)
            cubeCanvas.after(100, updateCubeColours())
            cubeCanvas.update_idletasks()
        except:
            print("Cannot Perform Move '" + move + "'")



# Converts Cubie To Colour for Digital Cube
def colourFromLetter(value):
    try:
        colors = {'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'W': 'White', 'Y': 'Yellow'}
        return colors[value]
    except:
        messagebox.showinfo("Say Hello", "Hello World")
        return None

def updateCubeColours():
    # Green Face (Layer 1)
    cubeCanvas.itemconfigure(green_00, fill=colourFromLetter(c.get_piece(-1,1,-1).colors[0]))
    cubeCanvas.itemconfigure(green_01, fill=colourFromLetter(c.get_piece(-1,1,0).colors[0]))
    cubeCanvas.itemconfigure(green_02, fill=colourFromLetter(c.get_piece(-1,1,1).colors[0]))
    # Green Face (Layer 2)
    cubeCanvas.itemconfigure(green_10, fill=colourFromLetter(c.get_piece(-1, 0, -1).colors[0]))
    cubeCanvas.itemconfigure(green_11, fill=colourFromLetter(c.get_piece(-1, 0, 0).colors[0]))
    cubeCanvas.itemconfigure(green_12, fill=colourFromLetter(c.get_piece(-1, 0, 1).colors[0]))
    # Green Face (Layer 3)
    cubeCanvas.itemconfigure(green_20, fill=colourFromLetter(c.get_piece(-1, -1, -1).colors[0]))
    cubeCanvas.itemconfigure(green_21, fill=colourFromLetter(c.get_piece(-1, -1, 0).colors[0]))
    cubeCanvas.itemconfigure(green_22, fill=colourFromLetter(c.get_piece(-1, -1, 1).colors[0]))

    # White Face (Layer 1)
    cubeCanvas.itemconfigure(white_00, fill=colourFromLetter(c.get_piece(-1,1,1).colors[2]))
    cubeCanvas.itemconfigure(white_01, fill=colourFromLetter(c.get_piece(0,1,1).colors[2]))
    cubeCanvas.itemconfigure(white_02, fill=colourFromLetter(c.get_piece(1,1,1).colors[2]))
    # White Face (Layer 2)
    cubeCanvas.itemconfigure(white_10, fill=colourFromLetter(c.get_piece(-1, 0, 1).colors[2]))
    cubeCanvas.itemconfigure(white_11, fill=colourFromLetter(c.get_piece(0, 0, 1).colors[2]))
    cubeCanvas.itemconfigure(white_12, fill=colourFromLetter(c.get_piece(1,0,1).colors[2]))
    # White Face (Layer 3)
    cubeCanvas.itemconfigure(white_20, fill=colourFromLetter(c.get_piece(-1, -1, 1).colors[2]))
    cubeCanvas.itemconfigure(white_21, fill=colourFromLetter(c.get_piece(0, -1, 1).colors[2]))
    cubeCanvas.itemconfigure(white_22, fill=colourFromLetter(c.get_piece(1, -1, 1).colors[2]))

    # Orange Face (Layer 1)
    cubeCanvas.itemconfigure(orange_00, fill=colourFromLetter(c.get_piece(-1,1,-1).colors[1]))
    cubeCanvas.itemconfigure(orange_01, fill=colourFromLetter(c.get_piece(0,1,-1).colors[1]))
    cubeCanvas.itemconfigure(orange_02, fill=colourFromLetter(c.get_piece(1,1,-1).colors[1]))
    # Orange Face (Layer 2)
    cubeCanvas.itemconfigure(orange_10, fill=colourFromLetter(c.get_piece(-1, 1, 0).colors[1]))
    cubeCanvas.itemconfigure(orange_11, fill=colourFromLetter(c.get_piece(0, 1, 0).colors[1]))
    cubeCanvas.itemconfigure(orange_12, fill=colourFromLetter(c.get_piece(1, 1, 0).colors[1]))
    # Orange Face (Layer 3)
    cubeCanvas.itemconfigure(orange_20, fill=colourFromLetter(c.get_piece(-1, 1, 1).colors[1]))
    cubeCanvas.itemconfigure(orange_21, fill=colourFromLetter(c.get_piece(0, 1, 1).colors[1]))
    cubeCanvas.itemconfigure(orange_22, fill=colourFromLetter(c.get_piece(1, 1, 1).colors[1]))

    # Red Face (Layer 1)
    cubeCanvas.itemconfigure(red_00, fill=colourFromLetter(c.get_piece(-1,-1,1).colors[1]))
    cubeCanvas.itemconfigure(red_01, fill=colourFromLetter(c.get_piece(0,-1,1).colors[1]))
    cubeCanvas.itemconfigure(red_02, fill=colourFromLetter(c.get_piece(1,-1,1).colors[1]))
    # Red Face (Layer 2)
    cubeCanvas.itemconfigure(red_10, fill=colourFromLetter(c.get_piece(-1, -1, 0).colors[1]))
    cubeCanvas.itemconfigure(red_11, fill=colourFromLetter(c.get_piece(0, -1, 0).colors[1]))
    cubeCanvas.itemconfigure(red_12, fill=colourFromLetter(c.get_piece(1, -1, 0).colors[1]))
    # Red Face (Layer 3)
    cubeCanvas.itemconfigure(red_20, fill=colourFromLetter(c.get_piece(-1, -1, -1).colors[1]))
    cubeCanvas.itemconfigure(red_21, fill=colourFromLetter(c.get_piece(0, -1, -1).colors[1]))
    cubeCanvas.itemconfigure(red_22, fill=colourFromLetter(c.get_piece(1, -1, -1).colors[1]))

    # Blue Face (Layer 1)
    cubeCanvas.itemconfigure(blue_00, fill=colourFromLetter(c.get_piece(1,1,1).colors[0]))
    cubeCanvas.itemconfigure(blue_01, fill=colourFromLetter(c.get_piece(1,1,0).colors[0]))
    cubeCanvas.itemconfigure(blue_02, fill=colourFromLetter(c.get_piece(1,1,-1).colors[0]))
    # Blue Face (Layer 2)
    cubeCanvas.itemconfigure(blue_10, fill=colourFromLetter(c.get_piece(1, 0, 1).colors[0]))
    cubeCanvas.itemconfigure(blue_11, fill=colourFromLetter(c.get_piece(1, 0, 0).colors[0]))
    cubeCanvas.itemconfigure(blue_12, fill=colourFromLetter(c.get_piece(1, 0, -1).colors[0]))
    # Blue Face (Layer 3)
    cubeCanvas.itemconfigure(blue_20, fill=colourFromLetter(c.get_piece(1,-1,1).colors[0]))
    cubeCanvas.itemconfigure(blue_21, fill=colourFromLetter(c.get_piece(1, -1, 0).colors[0]))
    cubeCanvas.itemconfigure(blue_22, fill=colourFromLetter(c.get_piece(1, -1, -1).colors[0]))

    # Yellow Face (Layer 1)
    cubeCanvas.itemconfigure(yellow_00, fill=colourFromLetter(c.get_piece(1,1,-1).colors[2]))
    cubeCanvas.itemconfigure(yellow_01, fill=colourFromLetter(c.get_piece(0,1,-1).colors[2]))
    cubeCanvas.itemconfigure(yellow_02, fill=colourFromLetter(c.get_piece(-1,1,-1).colors[2]))
    # Yellow Face (Layer 2)
    cubeCanvas.itemconfigure(yellow_10, fill=colourFromLetter(c.get_piece(1, 0, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_11, fill=colourFromLetter(c.get_piece(0, 0, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_12, fill=colourFromLetter(c.get_piece(-1, 0, -1).colors[2]))
    # Yellow Face (Layer 3)
    cubeCanvas.itemconfigure(yellow_20, fill=colourFromLetter(c.get_piece(1,-1,-1).colors[2]))
    cubeCanvas.itemconfigure(yellow_21, fill=colourFromLetter(c.get_piece(0, -1, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_22, fill=colourFromLetter(c.get_piece(-1, -1, -1).colors[2]))


# Green Face (Layer 1)
green_00 = cubeCanvas.create_rectangle(20, 240, 90, 310, width=0, fill='green')
green_01 = cubeCanvas.create_rectangle(100, 240, 170, 310, width=0, fill='green')
green_02 = cubeCanvas.create_rectangle(180, 240, 250, 310, width=0, fill='green')
# Green Face (Layer 2)
green_10 = cubeCanvas.create_rectangle(20, 320, 90, 390, width=0, fill='green')
green_11 = cubeCanvas.create_rectangle(100, 320, 170, 390, width=0, fill='green')
green_12 = cubeCanvas.create_rectangle(180, 320, 250, 390, width=0, fill='green')
# Green Face (Layer 3)
green_20 = cubeCanvas.create_rectangle(20, 400, 90, 470, width=0, fill='green')
green_21 = cubeCanvas.create_rectangle(100, 400, 170, 470, width=0, fill='green')
green_22 = cubeCanvas.create_rectangle(180, 400, 250, 470, width=0, fill='green')

# White Face (Layer 1)
white_00 = cubeCanvas.create_rectangle(260, 240, 330, 310, width=0, fill='white')
white_01 = cubeCanvas.create_rectangle(340, 240, 410, 310, width=0, fill='white')
white_02 = cubeCanvas.create_rectangle(420, 240, 490, 310, width=0, fill='white')
# White Face (Layer 2)
white_10 = cubeCanvas.create_rectangle(260, 320, 330, 390, width=0, fill='white')
white_11 = cubeCanvas.create_rectangle(340, 320, 410, 390, width=0, fill='white')
white_12 = cubeCanvas.create_rectangle(420, 320, 490, 390, width=0, fill='white')
# White Face (Layer 3)
white_20 = cubeCanvas.create_rectangle(260, 400, 330, 470, width=0, fill='white')
white_21 = cubeCanvas.create_rectangle(340, 400, 410, 470, width=0, fill='white')
white_22 = cubeCanvas.create_rectangle(420, 400, 490, 470, width=0, fill='white')

# Orange Face (Layer 1)
orange_00 = cubeCanvas.create_rectangle(260, 0, 330, 70, width=0, fill='orange')
orange_01 = cubeCanvas.create_rectangle(340, 0, 410, 70, width=0, fill='orange')
orange_02 = cubeCanvas.create_rectangle(420, 0, 490, 70, width=0, fill='orange')
# Orange Face (Layer 2)
orange_10 = cubeCanvas.create_rectangle(260, 80, 330, 150, width=0, fill='orange')
orange_11 = cubeCanvas.create_rectangle(340, 80, 410, 150, width=0, fill='orange')
orange_12 = cubeCanvas.create_rectangle(420, 80, 490, 150, width=0, fill='orange')
# Orange Face (Layer 3)
orange_20 = cubeCanvas.create_rectangle(260, 160, 330, 230, width=0, fill='orange')
orange_21 = cubeCanvas.create_rectangle(340, 160, 410, 230, width=0, fill='orange')
orange_22 = cubeCanvas.create_rectangle(420, 160, 490, 230, width=0, fill='orange')


# Blue Face (Layer 1)
blue_00 = cubeCanvas.create_rectangle(500, 240, 570, 310, width=0, fill='blue')
blue_01 = cubeCanvas.create_rectangle(580, 240, 650, 310, width=0, fill='blue')
blue_02 = cubeCanvas.create_rectangle(660, 240, 730, 310, width=0, fill='blue')
# Blue Face (Layer 2)
blue_10 = cubeCanvas.create_rectangle(500, 320, 570, 390, width=0, fill='blue')
blue_11 = cubeCanvas.create_rectangle(580, 320, 650, 390, width=0, fill='blue')
blue_12 = cubeCanvas.create_rectangle(660, 320, 730, 390, width=0, fill='blue')
# Blue Face (Layer 2)
blue_20 = cubeCanvas.create_rectangle(500, 400, 570, 470, width=0, fill='blue')
blue_21 = cubeCanvas.create_rectangle(580, 400, 650, 470, width=0, fill='blue')
blue_22 = cubeCanvas.create_rectangle(660, 400, 730, 470, width=0, fill='blue')


# Yellow Face (Layer 1)
yellow_00 = cubeCanvas.create_rectangle(740, 240, 810, 310, width=0, fill='yellow')
yellow_01 = cubeCanvas.create_rectangle(820, 240, 890, 310, width=0, fill='yellow')
yellow_02 = cubeCanvas.create_rectangle(900, 240, 970, 310, width=0, fill='yellow')
# Yellow Face (Layer 2)
yellow_10 = cubeCanvas.create_rectangle(740, 320, 810, 390, width=0, fill='yellow')
yellow_11 = cubeCanvas.create_rectangle(820, 320, 890, 390, width=0, fill='yellow')
yellow_12 = cubeCanvas.create_rectangle(900, 320, 970, 390, width=0, fill='yellow')
# Yellow Face (Layer 3)
yellow_20 = cubeCanvas.create_rectangle(740, 400, 810, 470, width=0, fill='yellow')
yellow_21 = cubeCanvas.create_rectangle(820, 400, 890, 470, width=0, fill='yellow')
yellow_22 = cubeCanvas.create_rectangle(900, 400, 970, 470, width=0, fill='yellow')


# Red Face (Layer 1)
red_00 = cubeCanvas.create_rectangle(260, 480, 330, 550, width=0, fill='red')
red_01 = cubeCanvas.create_rectangle(340, 480, 410, 550, width=0, fill='red')
red_02 = cubeCanvas.create_rectangle(420, 480, 490, 550, width=0, fill='red')
# Red Face (Layer 2)
red_10 = cubeCanvas.create_rectangle(260, 560, 330, 630, width=0, fill='red')
red_11 = cubeCanvas.create_rectangle(340, 560, 410, 630, width=0, fill='red')
red_12 = cubeCanvas.create_rectangle(420, 560, 490, 630, width=0, fill='red')
# Red Face (Layer 3)
red_20 = cubeCanvas.create_rectangle(260, 640, 330, 710, width=0, fill='red')
red_21 = cubeCanvas.create_rectangle(340, 640, 410, 710, width=0, fill='red')
red_22 = cubeCanvas.create_rectangle(420, 640, 490, 710, width=0, fill='red')




updateCubeColours()
cubeCanvas.update_idletasks()


# btnFrame = Frame(mainFrame, width=200, height=200)
# btnFrame.grid(row=1, column=0, padx=10, pady=2)

# resultlog = Text(mainFrame, width = 40, height = 24, takefocus=0)
# resultlog.grid(row=3, column=0, padx=10, pady=0)

solveButton = Button(root, text="Solve Cube", command=lambda: performAlgorithm("R Fi U F B B U U B B B R B Ri Bi B D B Di Bi D B Di Bi D B Di Bi Li Bi L B Li Bi L B Li Bi L B Li Bi L B Li Bi L B  L B Li Bi Di Bi D B B Ui Bi U B R B Ri Bi B B Ri Bi R B D B Di Bi B B B Li Bi L B U B Ui B B B L B Li Bi Di Bi D B B U R B Ri Bi Ui  B B R B B Ri Ri Bi R R Bi Ri Ri B B R B B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui  Mi Mi Bi M Bi Bi Mi Bi Mi Mi B B"))
solveButton.config(font=("Arial", 20))
solveButton.place(x=1150,y=600)


# Label For Main Title
title = Label(root, text = "Rubiks Cube Solver")
title.config(font=("Courier", 30))
title.place(x=1045, y=30)

# Label For Subtitle
subTitle = Label(root, text = "Project By Ryan Jewsbury")
subTitle.config(font=("Arial", 20))
subTitle.place(x=1090, y=60)

# More Information Button
moreInfo = Button(root, text="More Info", command=lambda:  print("more info pressed"))
moreInfo.config(font=("Arial", 15))
moreInfo.place(x=1100,y=100)

# Settings Button
settingsButton = Button(root, text="Settings", command=lambda: print("settings pressed"))
settingsButton.config(font=("Arial", 15))
settingsButton.place(x=1230,y=100)

# Scan Your Own Cube Label
scan_title = Label(root, text = "Scan Your Own Cube")
scan_title.config(font=("Arial", 20))
scan_title.place(x=1110, y=150)

# Scan Cube Button
scanCube_button = Button(root, text="Scan Cube", command=lambda: print("Scan Cube Pressed"))
scanCube_button.config(font=("Arial", 15))
scanCube_button.place(x=1160,y=180)

# Perform Move
move_title = Label(root, text = "Make Your Own Move")
move_title.config(font=("Arial", 20))
move_title.place(x=1110, y=230)

# Move Input
moveInput = Entry(root)
moveInput.place(x=1125, y=260)
inputButton = Button(root, text="Make Move", command=lambda : performAlgorithm(moveInput.get()))
inputButton.place(x=1160,y=290)

root.mainloop()

