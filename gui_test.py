# from tkinter import *
# # import RPi.GPIO as GPIO
# from datetime import *
# from time import *
#
# root = Tk()  # Draws the window
#
# rectangleId = None
#
#
# def whiteRectangle():
#     global rectangleId
#     LEDCanvas.itemconfigure(rectangleId, fill="white")
#     print('white should be on now')
#
# def greenRect():
#     global rectangleId
#     LEDCanvas.itemconfigure(rectangleId, fill="green")
#     print('white should be on now')
#
#
# def redRectangle():
#     global rectangleId
#     print('red should be on now')
#     rectangleId = LEDCanvas.create_rectangle(20, 20, 80, 80, width=0, fill='red')
#     blobid = LEDCanvas.create_rectangle(60, 60, 80, 80, width=0, fill='red')
#     root.after(2000, whiteRectangle)
#     root.after(2000, greenRect)
#
#
#
#
#
#
# # These next lines define size, position and title of tkinter window
# root.geometry('350x550+20+100')  # width x height + xpos + ypos
# root.title("Change Colours")
#
# # Frame and its contents
# mainFrame = Frame(root, width=200, height=200)
# mainFrame.grid(row=0, column=0, padx=10, pady=2)
#
# LEDCanvas = Canvas(mainFrame, width=200, height=100, bg='gray85')
# LEDCanvas.grid(row=0, column=0, padx=10, pady=2)
#
# btnFrame = Frame(mainFrame, width=200, height=200)
# btnFrame.grid(row=1, column=0, padx=10, pady=2)
#
# # resultlog = Text(mainFrame, width = 40, height = 24, takefocus=0)
# # resultlog.grid(row=3, column=0, padx=10, pady=0)
#
# testBtn = Button(btnFrame, text="Test", command=redRectangle)
# testBtn.grid(row=0, column=1, padx=10, pady=2)
#
# root.mainloop()

from rubik.cube import Cube
from tkinter import *
# import RPi.GPIO as GPIO
from datetime import *
from time import *

root = Tk()  # Draws the window

# These next lines define size, position and title of tkinter window
root.geometry('1280x900+20+100')  # width x height + xpos + ypos
root.title("Cube Solver")

# Frame and its contents
mainFrame = Frame(root, width=200, height=200)
mainFrame.grid(row=0, column=0, padx=10, pady=2)

cubeCanvas = Canvas(mainFrame, width=640, height=700, bg='gray0')
cubeCanvas.grid(row=0, column=0, padx=10, pady=2)


c = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")


# Converts Cubie To Colour for Digital Cube
def colourFromLetter(value):
    try:
        colors = {'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'W': 'White', 'Y': 'Yellow'}
        return colors[value]
    except:
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

    # White Face
    cubeCanvas.itemconfigure(white_00, fill=colourFromLetter(c.get_piece(-1,1,1).colors[2]))
    cubeCanvas.itemconfigure(white_01, fill=colourFromLetter(c.get_piece(0,1,1).colors[2]))
    cubeCanvas.itemconfigure(white_02, fill=colourFromLetter(c.get_piece(1,1,1).colors[2]))




def makeMove(move):
    print("Making move")
    c.sequence(move)
    updateCubeColours()


# Green Face...
green_00 = cubeCanvas.create_rectangle(20, 240, 90, 310, width=0, fill='green')
green_01 = cubeCanvas.create_rectangle(100, 240, 170, 310, width=0, fill='green')
green_02 = cubeCanvas.create_rectangle(180, 240, 250, 310, width=0, fill='green')

green_10 = cubeCanvas.create_rectangle(20, 320, 90, 390, width=0, fill='green')
green_11 = cubeCanvas.create_rectangle(100, 320, 170, 390, width=0, fill='green')
green_12 = cubeCanvas.create_rectangle(180, 320, 250, 390, width=0, fill='green')

green_20 = cubeCanvas.create_rectangle(20, 400, 90, 470, width=0, fill='green')
green_21 = cubeCanvas.create_rectangle(100, 400, 170, 470, width=0, fill='green')
green_22 = cubeCanvas.create_rectangle(180, 400, 250, 470, width=0, fill='green')

# White Face...
white_00 = cubeCanvas.create_rectangle(260, 240, 330, 310, width=0, fill='white')
white_01 = cubeCanvas.create_rectangle(340, 240, 410, 310, width=0, fill='white')
white_02 = cubeCanvas.create_rectangle(420, 240, 490, 310, width=0, fill='white')

white_10 = cubeCanvas.create_rectangle(260, 320, 330, 390, width=0, fill='white')
white_11 = cubeCanvas.create_rectangle(340, 320, 410, 390, width=0, fill='white')
white_12 = cubeCanvas.create_rectangle(420, 320, 490, 390, width=0, fill='white')
#
white_20 = cubeCanvas.create_rectangle(260, 400, 330, 470, width=0, fill='white')
white_21 = cubeCanvas.create_rectangle(340, 400, 410, 470, width=0, fill='white')
white_22 = cubeCanvas.create_rectangle(420, 400, 490, 470, width=0, fill='white')




btnFrame = Frame(mainFrame, width=200, height=200)
btnFrame.grid(row=1, column=0, padx=10, pady=2)

# resultlog = Text(mainFrame, width = 40, height = 24, takefocus=0)
# resultlog.grid(row=3, column=0, padx=10, pady=0)

testBtn = Button(btnFrame, text="Solve Cube", command=lambda: makeMove("U"))
testBtn.grid(row=0, column=1, padx=10, pady=2)



root.mainloop()

