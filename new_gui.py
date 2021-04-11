import random
from rubik.cube import Cube
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from CubeScanner import CubeScanner
from Solver import SolveCube
import numpy as np
from fpdf import FPDF


root = Tk()
edit_mode = False
current_color = " "

settings_open = False

# These next lines define size, position and title of tkinter window
root.geometry('1400x740+10+10')  # width x height + xpos + ypos
root.title("Cube Solver")

# Frame and its contents
mainFrame = Frame(root, width=200, height=200)
mainFrame.grid(row=0, column=0, padx=10, pady=2)

cubeCanvas = Canvas(mainFrame, width=1000, height=720, bg='black',  bd=0, highlightthickness=0, borderwidth=0,highlightbackground="#232323" )
cubeCanvas.grid(row=0, column=0, padx=0, pady=0)

current_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")


def checkSolvable(cube_string):
    cube_colors = ["O", "W", "R", "G", "B", "Y"]
    color_count = []
    for i in range(len(cube_colors)):
        color_count.append(str(cube_string.count(cube_colors[i])))
    if all(x==color_count[0] for x in color_count):
        print("All Colors Have 9")
        return True
    else:
        print(color_count)
        return False


def colourFromLetter(value):
    try:
        colors = {'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'W': 'White', 'Y': 'Yellow'}
        return colors[value]
    except:
        messagebox.showinfo("Say Hello", "Hello World")
        return None


# Updates cube colours from c
def updateCubeColours():
    # Green Face (Layer 1)
    cubeCanvas.itemconfigure(green_00, fill=colourFromLetter(current_cube.get_piece(-1, 1, -1).colors[0]))
    cubeCanvas.itemconfigure(green_01, fill=colourFromLetter(current_cube.get_piece(-1, 1, 0).colors[0]))
    cubeCanvas.itemconfigure(green_02, fill=colourFromLetter(current_cube.get_piece(-1, 1, 1).colors[0]))
    # Green Face (Layer 2)
    cubeCanvas.itemconfigure(green_10, fill=colourFromLetter(current_cube.get_piece(-1, 0, -1).colors[0]))
    cubeCanvas.itemconfigure(green_11, fill=colourFromLetter(current_cube.get_piece(-1, 0, 0).colors[0]))
    cubeCanvas.itemconfigure(green_12, fill=colourFromLetter(current_cube.get_piece(-1, 0, 1).colors[0]))
    # Green Face (Layer 3)
    cubeCanvas.itemconfigure(green_20, fill=colourFromLetter(current_cube.get_piece(-1, -1, -1).colors[0]))
    cubeCanvas.itemconfigure(green_21, fill=colourFromLetter(current_cube.get_piece(-1, -1, 0).colors[0]))
    cubeCanvas.itemconfigure(green_22, fill=colourFromLetter(current_cube.get_piece(-1, -1, 1).colors[0]))

    # White Face (Layer 1)
    cubeCanvas.itemconfigure(white_00, fill=colourFromLetter(current_cube.get_piece(-1, 1, 1).colors[2]))
    cubeCanvas.itemconfigure(white_01, fill=colourFromLetter(current_cube.get_piece(0, 1, 1).colors[2]))
    cubeCanvas.itemconfigure(white_02, fill=colourFromLetter(current_cube.get_piece(1, 1, 1).colors[2]))
    # White Face (Layer 2)
    cubeCanvas.itemconfigure(white_10, fill=colourFromLetter(current_cube.get_piece(-1, 0, 1).colors[2]))
    cubeCanvas.itemconfigure(white_11, fill=colourFromLetter(current_cube.get_piece(0, 0, 1).colors[2]))
    cubeCanvas.itemconfigure(white_12, fill=colourFromLetter(current_cube.get_piece(1, 0, 1).colors[2]))
    # White Face (Layer 3)
    cubeCanvas.itemconfigure(white_20, fill=colourFromLetter(current_cube.get_piece(-1, -1, 1).colors[2]))
    cubeCanvas.itemconfigure(white_21, fill=colourFromLetter(current_cube.get_piece(0, -1, 1).colors[2]))
    cubeCanvas.itemconfigure(white_22, fill=colourFromLetter(current_cube.get_piece(1, -1, 1).colors[2]))

    # Orange Face (Layer 1)
    cubeCanvas.itemconfigure(orange_00, fill=colourFromLetter(current_cube.get_piece(-1, 1, -1).colors[1]))
    cubeCanvas.itemconfigure(orange_01, fill=colourFromLetter(current_cube.get_piece(0, 1, -1).colors[1]))
    cubeCanvas.itemconfigure(orange_02, fill=colourFromLetter(current_cube.get_piece(1, 1, -1).colors[1]))
    # Orange Face (Layer 2)
    cubeCanvas.itemconfigure(orange_10, fill=colourFromLetter(current_cube.get_piece(-1, 1, 0).colors[1]))
    cubeCanvas.itemconfigure(orange_11, fill=colourFromLetter(current_cube.get_piece(0, 1, 0).colors[1]))
    cubeCanvas.itemconfigure(orange_12, fill=colourFromLetter(current_cube.get_piece(1, 1, 0).colors[1]))
    # Orange Face (Layer 3)
    cubeCanvas.itemconfigure(orange_20, fill=colourFromLetter(current_cube.get_piece(-1, 1, 1).colors[1]))
    cubeCanvas.itemconfigure(orange_21, fill=colourFromLetter(current_cube.get_piece(0, 1, 1).colors[1]))
    cubeCanvas.itemconfigure(orange_22, fill=colourFromLetter(current_cube.get_piece(1, 1, 1).colors[1]))

    # Red Face (Layer 1)
    cubeCanvas.itemconfigure(red_00, fill=colourFromLetter(current_cube.get_piece(-1, -1, 1).colors[1]))
    cubeCanvas.itemconfigure(red_01, fill=colourFromLetter(current_cube.get_piece(0, -1, 1).colors[1]))
    cubeCanvas.itemconfigure(red_02, fill=colourFromLetter(current_cube.get_piece(1, -1, 1).colors[1]))
    # Red Face (Layer 2)
    cubeCanvas.itemconfigure(red_10, fill=colourFromLetter(current_cube.get_piece(-1, -1, 0).colors[1]))
    cubeCanvas.itemconfigure(red_11, fill=colourFromLetter(current_cube.get_piece(0, -1, 0).colors[1]))
    cubeCanvas.itemconfigure(red_12, fill=colourFromLetter(current_cube.get_piece(1, -1, 0).colors[1]))
    # Red Face (Layer 3)
    cubeCanvas.itemconfigure(red_20, fill=colourFromLetter(current_cube.get_piece(-1, -1, -1).colors[1]))
    cubeCanvas.itemconfigure(red_21, fill=colourFromLetter(current_cube.get_piece(0, -1, -1).colors[1]))
    cubeCanvas.itemconfigure(red_22, fill=colourFromLetter(current_cube.get_piece(1, -1, -1).colors[1]))

    # Blue Face (Layer 1)
    cubeCanvas.itemconfigure(blue_00, fill=colourFromLetter(current_cube.get_piece(1, 1, 1).colors[0]))
    cubeCanvas.itemconfigure(blue_01, fill=colourFromLetter(current_cube.get_piece(1, 1, 0).colors[0]))
    cubeCanvas.itemconfigure(blue_02, fill=colourFromLetter(current_cube.get_piece(1, 1, -1).colors[0]))
    # Blue Face (Layer 2)
    cubeCanvas.itemconfigure(blue_10, fill=colourFromLetter(current_cube.get_piece(1, 0, 1).colors[0]))
    cubeCanvas.itemconfigure(blue_11, fill=colourFromLetter(current_cube.get_piece(1, 0, 0).colors[0]))
    cubeCanvas.itemconfigure(blue_12, fill=colourFromLetter(current_cube.get_piece(1, 0, -1).colors[0]))
    # Blue Face (Layer 3)
    cubeCanvas.itemconfigure(blue_20, fill=colourFromLetter(current_cube.get_piece(1, -1, 1).colors[0]))
    cubeCanvas.itemconfigure(blue_21, fill=colourFromLetter(current_cube.get_piece(1, -1, 0).colors[0]))
    cubeCanvas.itemconfigure(blue_22, fill=colourFromLetter(current_cube.get_piece(1, -1, -1).colors[0]))

    # Yellow Face (Layer 1)
    cubeCanvas.itemconfigure(yellow_00, fill=colourFromLetter(current_cube.get_piece(1, 1, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_01, fill=colourFromLetter(current_cube.get_piece(0, 1, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_02, fill=colourFromLetter(current_cube.get_piece(-1, 1, -1).colors[2]))
    # Yellow Face (Layer 2)
    cubeCanvas.itemconfigure(yellow_10, fill=colourFromLetter(current_cube.get_piece(1, 0, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_11, fill=colourFromLetter(current_cube.get_piece(0, 0, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_12, fill=colourFromLetter(current_cube.get_piece(-1, 0, -1).colors[2]))
    # Yellow Face (Layer 3)
    cubeCanvas.itemconfigure(yellow_20, fill=colourFromLetter(current_cube.get_piece(1, -1, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_21, fill=colourFromLetter(current_cube.get_piece(0, -1, -1).colors[2]))
    cubeCanvas.itemconfigure(yellow_22, fill=colourFromLetter(current_cube.get_piece(-1, -1, -1).colors[2]))


def editMode(edit_mode_label, edit_cube_button):
    global edit_mode, cube_layout, current_cube
    cubeCanvas.update_idletasks()
    edit_mode = not edit_mode
    if edit_mode:
        print("Entering Edit Mode")
        edit_cube_button.config(text="Leave Edit Mode")
        edit_mode_label.place(x=30, y=20)
        cubeCanvas.itemconfigure(white_color, state='normal')
        cubeCanvas.itemconfigure(red_color, state='normal')
        cubeCanvas.itemconfigure(blue_color, state='normal')
        cubeCanvas.itemconfigure(green_color, state='normal')
        cubeCanvas.itemconfigure(orange_color, state='normal')
        cubeCanvas.itemconfigure(yellow_color, state='normal')
        updateCube(flattenCube())
    else:
        print("Leaving Edit mode")
        edit_cube_button.config(text="Enter Edit Mode")
        edit_mode_label.place(x=-40, y=-40)
        cubeCanvas.itemconfigure(white_color, state='hidden')
        cubeCanvas.itemconfigure(red_color, state='hidden')
        cubeCanvas.itemconfigure(blue_color, state='hidden')
        cubeCanvas.itemconfigure(green_color, state='hidden')
        cubeCanvas.itemconfigure(orange_color, state='hidden')
        cubeCanvas.itemconfigure(yellow_color, state='hidden')
        updateCube(flattenCube())
    return not edit_mode


def editColor(event):
    global current_color, edit_mode
    if edit_mode:
        if current_color == " ":
            current_color = "white"

        # First Stage Decide What Colour Has Been Selected...
        options = {55: "White", 56: "red", 57: "blue", 58: "orange", 59: "green", 60: "Yellow"}
        if event.widget.find_withtag("current")[0] in options:
            current_color = options.get(event.widget.find_withtag("current")[0])
            print("Current Color = " + str(current_color))
            # Default To White...
        else:
            # # Check the value is not in dict
            print("You clicked " + str(event))
            print("Current Color = " + str(current_color))
            current = event.widget.find_withtag("current")[0]
            event.widget.itemconfig(current, fill=current_color)
    else:
        print("Need to be in edit mode")


# Converts Rectangle To Color Letter ("green_00" = "g") For use in cube...
def convertToLetter(tag):
    color = cubeCanvas.itemcget(tag, "fill")
    options = {"red": "R", "White": "W", "Yellow": "Y", "orange": "O", "blue": "B", "green": "G"}
    return str(options.get(color))


# Takes the values from each index and returns a string...
# This will then be used with the solver.
def flattenCube():
    cube_string = ""
    # First Layer
    cube_string += str(convertToLetter(orange_00) + convertToLetter(orange_01)+ convertToLetter(orange_02)
    + convertToLetter(orange_10)+ convertToLetter(orange_11)+  convertToLetter(orange_12) + convertToLetter(orange_20)
    + convertToLetter(orange_21) + convertToLetter(orange_22))

    # Second Layer
    cube_string += str(convertToLetter(green_00) + convertToLetter(green_01) + convertToLetter(green_02)
    + convertToLetter(white_00) + convertToLetter(white_01) + convertToLetter(white_02) + convertToLetter(blue_00)
    + convertToLetter(blue_01) + convertToLetter(blue_02) + convertToLetter(yellow_00) + convertToLetter(yellow_01)
    + convertToLetter(yellow_02))

    # Third Layer
    cube_string += str(convertToLetter(green_10) + convertToLetter(green_11) + convertToLetter(green_12)
    + convertToLetter(white_10) + convertToLetter(white_11) + convertToLetter(white_12) + convertToLetter(blue_10)
    + convertToLetter(blue_11) + convertToLetter(blue_12) + convertToLetter(yellow_10) + convertToLetter(yellow_11)
    + convertToLetter(yellow_12))

    # Fourth Layer
    cube_string += str(convertToLetter(green_20) + convertToLetter(green_21) + convertToLetter(green_22)
    + convertToLetter(white_20) + convertToLetter(white_21) + convertToLetter(white_22) + convertToLetter(blue_20)
    + convertToLetter(blue_21) + convertToLetter(blue_22) + convertToLetter(yellow_20) + convertToLetter(yellow_21)
    + convertToLetter(yellow_22))

    # Final Layer
    cube_string += str(convertToLetter(red_00) + convertToLetter(red_01) + convertToLetter(red_02) + convertToLetter(red_10)
    + convertToLetter(red_11) + convertToLetter(red_12) + convertToLetter(red_20) + convertToLetter(
        red_21) + convertToLetter(red_22))

    return cube_string


# To be used in edit mode - updates cube  with new colors.
def updateCube(newCubeString):
    global current_cube
    current_cube = Cube(newCubeString)
    updateCubeColours()
    cubeCanvas.update_idletasks()


def printDetails():
    print(flattenCube())
    print(current_cube)


def performAlgorithm(algo):
    if edit_mode:
        messagebox.showinfo("Edit Mode","Please Leave Edit Mode")
    else:
        for move in algo.split():
            try:
                print("Move = " + move)
                print(current_cube)
                current_cube.sequence(move)
                cubeCanvas.after(200, updateCubeColours())
                cubeCanvas.update_idletasks()
            except:
                print("Cannot Perform Move '" + move + "'")


def notationToMove(move):
    print("")
    notation = {
        "F": "Front Face Right",
        "Fi": "Front Face Left",
        "R": "Right Side Up",
        "Ri": "Right Side Down",
        "L": "Left Side Down",
        "Li": "Left Side Up",
        "U": "Top Layer Left",
        "Ui": "Top Layer Right",
        "B": "Back Layer Left",
        "Bi": "Back Layer Right",
        "D": "Bottom Layer Right",
        "Di": "Bottom Layer Left",
        "M": "Middle Layer Up",
        "Mi": "Middle Layer Down"
    }
    return notation.get(move)


def solveCube():
    global current_cube
    if edit_mode:
        messagebox.showinfo("Edit Mode", "Please Leave Edit Mode")
    else:
        new_cube = Cube(flattenCube())
        cube_str = flattenCube()
        if new_cube.is_solved():
            messagebox.showinfo("Cube Solved", "This cube is already solved!")
        else:
            if checkSolvable(flattenCube()):
                solver = SolveCube(new_cube)
                algo = solver.solveCube()
                if algo == None:
                    messagebox.showerror(title="Cube Unsolvable", message="This cube cannot be solved, - this is due to an piece incorrectly rotated ,please double check your cube / the digital on-screen cube")
                else:
                    performAlgorithm(algo[0])
                    solve_text.set(algo[0])
                    displaySummary(algo, cube_str)
                    print(algo[0])
                    # R Ui F L B D Ri Li B Ui
                    #  F D Fi F U Fi F R Fi D Fi R F Ri Bi R B D B Di Bi D B Di Bi D B Di Bi B B B Li Bi L B Li Bi L B Li Bi L B B B L B Li Bi B B R B Ri Bi R B Ri Bi R B Ri Bi  D B Di Bi Ri Bi R B B B D B Di Bi Ri Bi R B B B Li Bi L B U B Ui B B Di Bi D B L B Li Bi B B R B Ri Bi Ui Bi U B B D B L Bi Li Di  B B B B R R F Ri B B R Fi Ri B B Ri B R B Ri Bi Ri U R R Bi Ri Bi R B Ri Ui  B Mi Mi Bi M Bi Bi Mi Bi Mi Mi B
            else:
                messagebox.showerror("Cube Unsolvable", "Please ensure there are 9 of each colour on the cube.")


def scanCube():
    c = CubeScanner()
    fullcube = c.scan()
    print(fullcube)
    colors = {"White": "W", "Yellow": "Y", "Red": "R", "Green": "G", "Orange": "O", "Blue": "B"}
    cube_string = ""
    # Layer 1
    # Orange Face
    for val in np.nditer(fullcube[5]):
        cube_string += colors.get(str(val))
    # Layer 2 (Top Row From Green-White-Blue-Yellow)
    for val in np.nditer(fullcube[1][0]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[0][0]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[3][0]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[2][0]):
        cube_string += colors.get(str(val))
    # Layer 2 (Middle Row From Green-White-Blue-Yellow)
    for val in np.nditer(fullcube[1][1]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[0][1]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[3][1]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[2][1]):
        cube_string += colors.get(str(val))
    # Layer 3 (Bottom Row From Green-White-Blue-Yellow)
    for val in np.nditer(fullcube[1][2]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[0][2]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[3][2]):
        cube_string += colors.get(str(val))
    for val in np.nditer(fullcube[2][2]):
        cube_string += colors.get(str(val))
    # Red Face
    for val in np.nditer(fullcube[4]):
        cube_string += colors.get(str(val))

    print("String = " + cube_string)
    updateCube(cube_string)
    updateCubeColours()


def displaySummary(algo, cube_str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(40, 10, 'Rubiks Cube Solve Summary:')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(40, 10, 'Cube String: ' + cube_str)
    pdf.ln(h='')

    # Start of Summary of Solve
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'White Cross:')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 10,'' + str(algo[1][0]))
    # White Corner
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'White Corners:')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 8, '' + str(algo[1][1]))
    # Second layer
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'Second Layer (Edge Pieces):')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 10, ' ' + str(algo[1][2]))
    # Yellow Cross
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'Yellow Cross (Oll Look 1):')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 10, ' ' + str(algo[1][3]))
    # OLL
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'OLL Look 2:')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 10, ' ' + str(algo[1][4]))
    # Pll 1
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'Permutate Top Layer (PLL Look 1):')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 10, ' ' + str(algo[1][5]))
    # Solve cube
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'Solve Cube (PLL Look 2):')
    pdf.ln(h='')
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 10, ' ' + str(algo[1][6]))

    # Count Moves -
    moves = 0
    for i in algo[0].split():
        moves += 1
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 5, 'Cube Solved In ' + str(moves) + ' Moves.')
    pdf.ln(h='')
    pdf.cell(40, 5, "Entire Solve... (In Words)")
    pdf.ln(h='')
    for i in algo[0].split():
        print(notationToMove(i))
        pdf.cell(0, 10, ''+str(notationToMove(i)), 0, 1)


    pdf.output('CubeSolve.pdf', 'F')


