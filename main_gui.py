import random
from rubik.cube import Cube
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
from tkmacosx import Button as btn
import pygame
import webbrowser

# Importing My code for solver and scanner
from CubeScanner import CubeScanner
from Solver import SolveCube

# Initilise pygame (used for playing audio)
pygame.mixer.init()

# Global Variables
# This variable controls how the cube looks through out the program, and how it is mapped onto the digital cube.
current_cube = Cube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
# Variable for whether the user is using edit mode
edit_mode = False
# Variable for selecting which colour you want in edit mode
current_color = " "
# Variable for whether dark mode is active or not.
dark_mode_active = False
# Variable for mute being active or disabled
mute_active = False

# Initialise root TK
root = Tk()
# These next lines define size, position and title of tkinter window
root.geometry('1400x740+10+10')
# Title of Tkinter Window
root.title("Cube Solver")

# Main frame with buttons & content on.
mainFrame = Frame(root, width=200, height=200)
mainFrame.grid(row=0, column=0, padx=10, pady=2)
# Setting up canvas for digital cube to be printed on
cubeCanvas = Canvas(mainFrame, width=1000, height=720, bg='black', bd=0, highlightthickness=0,
                    borderwidth=0, highlightbackground="#232323")
cubeCanvas.grid(row=0, column=0, padx=0, pady=0)


##########################################################################################
# Open Quickstart
##########################################################################################
def openQuickStart():
    quickStart = Toplevel(root)
    # sets the title of the top level widget
    quickStart.title("Getting Started")
    # sets the geometry of toplevel
    quickStart.geometry("800x740")
    # Declaring notebook
    my_notebook = ttk.Notebook(quickStart)
    my_notebook.pack()

    # Declaring Each tab
    # Getting Started
    getting_started = Frame(my_notebook, width=800, height=400)
    getting_started.pack()
    # Cube Scanner
    cube_scanner = Frame(my_notebook, width=800, height=400)
    cube_scanner.pack()
    # Cube Notation
    cube_notation = Frame(my_notebook, width=800, height=400)
    cube_notation.pack()
    # Drawing / Editing Your Cube
    drawing_cube = Frame(my_notebook, width=800, height=400)
    drawing_cube.pack()
    # Solving the Cube
    solving_options = Frame(my_notebook, width=800, height=400)
    solving_options.pack()

    # Adding the different tabs
    my_notebook.add(getting_started, text='Getting Started')
    my_notebook.add(cube_scanner, text='Scan Your Cube')
    my_notebook.add(cube_notation, text='Cube Notation')
    my_notebook.add(drawing_cube, text='Draw Your Cube')
    my_notebook.add(solving_options, text='Solving Your Cube')

    # Different Pages

    # Getting Started Page:

    getting_started_title = Label(getting_started, text=" \n Getting Started \n").pack()
    # Main Text
    # Use open() to load the text
    p1 = open("Text/Getting Started/gettingstarted.txt")
    # Read the file, and store it in a variable
    p1_content = p1.read()
    # Create the label, and pack() it on getting_started screen
    para1 = Label(getting_started, text=p1_content).pack()

    # Load this pages image
    main_app_image = PhotoImage(file='Images/Getting Started Images/Getting Started/main_app_photo.gif')
    # Create a label for the image
    image_label = Label(getting_started, image=main_app_image)
    # Store a copy of the image in memory
    image_label.photo = main_app_image
    # Pack() the label on screen
    image_label.pack()

    # Scanning Your Cube
    cube_scanner_title = Label(cube_scanner, text="\n Scanning Your Own Cube \n ").pack()
    scanner_p1 = open("Text/Scan Your Cube/scanningcube.txt")
    scanner_p1_content = scanner_p1.read()
    Label(cube_scanner, text=scanner_p1_content).pack()

    cube_scanner_image = PhotoImage(file="Images/Getting Started Images/Cube Scanner/cube_scanner__image.gif")
    scanner_image_label = Label(cube_scanner, image=cube_scanner_image)
    scanner_image_label.photo = cube_scanner_image
    scanner_image_label.pack()

    # Cube Notation1400
    cube_notation_title = Label(cube_notation, text="\n Cube Notation\n ").pack()
    notation_p1 = open("Text/Cube Notation/cubenotation.txt")
    notation_p1_content = notation_p1.read()
    Label(cube_notation, text=notation_p1_content).pack()

    # Images
    cube_notation_images = PhotoImage(file="Images/Getting Started Images/Notation/cube_notation_image.gif")
    cube_notation_image_label = Label(cube_notation, image=cube_notation_images)
    cube_notation_image_label.photo = cube_notation_images
    cube_notation_image_label.pack()

    # Para 2
    notation_p2 = open("Text/Cube Notation/cubenotation_para2.txt")
    notation_p2_content = notation_p2.read()
    Label(cube_notation, text=notation_p2_content).pack()

    # Drawing Your Cube
    drawing_cube_title = Label(drawing_cube, text="\n Drawing Your Cube Digitally\n ").pack()
    edit_cube_image = PhotoImage(file="Images/Getting Started Images/Edit Cube/draw_cube.gif")
    edit_cube_image_label = Label(drawing_cube, image=edit_cube_image)
    edit_cube_image_label.photo = edit_cube_image
    edit_cube_image_label.pack()

    drawing_cube_p1 = open("Text/Drawing Your Cube/drawingcube.txt")
    drawing_cube_p1_content = drawing_cube_p1.read()
    Label(drawing_cube, text=drawing_cube_p1_content).pack()

    # Solving Your Cube
    solving_options_title = Label(solving_options, text="\n Solving Your Cube\n ").pack()

    solving_cube_p1 = open("Text/Solving/solving.txt")
    solving_cube_p1_content = solving_cube_p1.read()
    Label(solving_options, text=solving_cube_p1_content).pack()

    solving_cube_image = PhotoImage(file="Images/Getting Started Images/Solving Cube/step-by-step.gif")
    solving_cube_image_label = Label(solving_options, image=solving_cube_image)
    solving_cube_image_label.photo = solving_cube_image
    solving_cube_image_label.pack()

    solving_cube_p2 = open("Text/Solving/solving_para2.txt")
    solving_cube_p2_content = solving_cube_p2.read()
    Label(solving_options, text=solving_cube_p2_content).pack()

    solving_cube_image2 = PhotoImage(file="Images/Getting Started Images/Solving Cube/full_solve.gif")
    solving_cube_image_label2 = Label(solving_options, image=solving_cube_image2)
    solving_cube_image_label2.photo = solving_cube_image2
    solving_cube_image_label2.pack()

    quickStart.resizable(False, False)


