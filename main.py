# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:13:34 2020
@author: Andrew Fox
@author: Reuben Corrigan
"""

import tkinter as tk  # Import the TKinter library/module so we can use it
from tkinter import messagebox
import tkinter.font
from helpers import *

DEBUG_LVL = 11

root = tk.Tk()
root.title('Tic-Tac-Toe')
buttonFont = tkinter.font.Font(size=60, weight='bold')
labelsFont = tkinter.font.Font(size=18, weight='bold')

Player = "X"  # The player whose Turn it currently is (i.e., "X" or "O")

# Global variable integers to keep track of the number of X wins, O wins and draws:
num_X_wins = 0
num_O_wins = 0
num_draws = 0

gameboard_state = [['', '', ''],  # A blank (starting) gameboard state
                   ['', '', ''],
                   ['', '', '']]

# This 'buttons' Dictionary (dict) is to contain references to each of the 3x3 = 9 TKinter Buttons in the GUI.
# We initialise them as blank/empty (i.e., None). We will put the actual Buttons
# into the correct slots during the Button construction double For-loop (see below).
buttons = {0: {0: None, 1: None, 2: None},
           1: {0: None, 1: None, 2: None},
           2: {0: None, 1: None, 2: None}}

# This 'button_pos' Dictionary (dict) will store the position of where each button is on the GameBoard.
# So the keys of this dict will be the Button's, and the values of this dict will be the (row,col) tuple
# specifying where that particular button is on the GameBoard.
button_pos = {}  # Begin as empty dict, we fill it out during the Button construction double For-loop directly below:

frame_turn = tk.Frame(root)  # A frame that will hold ONLY the tk.Label that displays whose turn it is
frame_turn.pack(side=tk.TOP)  # This should be at the TOP of the 'root' window

label_turn = tk.Label(frame_turn,
                      text="Current Player's Turn:  " + Player)  # The label displaying whose turn. Its parent frame is 'frame_turn'.
label_turn[
    'font'] = labelsFont  # Make the font of this label equal to "labelsFont", which is defined earlier in this script.
label_turn.pack(side=tk.TOP)  # Add this label into its parent frame (i.e., into "frame_turn"). Pack it towards the TOP.

frame_board = tk.Frame(
    root)  # Make the tk.Frame that will hold the GameBoard (it will hold all 9 tk.Buttons's of the 3x3 grid)
frame_board.pack(
    side=tk.TOP)  # Add (i.e., "pack") this frame into its parent element. Its parent element is 'root' (the main window)

frame_wins = tk.Frame(root)
frame_wins.pack(side=tk.BOTTOM)

label_X = tk.Label(frame_wins,
                   text="X Wins: " + str(num_X_wins) + "  draws: " + str(num_draws) + "  O Wins: " + str(num_O_wins))
label_X.pack()
label_X['font'] = labelsFont
# This is the Button construction double For-loop
# Make the 3x3 array of 9 buttons, store each one of them into the correct slot in the 'buttons' variable we initialised above.
for rowN in range(3):
    for colN in range(3):
        button = tk.Button(frame_board, text="", height=1, width=3, command=lambda r=rowN, c=colN: doStuffOnClick(r, c))
        button['font'] = buttonFont
        button.grid(row=rowN, column=colN)  # Place this new button into the current TKinter grid layout
        buttons[rowN][colN] = button  # Save this new button into the "buttons" List variable
        button_pos[button] = (rowN, colN)  # Save the position of this button into the "button_pos" Dict
        if DEBUG_LVL >= 2: print(button, button_pos[button])  # Show the button's name and its position
    # endfor colN


# endfor rowN

# Function: 'doStuffOnClick'
# What to check and the procedure to follow when the current Player clicks one of the 9 Buttons.
def doStuffOnClick(r, c):
    global Player, num_X_wins, num_O_wins, num_draws
    theButton = buttons[r][c]
    if DEBUG_LVL >= 2: print("The button name/ID is: " + str(theButton))
    (button_row, button_col) = button_pos[theButton]
    if DEBUG_LVL >= 2: print("Button Clicked was: Row=" + str(button_row) + \
                             ", Column=" + str(
        button_col))  # Backslash ('\') lets you continue ur code statement on the next line
    if move_is_valid(gameboard_state, button_row, button_col):
        if DEBUG_LVL >= 1: print("That move looks Valid.")
        update_gameboard_state(gameboard_state, Player, button_row, button_col)
        buttons[button_row][button_col]["text"] = Player
        if current_player_has_won(gameboard_state, Player):
            if Player == "X":
                num_X_wins += 1
                print("Num X wins: ", num_X_wins);
                print("Num O wins: ", num_O_wins);
                print("Num Draws : ", num_draws)
                messagebox.showinfo(message="Player X won: Well done Player X!")
                label_X["text"] = "X Wins: " + str(num_X_wins) + "  draws: " + str(num_draws) + "  O Wins: " + str(
                    num_O_wins)
            else:
                num_O_wins += 1
                print("Num X wins: ", num_X_wins);
                print("Num O wins: ", num_O_wins);
                print("Num Draws : ", num_draws)
                messagebox.showinfo(message="Player O won: Well done Player O!")
                label_X["text"] = "X Wins: " + str(num_X_wins) + "  draws: " + str(num_draws) + "  O Wins: " + str(
                    num_O_wins)
                # Clear the Board for the next Game    
            newgame_clear_board(gameboard_state)
            newgame_clear_all_buttons_text(buttons)
        if check_draw(gameboard_state):
            num_draws += 1
            print("Num X wins: ", num_X_wins);
            print("Num O wins: ", num_O_wins);
            print("Num Draws : ", num_draws)
            messagebox.showinfo(message="Game was a Draw")
            label_X["text"] = "X Wins: " + str(num_X_wins) + "  draws: " + str(num_draws) + "  O Wins: " + str(
                num_O_wins)
            # Clear the Board for the next Game
            newgame_clear_board(gameboard_state)
            newgame_clear_all_buttons_text(buttons)

        """"
        # Above, we needed to check if 'Player' has won the game - NB: there is a function in helpers.py that can do this called: current_player_has_won(...)
        # Also needed to check if the game has been a Draw - NB: there is a function in helpers.py that can do this called: check_draw(...)

        # If the game finished (X wins, O wins or it's a Draw), we also needed to call the newgame_clear_board(...) function,
        # and we also needed to call the newgame_clear_all_buttons_text(...) function,
        # and we also needed to update num_X_wins, num_O_wins or num_draws appropriately
        """

        # Swap the Player for the next turn:
        if Player == "X":
            Player = "O"
            label_turn[
                "text"] = "Current Player's Turn:  " + Player  # Update the display label at the top showing whose turn it is
        else:
            Player = "X"
            label_turn[
                "text"] = "Current Player's Turn:  " + Player  # Update the display label at the top showing whose turn it is
    else:
        if DEBUG_LVL >= 1: print("Invalid move. Someone already played that square.")


tk.mainloop()  # Run the TKinter Main GUI Program, i.e. show it on the screen.