def generateScramble():
    notation = [" R ", " U ", " F ", " L ", " B ", "  D ", " Ri ", " Ui ", " Fi ", " Li ", " Bi ", "  Di "]
    scramble = " "
    for i in range(1, 20):
        scramble += str(notation[random.randrange(0, 12)])
    performAlgorithm(scramble)
    return 0


def openSettings():
    global settings_open
    from PIL import ImageTk, Image

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Settings")

    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    settings_canvas = Canvas(newWindow, width=400, height=400)
    settings_canvas.grid(row=0, column=0, padx=0, pady=0)


    cube_image = PhotoImage(file='Images/cube_icon.gif')
    image_label = Label(settings_canvas, image=cube_image)
    image_label.photo = cube_image
    image_label.place(x=148,y=0)
    #
    # # # Settings Label (Title)
    # settings_label = Label(settings_canvas, text=" Settings:")
    # settings_label.config(font=("Arial", 20))
    # settings_label.place(x=180,y=10)

    # Mode Label
    mode_label = Label(settings_canvas, text=" Mode")
    mode_label.config(font=("Arial", 20))
    mode_label.place(x=165, y=105)

    mode_dark = Button(settings_canvas, text="Dark Mode", command= lambda: theme_dark())
    mode_dark.config(font=("Arial", 15))
    mode_dark.place(x=95, y=140)

    mode_light = Button(settings_canvas, text="Light Mode", command= lambda: print("Light Mode"))
    mode_light.config(font=("Arial", 15))
    mode_light.place(x=200, y=140)

    # Sound Label
    sound_label = Label(settings_canvas, text=" Sound")
    sound_label.config(font=("Arial", 20))
    sound_label.place(x=160, y=185)

    mute_button = Button(settings_canvas, text="Mute Sound", command= lambda: print("Mute Mode"))
    mute_button.config(font=("Arial", 15))
    mute_button.place(x=85, y=220)

    unmute_button = Button(settings_canvas, text="Unmute Sound", command= lambda: print("Unmute Mode"))
    unmute_button.config(font=("Arial", 15))
    unmute_button.place(x=200, y=220)

    # Options Label
    close_label = Label(settings_canvas, text="Config & Links")
    close_label.config(font=("Arial", 20))
    close_label.place(x=130, y=270)

    close_app_button = Button(settings_canvas, text="Close App", command=lambda: print("Closing App"))
    close_app_button.config(font=("Arial", 15))
    close_app_button.place(x=153, y=305)

    github_button = Button(settings_canvas, text="Git-Hub", command=lambda: print("Opening GitHub"))
    github_button.config(font=("Arial", 15))
    github_button.place(x=120, y=340)

    reset_app_button = Button(settings_canvas, text="Restart", command=lambda: print("Reseting App"))
    reset_app_button.config(font=("Arial", 15))
    reset_app_button.place(x=200, y=340)

    def theme_dark():
        # Background
        root.configure(background='#232323')
        # Text & Labels
        title.config(bg="#232323", fg="#fff")
        subTitle.config(bg="#232323", fg="#fff")
        scan_title.config(bg="#232323", fg="#fff")
        edit_mode_label.config(bg="#232323", fg="#fff")
        scramble_label.config(bg="#232323", fg="#fff")
        move_title.config(bg="#232323", fg="#fff")
        edit_cube_title.config(bg="#232323", fg="#fff")
        # Buttons & Input
        settingsButton.config(highlightbackground="#232323")
        moreInfo.config(highlightbackground="#232323")
        scanCube_button.config(highlightbackground="#232323")
        edit_cube_button.config(highlightbackground="#232323")
        moveInputButton.config(highlightbackground="#232323")
        solveButton.config(highlightbackground="#232323")
        resetButton.config(highlightbackground="#232323")
        randomScrambleButton.config(highlightbackground="#232323")

        # Settings Screen
        # Background
        newWindow.configure(background='#232323')
        settings_canvas.config(bg="#232323", bd=0, highlightthickness=0, borderwidth=0,highlightbackground="#232323")
        # Images
        image_label.config(bg="#232323")
        # Text & Labels
        mode_label.config(bg="#232323", fg="#fff")
        sound_label.config(bg="#232323", fg="#fff")
        close_label.config(bg="#232323", fg="#fff")
        # Buttons
        mode_dark.config(highlightbackground="#232323")
        mode_light.config(highlightbackground="#232323")
        mute_button.config(highlightbackground="#232323")
        unmute_button.config(highlightbackground="#232323")
        close_app_button.config(highlightbackground="#232323")
        github_button.config(highlightbackground="#232323")
        reset_app_button.config(highlightbackground="#232323")




    newWindow.grab_set()