##########################################################################################
# Settings
##########################################################################################
def mute():
    # Get Global mute_active variable
    global mute_active
    # Set mute_active to True
    mute_active = True


def unMute():
    # Get Global mute_active variable
    global mute_active
    # Set mute_active to False
    mute_active = False


def openSettings():
    # Top level object which will be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the top level widget
    newWindow.title("Settings")

    # sets the geometry of top level
    newWindow.geometry("400x400")

    # Creating a canvas to add text and images too
    settings_canvas = Canvas(newWindow, width=400, height=400)
    settings_canvas.grid(row=0, column=0, padx=0, pady=0)

    # Finding Image
    cube_image = PhotoImage(file='Images/cube_icon.gif')
    # Creating a label of this image
    image_label = Label(settings_canvas, image=cube_image)
    # Keeping a copy of the image in memory
    image_label.photo = cube_image
    # Placing the image
    image_label.place(x=148, y=0)

    # Mode Label
    mode_label = Label(settings_canvas, text=" Mode")
    mode_label.config(font=("Arial", 20))
    mode_label.place(x=165, y=105)

    # Dark Mode Button
    mode_dark = btn(settings_canvas, text="Dark Mode", command=lambda: theme_dark(), bg="#EEEEEE", fg="#000",
                    highlightbackground="white")
    mode_dark.config(font=("Arial", 15))
    mode_dark.place(x=95, y=140)

    # Light Mode Button
    mode_light = btn(settings_canvas, text="Light Mode", command=lambda: theme_light(), bg="#EEEEEE", fg="#000",
                     highlightbackground="white")
    mode_light.config(font=("Arial", 15))
    mode_light.place(x=200, y=140)

    # Sound Label
    sound_label = Label(settings_canvas, text=" Sound: ")
    sound_label.config(font=("Arial", 20))
    sound_label.place(x=160, y=185)

    # Mute Button
    mute_button = btn(settings_canvas, text="Mute Sound", command=lambda: mute(), bg="#EEEEEE", fg="#000",
                      highlightbackground="white")
    mute_button.config(font=("Arial", 15))
    mute_button.place(x=85, y=220)

    # Un-mute button
    unmute_button = btn(settings_canvas, text="Unmute Sound", command=lambda: unMute(), bg="#EEEEEE", fg="#000",
                        highlightbackground="white")
    unmute_button.config(font=("Arial", 15))
    unmute_button.place(x=200, y=220)

    # Options Label
    close_label = Label(settings_canvas, text="Config & Links")
    close_label.config(font=("Arial", 20))
    close_label.place(x=130, y=270)

    # Close App Button
    close_app_button = btn(settings_canvas, text="Close App", command=lambda: root.destroy(), bg="#EEEEEE", fg="#000",
                           highlightbackground="white")
    close_app_button.config(font=("Arial", 15))
    close_app_button.place(x=153, y=305)

    # Link to github button
    github_button = btn(settings_canvas, text="Git-Hub",
                        command=lambda: webbrowser.open('https://github.com/ryanjewsburyMMU/Rubiks-Cube-Solver'),
                        bg="#EEEEEE", fg="#000", highlightbackground="white")
    github_button.config(font=("Arial", 15))
    github_button.place(x=160, y=340)

    def theme_dark():
        # Declare colours to use throughout dark mode
        main_bg = "#232323"
        listbox_bg = "#2E2E2E"
        button_bg = "#BB86FC"
        button_fg = "#fff"
        button_outer = "#2E2E2E"
        text_bg = "#232323"
        text_fg = "#fff"

        # Background
        root.configure(background=main_bg)
        solve_listbox.config(bg=listbox_bg, fg=button_bg)
        # Text & Labels
        title.config(bg=text_bg, fg=text_fg)
        subTitle.config(bg=text_bg, fg=text_fg)
        scan_title.config(bg=text_bg, fg=text_fg)
        edit_mode_label.config(bg=text_bg, fg=text_fg)
        scramble_label.config(bg=text_bg, fg=text_fg)
        move_title.config(bg=text_bg, fg=text_fg)
        edit_cube_title.config(bg=text_bg, fg=text_fg)
        # Buttons & Input
        settingsButton.config(bg=button_bg, fg=button_fg, highlightbackground=button_outer)
        quickStartButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        scanCube_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        edit_cube_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        moveInputButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        solveButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        resetButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        randomScrambleButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        sbsButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        moveInput.config(highlightbackground=main_bg, fg=button_fg, bg=listbox_bg)

        # Settings Screen
        # Background
        newWindow.configure(background='#232323')
        settings_canvas.config(bg="#232323", bd=0, highlightthickness=0, borderwidth=0, highlightbackground="#232323")
        # Images
        image_label.config(bg="#232323")
        # Text & Labels
        mode_label.config(bg="#232323", fg="#fff")
        sound_label.config(bg="#232323", fg="#fff")
        close_label.config(bg="#232323", fg="#fff")
        # Buttons
        mode_dark.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        mode_light.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        mute_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        unmute_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        close_app_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        github_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)

    def theme_light():
        # Declare colours to use throughout light mode
        main_bg = "#ffffff"
        listbox_bg = "#ffffff"
        button_bg = "#EEEEEE"
        button_fg = "#000"
        button_outer = "white"
        text_bg = "#ffffff"
        text_fg = "#000"
        white_color = '#ffffff'

        # Background
        root.configure(background=main_bg)
        solve_listbox.config(bg=listbox_bg, fg=white_color)
        # Text & Labels
        title.config(bg=text_bg, fg=text_fg)
        subTitle.config(bg=text_bg, fg=text_fg)
        scan_title.config(bg=text_bg, fg=text_fg)
        edit_mode_label.config(bg=text_bg, fg=text_fg)
        scramble_label.config(bg=text_bg, fg=text_fg)
        move_title.config(bg=text_bg, fg=text_fg)
        edit_cube_title.config(bg=text_bg, fg=text_fg)
        # Buttons & Input

        settingsButton.config(bg=button_bg, fg=button_fg, highlightbackground=button_outer)
        quickStartButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        scanCube_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        edit_cube_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        moveInputButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        solveButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        resetButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        randomScrambleButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        sbsButton.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        moveInput.config(highlightbackground=main_bg, fg=button_fg, bg=listbox_bg)

        # Settings Screen
        # Background
        newWindow.configure(background=main_bg)
        settings_canvas.config(bg=main_bg, bd=0, highlightthickness=0, borderwidth=0, highlightbackground=main_bg)
        # Images
        image_label.config(bg=main_bg)
        # Text & Labels
        mode_label.config(bg=text_bg, fg=text_fg)
        sound_label.config(bg=text_bg, fg=text_fg)
        close_label.config(bg=text_bg, fg=text_fg)
        # Buttons
        mode_dark.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        mode_light.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        mute_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        unmute_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        close_app_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)
        github_button.config(highlightbackground=button_outer, fg=button_fg, bg=button_bg)

    newWindow.grab_set()


