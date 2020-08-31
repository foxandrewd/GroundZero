import tkinter as tk  # Import the TKinter library/module so we can use it
DEBUG_LVL = 3
root = tk.Tk()  # Create the top-level Window object. It's not displayed yet, though!

Player = "X"

gameboard_state = [ ['','',''],       # A blank (starting) gameboard state
                    ['','',''],
                    ['','',''] ]

def newgame_clear_board(gameboard_state):
    for i in range(3):
        for j in range(3):
            gameboard_state[i][j] = ''
    return gameboard_state
  
def move_is_valid(gameboard_state, row, col):
  if gameboard_state[row][col] == '':
    return True
  else:
    return False

def update_gameboard_state(gameboard_state, player, row, col):
  gameboard_state[row][col] = player


buttons = { 0:{0:None,1:None,2:None}, 1:{0:None,1:None,2:None}, 2:{0:None,1:None,2:None} }
button_pos = {}

# Make a 2D array of buttons
for rowN in range(3):
    for colN in range(3):
        button = tk.Button(root, text = "", height=3, width=6, command = lambda r=rowN, c=colN: doStuffOnClick(r,c) )
        button.grid(row=rowN, column=colN)      # Place this new button into the current TKinter grid layout
        buttons[rowN][colN] = button            # Save this new button into the "buttons" List variable
        button_pos[button] = (rowN, colN)       # Save the position of this button into the "button_pos" Dict
        if DEBUG_LVL >= 2: print(button , button_pos[button])      # Show the button's name and its position
    #endfor colN
#endfor rowN

# Print out some helpful information when we click on one of the buttons in the grid
def doStuffOnClick(r, c):
    theButton = buttons[r][c]
    if DEBUG_LVL >= 2: print("The button name/ID is: " + str(theButton) )
    theButtonPos = button_pos[theButton]
    (button_row, button_col) = button_pos[theButton]
    if DEBUG_LVL >= 2: print("Button Clicked was: Row=" + str(button_row) + \
          ", Column=" + str(button_col) )                        # Backslash ('\') lets you continue ur code statement on the next line
    if move_is_valid(gameboard_state, button_row, button_col):
        if DEBUG_LVL >= 1: print("That move looks Valid.")
        update_gameboard_state(gameboard_state, Player, button_row, button_col)
        (buttons[button_row][button_col])["text"] = Player
    else:
        if DEBUG_LVL >= 1: print("Invalid move. Someone already played that square.")

tk.mainloop()   # Run the TKinter Main GUI Program, i.e. show it on the screen.