green_00 = cubeCanvas.create_rectangle(20, 240, 90, 310, width=0, fill='green', tag="green_00")
cubeCanvas.tag_bind("green_00", "<Button-1>", editColor)
green_01 = cubeCanvas.create_rectangle(100, 240, 170, 310, width=0, fill='green', tag="green_01")
cubeCanvas.tag_bind("green_01", "<Button-1>", editColor)
green_02 = cubeCanvas.create_rectangle(180, 240, 250, 310, width=0, fill='green', tag="green_02")
cubeCanvas.tag_bind("green_02", "<Button-1>", editColor)

# Green Face (Layer 2)
green_10 = cubeCanvas.create_rectangle(20, 320, 90, 390, width=0, fill='green', tag="green_10")
cubeCanvas.tag_bind("green_10", "<Button-1>", editColor)
green_11 = cubeCanvas.create_rectangle(100, 320, 170, 390, width=0, fill='green', tag="green_11")
# Green_11 cannot be edited
green_12 = cubeCanvas.create_rectangle(180, 320, 250, 390, width=0, fill='green', tag="green_12")
cubeCanvas.tag_bind("green_12", "<Button-1>", editColor)
# Green Face (Layer 3)
green_20 = cubeCanvas.create_rectangle(20, 400, 90, 470, width=0, fill='green', tag="green_20")
cubeCanvas.tag_bind("green_20", "<Button-1>", editColor)
green_21 = cubeCanvas.create_rectangle(100, 400, 170, 470, width=0, fill='green', tag="green_21")
cubeCanvas.tag_bind("green_21", "<Button-1>", editColor)
green_22 = cubeCanvas.create_rectangle(180, 400, 250, 470, width=0, fill='green', tag="green_22")
cubeCanvas.tag_bind("green_22", "<Button-1>", editColor)