##########################################################################################
# Scan Your Own Cube
##########################################################################################
def scanCube():
    c = CubeScanner()
    fullcube = c.scan()
    if fullcube is None:
        return None
    else:
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
        updateCube(cube_string)
        updateCubeColours()


##########################################################################################
# Making Moves On The Cube and Updating the Canvas
##########################################################################################
# Takes a letter from current_cube e.g. 'o' and coverts to Orange
# Usage is for converting rectangle to same colour as current_cube
def colourFromLetter(value):
    try:
        colors = {'G': 'green', 'R': 'red', 'B': 'blue', 'O': 'orange', 'W': 'White', 'Y': 'Yellow'}
        return colors[value]
    except:
        messagebox.showinfo("Error", "There was an error converting the notation")
        return None


# Converts Rectangle To Color Letter (uses tag)
# For example, to be used as green_00's colour = 'g'
def letterFromColour(tag):
    color = cubeCanvas.itemcget(tag, "fill")
    options = {"red": "R", "White": "W", "Yellow": "Y", "orange": "O", "blue": "B", "green": "G"}
    return str(options.get(color))


# Updates cube colours from current_cube
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


# Plays a random cube sound
def play():
    # Pick a number between 1 and 12 (amount of audio files in directory)
    file_num = random.randrange(1, 12)
    # Create a file string, with the file being "move_file_num" - e.g. move_10
    file = ("SoundEffects/Cube Moves/move_" + str(file_num) + ".mp3")
    # Play the file
    pygame.mixer.music.load(file)
    # Don't loop
    pygame.mixer.music.play(loops=0)


