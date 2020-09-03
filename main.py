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

DEBUG_LVL = 0

root = tk.Tk()
root.title('Tic-Tac-Toe')
buttonFont = tkinter.font.Font(size=60, weight='bold')
labelsFont = tkinter.font.Font(size=18, weight='bold')

Player = "X"    # The player whose Turn it currently is (i.e., "X" or "O")

# Global variable integers to keep track of the number of X wins, O wins and draws:
num_X_wins = 0
num_O_wins = 0
num_draws  = 0

gameboard_state = [  ['','',''] ,       # A blank (starting) gameboard state
                     ['','',''] ,
                     ['','','']  ]

def newgame_clear_board(gameboard_state):
    """ Completely clear the state of all spots on the 3x3 GameBoard.
      We blank out all 3x3=9 cells in the gameboard_state data structure """
    for i in range(3):
        for j in range(3):
            gameboard_state[i][j] = ''    # Set the cell state equal to blank ( i.e., to the empty-string ('') )
    return gameboard_state
  
def newgame_clear_all_buttons_text(buttons):
    ## This function clears the ["text"] of all 9 tk.Button()'s in the GUI Game Board
    ## Note that the tk.Button()'s are all stored in the (parameter) variable 'buttons'
    for i in range(3):
        for j in range(3):
            (buttons[i][j])["text"] = ''    # Set the tk.Button text equal to blank ( i.e., to the empty-string ('') )
    return buttons
  
def move_is_valid(gameboard_state, row, col):
  """ Check if the move is valid or not. If the spot (row,col) on the
      GameBoard is clear/empty (i.e., equal to the empty string "")
      then this is a valid move for the current Player. Else, it's invalid.
      This function must return True if the move is valid, and must return
      False if the move is invalid.
  """
  if gameboard_state[row][col] == "":
    return True
  else:
    return False

def update_gameboard_state(gameboard_state, player, row, col):
    """ If player=="X", then store "X" at the correct position (i.e., (row,col) )
        in the 'gameboard_state' array variable
    """
    gameboard_state[row][col] = player

# This 'buttons' Dictionary (dict) is to contain references to each of the 3x3 = 9 TKinter Buttons in the GUI.
# We initialise them as blank/empty (i.e., None). We will put the actual Buttons
# into the correct slots during the Button construction double For-loop (see below).
buttons = {  0: {0:None, 1:None, 2:None} ,
             1: {0:None, 1:None, 2:None} ,
             2: {0:None, 1:None, 2:None}  }

# This 'button_pos' Dictionary (dict) will store the position of where each button is on the GameBoard.
# So the keys of this dict will be the Button's, and the values of this dict will be the (row,col) tuple
# specifying where that particular button is on the GameBoard.
button_pos = {}     # Begin as empty dict, we fill it out during the Button construction double For-loop directly below:

frame_turn = tk.Frame(root)
frame_turn.pack(side=tk.TOP)

label_turn = tk.Label(frame_turn, text="Current Player's Turn:  " + Player)
label_turn['font'] = labelsFont
label_turn.pack(side=tk.TOP)

frame_board = tk.Frame(root)
frame_board.pack(side=tk.TOP)


# This is the Button construction double For-loop
# Make the 3x3 array of 9 buttons, store each one of them into the correct slot in the 'buttons' variable we initialised above.
for rowN in range(3):
    for colN in range(3):
        button = tk.Button(frame_board, text = "", height=1, width=3, command = lambda r=rowN, c=colN: doStuffOnClick(r,c) )
        button['font'] = buttonFont
        button.grid(row=rowN, column=colN)      # Place this new button into the current TKinter grid layout
        buttons[rowN][colN] = button            # Save this new button into the "buttons" List variable
        button_pos[button] = (rowN, colN)       # Save the position of this button into the "button_pos" Dict
        if DEBUG_LVL >= 2: print(button , button_pos[button])      # Show the button's name and its position
    #endfor colN
#endfor rowN

# Function: 'doStuffOnClick'
# What to check and the procedure to follow when the current Player clicks one of the 9 Buttons.
def doStuffOnClick(r, c):
    global Player, num_X_wins, num_O_wins, num_draws
    theButton = buttons[r][c]
    if DEBUG_LVL >= 2: print("The button name/ID is: " + str(theButton) )
    (button_row, button_col) = button_pos[theButton]
    if DEBUG_LVL >= 2: print("Button Clicked was: Row=" + str(button_row) + \
          ", Column=" + str(button_col) )                        # Backslash ('\') lets you continue ur code statement on the next line
    if move_is_valid(gameboard_state, button_row, button_col):
        if DEBUG_LVL >= 1: print("That move looks Valid.")
        update_gameboard_state(gameboard_state, Player, button_row, button_col)
        (buttons[button_row][button_col])["text"] = Player
        if current_player_has_won(gameboard_state, Player):
            if Player =="X":
                num_X_wins += 1
                print("Num X wins: ", num_X_wins)
                print("Num O wins: ", num_O_wins)
                print("Num Draws : ", num_draws)
                messagebox.showinfo(message = "Player X won: Well done Player X!")
            else:
                num_O_wins += 1
                print("Num X wins: ", num_X_wins)
                print("Num O wins: ", num_O_wins)
                print("Num Draws : ", num_draws)
                messagebox.showinfo(message = "Player O won: Well done Player O!")
            # Clear the Board for the next Game    
            newgame_clear_board(gameboard_state)
            newgame_clear_all_buttons_text(buttons)
        if check_draw(gameboard_state):
            num_draws +=1
            print("Num X wins: ", num_X_wins)
            print("Num O wins: ", num_O_wins)
            print("Num Draws : ", num_draws)
            messagebox.showinfo(message = "Game was a Draw")
            # Clear the Board for the next Game
            newgame_clear_board(gameboard_state)
            newgame_clear_all_buttons_text(buttons)
            
        ## We needed to check if 'Player' has won the game - NB: there is a function in helpers.py that can do this called: current_player_has_won()
        ## Also needed to check if the game has been a Draw - NB: there is a function in helpers.py that can do this called: check_draw()
        
        ## If the game finished (i.e., if gameboard_is_full(gameboard_state) ), we needed to call the 'newgame_clear_board' function
        ## and we also needed to call the 'newgame_clear_all_buttons_text' function
        ## and we also needed to update num_X_wins, num_O_wins or num_draws
        
        # Swap the Player for the next turn:
        if Player == "X":
            Player = "O"
            label_turn["text"] = "Current Player's Turn:  " + Player
        else:
            Player = "X"
            label_turn["text"] = "Current Player's Turn:  " + Player
    else:
        if DEBUG_LVL >= 1: print("Invalid move. Someone already played that square.")

tk.mainloop()   # Run the TKinter Main GUI Program, i.e. show it on the screen.