# White Face (Layer 1)
white_00 = cubeCanvas.create_rectangle(260, 240, 330, 310, width=0, fill='White', tag="white_00")
cubeCanvas.tag_bind("white_00", "<Button-1>", editColor)
white_01 = cubeCanvas.create_rectangle(340, 240, 410, 310, width=0, fill='White', tag="white_01")
cubeCanvas.tag_bind("white_01", "<Button-1>", editColor)
white_02 = cubeCanvas.create_rectangle(420, 240, 490, 310, width=0, fill='White', tag="white_02")
cubeCanvas.tag_bind("white_02", "<Button-1>", editColor)

# White Face (Layer 2)
white_10 = cubeCanvas.create_rectangle(260, 320, 330, 390, width=0, fill='White', tag="white_10")
cubeCanvas.tag_bind("white_10", "<Button-1>", editColor)
white_11 = cubeCanvas.create_rectangle(340, 320, 410, 390, width=0, fill='White', tag="white_11")
# White_11 cannot be edited
white_12 = cubeCanvas.create_rectangle(420, 320, 490, 390, width=0, fill='White', tag="white_12")
cubeCanvas.tag_bind("white_12", "<Button-1>", editColor)

# White Face (Layer 3)
white_20 = cubeCanvas.create_rectangle(260, 400, 330, 470, width=0, fill='White', tag="white_20")
cubeCanvas.tag_bind("white_20", "<Button-1>", editColor)
white_21 = cubeCanvas.create_rectangle(340, 400, 410, 470, width=0, fill='White', tag="white_21")
cubeCanvas.tag_bind("white_21", "<Button-1>", editColor)
white_22 = cubeCanvas.create_rectangle(420, 400, 490, 470, width=0, fill='White', tag="white_22")
cubeCanvas.tag_bind("white_22", "<Button-1>", editColor)