# Given a string of notation, will perform a each move on the cube
def performAlgorithm(algo):
    approved_moves = ["F", "Fi", "R", "Ri", "L", "Li", "U", "Ui", "B", "Bi", "D", "Di", "M", "Mi"]

    if edit_mode:
        messagebox.showinfo("Edit Mode", "Please Leave Edit Mode")
    else:
        # Split the algorithm into moves
        for move in algo.split():
            try:
                # Check if the move can be done (list of approved moves)
                if move in approved_moves:
                    # Plays Sound if Not muted
                    if not mute_active:
                        play()
                    else:
                        pass
                    # Make a move on current_cube
                    current_cube.sequence(move)
                    # Update the cube colours to make changes to digital cube
                    cubeCanvas.after(150, updateCubeColours())
                    # Update canvas to show user the changes
                    cubeCanvas.update_idletasks()
                # If move cannot be done (is not in approved moves)
                elif move not in approved_moves:
                    # Show an error
                    messagebox.showerror("Move Not Allowed", "Cannot make move " + str(move))
            except:
                # Print an error if anything goes wrong
                messagebox.showerror("Move Error", "Cannot make move " + str(move))


def generateScramble():
    notation = [" R ", " U ", " F ", " L ", " B ", " D ", " Ri ", " Ui ", " Fi ", " Li ", " Bi ", " Di "]
    scramble = " "
    solve_listbox.delete(0, 'end')
    for i in range(0, 30):
        current_move = str(notation[random.randrange(0, 12)])
        print(current_move)
        scramble += current_move
        solve_listbox.insert(END, "Move " + str(i + 1) + ": " + current_move)
    performAlgorithm(scramble)