# Orange Face (Layer 1)
orange_00 = cubeCanvas.create_rectangle(260, 0, 330, 70, width=0, fill='orange', tag="orange_00")
cubeCanvas.tag_bind("orange_00", "<Button-1>", editColor)
orange_01 = cubeCanvas.create_rectangle(340, 0, 410, 70, width=0, fill='orange', tag="orange_01")
cubeCanvas.tag_bind("orange_01", "<Button-1>", editColor)
orange_02 = cubeCanvas.create_rectangle(420, 0, 490, 70, width=0, fill='orange', tag="orange_02")
cubeCanvas.tag_bind("orange_02", "<Button-1>", editColor)

# Orange Face (Layer 2)
orange_10 = cubeCanvas.create_rectangle(260, 80, 330, 150, width=0, fill='orange', tag="orange_10")
cubeCanvas.tag_bind("orange_10", "<Button-1>", editColor)
orange_11 = cubeCanvas.create_rectangle(340, 80, 410, 150, width=0, fill='orange', tag="orange_11")

orange_12 = cubeCanvas.create_rectangle(420, 80, 490, 150, width=0, fill='orange', tag="orange_12")
cubeCanvas.tag_bind("orange_12", "<Button-1>", editColor)

# Orange Face (Layer 3)
orange_20 = cubeCanvas.create_rectangle(260, 160, 330, 230, width=0, fill='orange', tag="orange_20")
cubeCanvas.tag_bind("orange_20", "<Button-1>", editColor)
orange_21 = cubeCanvas.create_rectangle(340, 160, 410, 230, width=0, fill='orange', tag="orange_21")
cubeCanvas.tag_bind("orange_21", "<Button-1>", editColor)
orange_22 = cubeCanvas.create_rectangle(420, 160, 490, 230, width=0, fill='orange', tag="orange_22")
cubeCanvas.tag_bind("orange_22", "<Button-1>", editColor)