##########################################################################################
# Editing Current Cube
##########################################################################################
# Updates cube  with new colors - to be used in editMode
def updateCube(newCubeString):
    global current_cube
    current_cube = Cube(newCubeString)
    updateCubeColours()
    cubeCanvas.update_idletasks()


# This is called when user clicks edit mode
def editMode(edit_mode_label, edit_cube_button):
    # Get global variables
    global edit_mode, current_cube
    # Update Cube Canvas whenever edit mode is clicked
    cubeCanvas.update_idletasks()
    # When edit mode is clicked, inverse the global edit_mode boolean
    edit_mode = not edit_mode
    if edit_mode:
        # User is entering edit mode
        # Change button text to Leave Edit Mode
        edit_cube_button.config(text="Leave Edit Mode")
        # Place 'Edit Mode' on top left of screen
        edit_mode_label.place(x=30, y=20)
        # Reveal all colours for users to click on
        cubeCanvas.itemconfigure(white_color, state='normal')
        cubeCanvas.itemconfigure(red_color, state='normal')
        cubeCanvas.itemconfigure(blue_color, state='normal')
        cubeCanvas.itemconfigure(green_color, state='normal')
        cubeCanvas.itemconfigure(orange_color, state='normal')
        cubeCanvas.itemconfigure(yellow_color, state='normal')
        # Update the global cube string with any changes
        updateCube(flattenCube())
    else:
        # User is leaving edit mode
        # Change button text to Enter Edit Mode
        edit_cube_button.config(text="Enter Edit Mode")
        # Remove Edit Mode text from screen
        edit_mode_label.place(x=-40, y=-40)
        # Hide all colours so users cannot interact with them
        cubeCanvas.itemconfigure(white_color, state='hidden')
        cubeCanvas.itemconfigure(red_color, state='hidden')
        cubeCanvas.itemconfigure(blue_color, state='hidden')
        cubeCanvas.itemconfigure(green_color, state='hidden')
        cubeCanvas.itemconfigure(orange_color, state='hidden')
        cubeCanvas.itemconfigure(yellow_color, state='hidden')
        # Update the global cube string with any changes
        updateCube(flattenCube())
    # Inverse the edit_mode boolean to leave / enter edit mode.
    return not edit_mode


def editColor(event):
    # Get the global variables, for edit mode and the current colour
    global current_color, edit_mode
    if edit_mode:
        # If edit mode has been activated and there is no current colour
        # Set current colour to white as default
        if current_color == " ":
            current_color = "white"

        # Options refers to the 6 intractable rectangles that appear when in edit mode.

        # Initialise dictionary of colours, based on their numerical values (amount of rectangles on screen)
        # Each rectangle is auto assigned a value (57 = blue (57th rectangle on screen))
        options = {55: "White", 56: "red", 57: "blue", 58: "orange", 59: "green", 60: "Yellow"}
        # Find which colour has been selected
        if event.widget.find_withtag("current")[0] in options:
            # Set current_colour to the the selected colour
            current_color = options.get(event.widget.find_withtag("current")[0])
            # Print to user for debugging
            print("Current Color = " + str(current_color))
        # If you selected another rectangle not in the options - by process of elimination this means you have
        # Selected a rectangle from within the cube.
        else:
            print("You clicked " + str(event))
            print("Current Color = " + str(current_color))
            # Take the 'current' rectangle selected on the cube
            current = event.widget.find_withtag("current")[0]
            # Set the 'current' rectangle, to the 'current_color' which is the one you selected from the
            # bottom options...
            event.widget.itemconfig(current, fill=current_color)
    else:
        # If not in edit mode, don't do anything if users click anything.
        pass


##########################################################################################
# Solving Algorithm (Full and Step-By-Step)
##########################################################################################
# Takes the values from each index and returns a string...
# This will then be used with the solver.
# "Flattens digital cube into cube string"
def flattenCube():
    cube_string = ""
    # First Layer
    # Concat a string based on the colour of each rectang;e/
    cube_string += str(letterFromColour(orange_00) + letterFromColour(orange_01) + letterFromColour(orange_02)
                       + letterFromColour(orange_10) + letterFromColour(orange_11) + letterFromColour(
        orange_12) + letterFromColour(orange_20)
                       + letterFromColour(orange_21) + letterFromColour(orange_22))

    # Second Layer
    cube_string += str(letterFromColour(green_00) + letterFromColour(green_01) + letterFromColour(green_02)
                       + letterFromColour(white_00) + letterFromColour(white_01) + letterFromColour(
        white_02) + letterFromColour(blue_00)
                       + letterFromColour(blue_01) + letterFromColour(blue_02) + letterFromColour(
        yellow_00) + letterFromColour(yellow_01)
                       + letterFromColour(yellow_02))

    # Third Layer
    cube_string += str(letterFromColour(green_10) + letterFromColour(green_11) + letterFromColour(green_12)
                       + letterFromColour(white_10) + letterFromColour(white_11) + letterFromColour(
        white_12) + letterFromColour(blue_10)
                       + letterFromColour(blue_11) + letterFromColour(blue_12) + letterFromColour(
        yellow_10) + letterFromColour(yellow_11)
                       + letterFromColour(yellow_12))

    # Fourth Layer
    cube_string += str(letterFromColour(green_20) + letterFromColour(green_21) + letterFromColour(green_22)
                       + letterFromColour(white_20) + letterFromColour(white_21) + letterFromColour(
        white_22) + letterFromColour(blue_20)
                       + letterFromColour(blue_21) + letterFromColour(blue_22) + letterFromColour(
        yellow_20) + letterFromColour(yellow_21)
                       + letterFromColour(yellow_22))

    # Final Layer
    cube_string += str(
        letterFromColour(red_00) + letterFromColour(red_01) + letterFromColour(red_02) + letterFromColour(red_10)
        + letterFromColour(red_11) + letterFromColour(red_12) + letterFromColour(red_20) + letterFromColour(
            red_21) + letterFromColour(red_22))

    return cube_string


# Converts Notation to Words for better understanding (step by step solve)
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
        "M": "Middle Layer Down",
        "Mi": "Middle Layer Up"
    }
    return notation.get(move)


def checkSolvable(cube_string):
    # Colours to check for
    cube_colors = ["O", "W", "R", "G", "B", "Y"]
    # Count of each colour
    color_count = []
    # Loop through all the colours
    for i in range(len(cube_colors)):
        color_count.append(str(cube_string.count(cube_colors[i])))
    # Check all numbers in colour_count match (9 is only possible amount to satisfy condition)
    if all(x == color_count[0] for x in color_count):
        # Cube has 9 of each colour
        return True
    else:
        # If not there is more or less of some colours - so print the colour count for debugging
        print(color_count)
        return False


def solveCube():
    global current_cube
    # Check if user is in edit mode, if they are don't start out the solve
    if edit_mode:
        messagebox.showinfo("Edit Mode", "Please Leave Edit Mode")
        pass
    # If not in edit mode, begin solve
    else:
        # Create a new string, with the current cube flattened into a string.
        new_cube = Cube(flattenCube())
        # Check if this cube is already solved
        if new_cube.is_solved():
            # If it is, return a message box to inform the user
            messagebox.showinfo("Cube Solved", "This cube is already solved!")
            pass
        else:
            # Check there are equal colours across the cube
            if checkSolvable(flattenCube()):
                # Initilise the sovler
                solver = SolveCube(new_cube)
                # Store the solving algorithm in variable algo
                algo = solver.solveCube()
                # If the algo is None, the cube is unsolvable, and the method will return an error.
                if algo == None:
                    messagebox.showerror(title="Cube Unsolvable", message="This cube cannot be solved,"
                                                                          " - Please double check your cube "
                                                                          "/ the digital on-screen cube")
                # If the cube is solvable
                else:
                    # Clear the list box
                    solve_listbox.delete(0, 'end')
                    # Perform the algorithm
                    performAlgorithm(algo[0])
                    # Filling the list box with each move
                    move_num = 0
                    for i in algo[0].split():
                        move_num += 1
                        solve_listbox.insert(END, "Move " + str(move_num) + ": " + i)
            else:
                # If the cubes colours across the cube are not all equal to 9 - inform the user
                messagebox.showerror("Cube Unsolvable", "Please ensure there are 9 of each colour on the cube.")