# Blue Face (Layer 1)
blue_00 = cubeCanvas.create_rectangle(500, 240, 570, 310, width=0, fill='blue', tag="blue_00")
cubeCanvas.tag_bind("blue_00", "<Button-1>", editColor)
blue_01 = cubeCanvas.create_rectangle(580, 240, 650, 310, width=0, fill='blue', tag="blue_01")
cubeCanvas.tag_bind("blue_01", "<Button-1>", editColor)
blue_02 = cubeCanvas.create_rectangle(660, 240, 730, 310, width=0, fill='blue', tag="blue_02")
cubeCanvas.tag_bind("blue_02", "<Button-1>", editColor)

# Blue Face (Layer 2)
blue_10 = cubeCanvas.create_rectangle(500, 320, 570, 390, width=0, fill='blue', tag="blue_10")
cubeCanvas.tag_bind("blue_10", "<Button-1>", editColor)
blue_11 = cubeCanvas.create_rectangle(580, 320, 650, 390, width=0, fill='blue', tag="blue_11")

blue_12 = cubeCanvas.create_rectangle(660, 320, 730, 390, width=0, fill='blue', tag="blue_21")
cubeCanvas.tag_bind("blue_12", "<Button-1>", editColor)

# Blue Face (Layer 2)
blue_20 = cubeCanvas.create_rectangle(500, 400, 570, 470, width=0, fill='blue', tag="blue_20")
cubeCanvas.tag_bind("blue_20", "<Button-1>", editColor)
blue_21 = cubeCanvas.create_rectangle(580, 400, 650, 470, width=0, fill='blue', tag="blue_21")
cubeCanvas.tag_bind("blue_21", "<Button-1>", editColor)
blue_22 = cubeCanvas.create_rectangle(660, 400, 730, 470, width=0, fill='blue', tag="blue_22")
cubeCanvas.tag_bind("blue_22", "<Button-1>", editColor)