# Controls button press for step by step solve
def stepByStepSolve():
    # Validation and solver the same as solveCube method
    global current_cube
    if edit_mode:
        messagebox.showinfo("Edit Mode", "Please Leave Edit Mode")
    else:
        new_cube = Cube(flattenCube())
        if new_cube.is_solved():
            messagebox.showinfo("Cube Solved", "This cube is already solved!")
        else:
            if checkSolvable(flattenCube()):
                solver = SolveCube(new_cube)
                algo = solver.solveCube()
                if algo is None:
                    messagebox.showerror(title="Cube Unsolvable", message="This cube cannot be solved, - "
                                                                          "Please double check your cube "
                                                                          "/ the digital on-screen cube")
                else:
                    # Difference is here, instead of performAlgorithm()
                    solve_listbox.delete(0, 'end')
                    # We call sbsSolve with the algorithm as a param, guiding the user through the solve.
                    sbsSolve(algo[0])
            else:
                messagebox.showerror("Cube Unsolvable", "Please ensure there are 9 of each colour on the cube.")


# Displays UI for step by step solve
def sbsSolve(algo):
    # Step By Step Solve
    # Create a new window using TopLevel
    stepSolve = Toplevel(root)
    # sets the title of the Toplevel widget
    stepSolve.title("Step By Step Solve")
    # sets the geometry of toplevel
    stepSolve.geometry("450x180")

    algo_list = []
    algo_num = 0
    algo_num_list = []
    # Convert Algorithm to list
    for i in algo.split():
        # Add moves to list one at a time
        algo_list.append(i)
        # Add move number to a list one at a time
        algo_num += 1
        # Create list of move numbers
        algo_num_list.append(algo_num)

    # Convert Both Lists to Iterable
    num_iter = iter(algo_num_list)
    algo_iter = iter(algo_list)

    # Labels and Buttons
    title_label = Label(stepSolve, text="Step by Step Solve")
    title_label.config(font=("Arial", 20))
    title_label.place(x=50, y=5)

    instructions = StringVar()
    instructions.set("Important: Please hold the cube with the White face facing you")
    instructions_label = Label(stepSolve, textvariable=instructions)
    instructions_label.place(x=50, y=35)

    instructions_2 = StringVar()
    instructions_2.set("and the Orange face, facing upwards")
    instructions_label_2 = Label(stepSolve, textvariable=instructions_2)
    instructions_label_2.place(x=50, y=55)

    move = StringVar()
    move.set("Move: ")
    move_label = Label(stepSolve, wraplength=200, textvariable=move)
    move_label.place(x=50, y=80)

    clear_move = StringVar()
    clear_move.set("Word:")
    clear_move_label = Label(stepSolve, wraplength=200, textvariable=clear_move)
    clear_move_label.place(x=50, y=110)

    num_move = StringVar()
    num_move.set("Num: ")
    num_move_label = Label(stepSolve, wraplength=200, textvariable=num_move)
    num_move_label.place(x=50, y=140)

    nextMoveButton = Button(stepSolve, text="Next Move", command=lambda: nextMove(algo_iter, num_iter))
    nextMoveButton.place(x=340, y=130)

    # Function Hierarchy

    # Next Move Button Functionality
    def nextMove(algo_iter, num_iter):
        try:
            # Set next_move equal to the next value in the algo_itter
            next_move = next(algo_iter)
            # Do the same for the move number / amount
            move_number = next(num_iter)
            # Update Listbox with current move
            solve_listbox.insert(END, "Move " + str(move_number) + ": " + next_move)
            # Set text to next move and move number
            move.set("Move: " + str(next_move))
            clear_move.set("Word: " + notationToMove(str(next_move)))
            num_move.set("Num: " + str(move_number) + " / " + str(len(algo_list)))
            performAlgorithm(str(next_move))
        except:
            # If you cannot make any more moves - then we have reached the end
            move.set("Move: There are no more moves.")
            clear_move.set("Word: There are no more moves.")


##########################################################################################
# Resetting Cube
##########################################################################################
def resetCube():
    # Makes use of the updateCube method, to convert the cube into a solved state
    updateCube("OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR")
    # Clears the solve list box
    solve_listbox.delete(0, 'end')


# Declaring individual rectangles for each index on a particular face.
# Green Face (Layer 1)
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
# Each cube index is bound with the editColor method, this allows us to change this particular rectangles
# Colour in edit mode.
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
title = Label(root, text="Rubik's Cube Solver")
title.config(font=("Courier", 30))
title.place(x=1040, y=30)

# Label For Subtitle
subTitle = Label(root, text="Project by Ryan Jewsbury")
subTitle.config(font=("Arial", 20))
subTitle.place(x=1090, y=60)

# More Information Button
quickStartButton = btn(root, text="Quick Start", command=lambda: openQuickStart(), bg="#45b6fe", fg="#000",
                       highlightbackground="white")
quickStartButton.config(font=("Arial", 15))
quickStartButton.place(x=1100, y=100)

# Settings Button
settingsButton = btn(root, text="Settings", command=lambda: openSettings(), bg="#EEEEEE", fg="#000",
                     highlightbackground="white")
settingsButton.config(font=("Arial", 15))
settingsButton.place(x=1230, y=100)

# Scan Your Own Cube Label

# SCAN YOUR CUBE..
scan_title = Label(root, text="Scan Your Own Cube")
scan_title.config(font=("Arial", 20))
scan_title.place(x=1110, y=150)

# Scan Cube Button
scanCube_button = btn(root, text="Scan Cube", command=lambda: scanCube(), bg="#EEEEEE", fg="#000",
                      highlightbackground="white")
scanCube_button.config(font=("Arial", 15))
scanCube_button.place(x=1160, y=180)

# Edit Mode Label
edit_mode_label = Label(root, text="Edit Mode Activated")
edit_mode_label.config(font=("Arial", 20), fg="white", bg="black")

# Edit Digital Cube
edit_cube_title = Label(root, text="Edit This Cube")
edit_cube_title.config(font=("Arial", 20))
edit_cube_title.place(x=1142, y=350)
edit_cube_button = btn(root, text="Enter Edit Mode", command=lambda: editMode(edit_mode_label, edit_cube_button),
                       bg="#EEEEEE", fg="#000", highlightbackground="white")
edit_cube_button.place(x=1150, y=380)

# Perform Move
move_title = Label(root, text="Make Your Own Move")
move_title.config(font=("Arial", 20))
move_title.place(x=1110, y=230)

# Move Input
moveInput = Entry(root)
moveInput.place(x=1125, y=260)

# Buttons for move input, and random scramble generator.
moveInputButton = btn(root, text="Make Move", command=lambda: performAlgorithm(moveInput.get()), bg="#EEEEEE",
                      fg="#000", highlightbackground="white")
moveInputButton.place(x=1160, y=290)
randomScrambleButton = btn(root, text="Random Scramble", command=lambda: generateScramble(), bg="#EEEEEE", fg="#000",
                           highlightbackground="white")
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

# Listbox to display solving algorithm
solve_listbox = Listbox(root)
solve_listbox.place(x=1137, y=480)

sbsButton = btn(root, text="Step By Step Solve", command=lambda: stepByStepSolve(), bg="#EEEEEE", fg="#000",
                highlightbackground="white")
sbsButton.config(font=("Arial", 15))
sbsButton.place(x=1140, y=670)

solveButton = btn(root, text="Solve Cube", command=lambda: solveCube(), bg="#EEEEEE", fg="#000",
                  highlightbackground="white")
solveButton.config(font=("Arial", 15))
solveButton.place(x=1110, y=700)

resetButton = btn(root, text="Reset Cube", command=lambda: resetCube(), bg="#EEEEEE", fg="#000",
                  highlightbackground="white")
resetButton.config(font=("Arial", 15))
resetButton.place(x=1220, y=700)

# Make Root Window Not Resizable
root.resizable(False, False)
root.mainloop()