# Yellow Face (Layer 1)
yellow_00 = cubeCanvas.create_rectangle(740, 240, 810, 310, width=0, fill='Yellow', tag="yellow_00")
cubeCanvas.tag_bind("yellow_00", "<Button-1>", editColor)
yellow_01 = cubeCanvas.create_rectangle(820, 240, 890, 310, width=0, fill='Yellow', tag="yellow_01")
cubeCanvas.tag_bind("yellow_01", "<Button-1>", editColor)
yellow_02 = cubeCanvas.create_rectangle(900, 240, 970, 310, width=0, fill='Yellow', tag="yellow_02")
cubeCanvas.tag_bind("yellow_02", "<Button-1>", editColor)

# Yellow Face (Layer 2)
yellow_10 = cubeCanvas.create_rectangle(740, 320, 810, 390, width=0, fill='Yellow', tag="yellow_10")
cubeCanvas.tag_bind("yellow_10", "<Button-1>", editColor)
yellow_11 = cubeCanvas.create_rectangle(820, 320, 890, 390, width=0, fill='Yellow', tag="yellow_11")

yellow_12 = cubeCanvas.create_rectangle(900, 320, 970, 390, width=0, fill='Yellow', tag="yellow_21")
cubeCanvas.tag_bind("yellow_12", "<Button-1>", editColor)

# Yellow Face (Layer 3)
yellow_20 = cubeCanvas.create_rectangle(740, 400, 810, 470, width=0, fill='Yellow', tag="yellow_20")
cubeCanvas.tag_bind("yellow_20", "<Button-1>", editColor)
yellow_21 = cubeCanvas.create_rectangle(820, 400, 890, 470, width=0, fill='Yellow', tag="yellow_21")
cubeCanvas.tag_bind("yellow_21", "<Button-1>", editColor)
yellow_22 = cubeCanvas.create_rectangle(900, 400, 970, 470, width=0, fill='Yellow', tag="yellow_22")
cubeCanvas.tag_bind("yellow_22", "<Button-1>", editColor)

# Red Face (Layer 1)
red_00 = cubeCanvas.create_rectangle(260, 480, 330, 550, width=0, fill='red', tag="red_00")
cubeCanvas.tag_bind("red_00", "<Button-1>", editColor)
red_01 = cubeCanvas.create_rectangle(340, 480, 410, 550, width=0, fill='red', tag="red_01")
cubeCanvas.tag_bind("red_01", "<Button-1>", editColor)
red_02 = cubeCanvas.create_rectangle(420, 480, 490, 550, width=0, fill='red', tag="red_02")
cubeCanvas.tag_bind("red_02", "<Button-1>", editColor)

# Red Face (Layer 2)
red_10 = cubeCanvas.create_rectangle(260, 560, 330, 630, width=0, fill='red', tag="red_10")
cubeCanvas.tag_bind("red_10", "<Button-1>", editColor)
red_11 = cubeCanvas.create_rectangle(340, 560, 410, 630, width=0, fill='red', tag="red_11")

red_12 = cubeCanvas.create_rectangle(420, 560, 490, 630, width=0, fill='red', tag="red_12")
cubeCanvas.tag_bind("red_12", "<Button-1>", editColor)

# Red Face (Layer 3)
red_20 = cubeCanvas.create_rectangle(260, 640, 330, 710, width=0, fill='red', tag="red_20")
cubeCanvas.tag_bind("red_20", "<Button-1>", editColor)
red_21 = cubeCanvas.create_rectangle(340, 640, 410, 710, width=0, fill='red', tag="red_21")
cubeCanvas.tag_bind("red_21", "<Button-1>", editColor)
red_22 = cubeCanvas.create_rectangle(420, 640, 490, 710, width=0, fill='red', tag="red_21")
cubeCanvas.tag_bind("red_22", "<Button-1>", editColor)

# Label For Main Title
title = Label(root, text="Rubiks Cube Solver")
title.config(font=("Courier", 30))
title.place(x=1045, y=30)

# Label For Subtitle
subTitle = Label(root, text="Project By Ryan Jewsbury")
subTitle.config(font=("Arial", 20))
subTitle.place(x=1090, y=60)

# More Information Button
moreInfo = Button(root, text="More Info", command=lambda: print("more info pressed"))
moreInfo.config(font=("Arial", 15))
moreInfo.place(x=1100, y=100)

# Settings Button
settingsButton = Button(root, text="Settings", command=lambda: openSettings())
settingsButton.config(font=("Arial", 15))
settingsButton.place(x=1230, y=100)

# Scan Your Own Cube Label
scan_title = Label(root, text="Scan Your Own Cube")
scan_title.config(font=("Arial", 20))
scan_title.place(x=1110, y=150)

# Scan Cube Button
scanCube_button = Button(root, text="Scan Cube", command=lambda: scanCube())
scanCube_button.config(font=("Arial", 15))
scanCube_button.place(x=1160, y=180)


# Edit Mode Label
edit_mode_label = Label(root, text="Edit Mode Activated")
edit_mode_label.config(font=("Arial", 20), fg="white", bg="black")

# Edit Digital Cube
edit_cube_title = Label(root, text="Edit This Cube")
edit_cube_title.config(font=("Arial", 20))
edit_cube_title.place(x=1142, y=350)
edit_cube_button = Button(root, text="Enter Edit Mode", command=lambda: editMode(edit_mode_label, edit_cube_button))
edit_cube_button.place(x=1150, y=380)

# Perform Move
move_title = Label(root, text="Make Your Own Move")
move_title.config(font=("Arial", 20))
move_title.place(x=1110, y=230)

# Move Input
moveInput = Entry(root)
moveInput.place(x=1125, y=260)
moveInputButton = Button(root, text="Make Move", command=lambda: performAlgorithm(moveInput.get()))
moveInputButton.place(x=1160, y=290)
randomScrambleButton = Button(root, text="Random Scramble", command=lambda: generateScramble())
randomScrambleButton.place(x=1141, y=315)


# Edit Mode Cubes
white_color = cubeCanvas.create_rectangle(600, 600, 650, 650, width=0, fill='white', state="hidden", tag="edit_white")
red_color = cubeCanvas.create_rectangle(660, 600, 710, 650, width=0, fill='red', state="hidden", tag="edit_red")
blue_color = cubeCanvas.create_rectangle(720, 600, 770, 650, width=0, fill='blue', state="hidden", tag="edit_blue")
orange_color = cubeCanvas.create_rectangle(780, 600, 830, 650, width=0, fill='orange', state="hidden",
                                           tag="edit_orange")
green_color = cubeCanvas.create_rectangle(840, 600, 890, 650, width=0, fill='green', state="hidden", tag="edit_green")
yellow_color = cubeCanvas.create_rectangle(900, 600, 950, 650, width=0, fill='yellow', state="hidden",
                                           tag="edit_yellow")
cubeCanvas.tag_bind("edit_white", "<Button-1>", editColor)
cubeCanvas.tag_bind("edit_red", "<Button-1>", editColor)
cubeCanvas.tag_bind("edit_blue", "<Button-1>", editColor)
cubeCanvas.tag_bind("edit_orange", "<Button-1>", editColor)
cubeCanvas.tag_bind("edit_green", "<Button-1>", editColor)
cubeCanvas.tag_bind("edit_yellow", "<Button-1>", editColor)



# Solve Text
solve_text = StringVar()
solve_text.set("Your Solving Algorithm Will Appear Here")
scramble_label = Label(root, wraplength=200, textvariable=solve_text)
scramble_label.place(x=1130, y=420)



solveButton = Button(root, text="Solve Cube", command=lambda: solveCube())
solveButton.config(font=("Arial", 15))
solveButton.place(x=1110, y=700)

resetButton = Button(root, text="Reset Cube", command=lambda: updateCube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR"))
resetButton.config(font=("Arial", 15))
resetButton.place(x=1220, y=700)

root.resizable(False, False)
root.mainloop()
