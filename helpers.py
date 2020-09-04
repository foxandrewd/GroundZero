# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:22:26 2020
Project Zero - "GroundZero" project
Developers: Andrew Fox and Reuben Corrigan
@authors: Andrew Fox and Reuben Corrigan
"""

DEBUG = False

X_WIN_STRING = 'XXX'
O_WIN_STRING = 'OOO'

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

def gameboard_is_full(gameboard_state):
    """ Return True is the GameBoard is full, else return False"""
    for i in range(3):
        for j in range(3):
            if gameboard_state[i][j] == '': return False
    # If we have made it to this point without ever having returned False ('cos of a blank ('') gamesquare)
    # then that means that all 9 gamesquares were NON-blank. This means that the gameboard
    # is completely full of X's and O's. So, we should return True at this point. And that's what we do:
    return True

def X_has_won(gameboard_state):
    if check_row_win(gameboard_state)       == X_WIN_STRING \
       or check_column_win(gameboard_state) == X_WIN_STRING \
       or check_diag_win(gameboard_state)   == X_WIN_STRING:
        print("X won this game. Well done Player X !!!")   
        return True
    else:
        return False

def O_has_won(gameboard_state):
    if check_row_win(gameboard_state)       == O_WIN_STRING \
       or check_column_win(gameboard_state) == O_WIN_STRING \
       or check_diag_win(gameboard_state)   == O_WIN_STRING:
        print("O won this game. Well done Player O !!!")
        return True
    else:
        return False

def current_player_has_won(gameboard_state, player):
    if player == "X" and X_has_won(gameboard_state):
        return True
    elif player == "O" and O_has_won(gameboard_state):
        return True
    else:
        return False

def check_draw(gameboard_state):
    if gameboard_is_full(gameboard_state):
        if   X_has_won(gameboard_state): return False
        elif O_has_won(gameboard_state): return False
        else:
            print("This game was a draw!!!")
            return True
    else:
        return False

def check_row_win(gameboard_state):
    for i in range(3):
        row_string = ''
        for j in range(3):
            row_string += gameboard_state[i][j]
        if row_string == X_WIN_STRING:
            return X_WIN_STRING
        elif row_string == O_WIN_STRING:
            return O_WIN_STRING
    return '-'

def check_column_win(gameboard_state):
    # Notation is as: GBS[i][j] is GBS[row_i][column_j]
    # An example win for X would be GBS[0][2]=='X' and GBS[1][2]=='X' and GBS[2][2]=='X'
    column_strings = ['', '', '']
    for i in range(3):        # i refers to Row number
        for j in range(3):    # j refers to Column number
            column_strings[j] += gameboard_state[i][j]

    for col_j in range(3):
        column_str = column_strings[col_j]
        if column_str == X_WIN_STRING:
            return X_WIN_STRING
        elif column_str == O_WIN_STRING:
            return O_WIN_STRING
    return '-'

def check_diag_win(gameboard_state):
    diag_1_str = '' ; diag_2_str = '' ;
    for x in range(3):
        diag_1_str += gameboard_state[x][x]
        if diag_1_str == X_WIN_STRING:
            return X_WIN_STRING
        elif diag_1_str == O_WIN_STRING:
            return O_WIN_STRING
    for x in range(3):
        diag_2_str += gameboard_state[3-1-x][x]
        if diag_2_str == X_WIN_STRING:
            return X_WIN_STRING
        elif diag_2_str == O_WIN_STRING:
            return O_WIN_STRING
    return '-'

# Here are a few tests to make sure we're correctly identifying each of
# the different types of winning states, and the draw/tie state:  

# Row numbers are: 0, 1, 2 for a 3x3 Game
# Col numbers are: 0, 1, 2 for a 3x3 Game
# Diag1 is the cells (0,0), (1,1), (2,2) for a 3x3 Game
# Diag2 is the cells (0,2), (1,1), (2,0) for a 3x3 Game

X_win_row_1 = [ ['O','' ,'O'],
                ['X','X','X'],
                ['' ,'O','' ]
              ]

O_win_col_2 = [ ['' ,'X','O'],
                ['' ,'X','O'],
                ['' ,'O','O']
              ]

X_win_diag1 = [ ['X','' ,'X'],
                ['' ,'X','X'],
                ['' ,'X','X']
              ]

O_win_diag2 = [ ['' ,'' ,'O'],
                ['' ,'O','X'],
                ['O','X','X']
              ]

a_draw_state = [ ['X','O','O'],
                 ['O','X','X'],
                 ['O','X','O']
               ]
if DEBUG:
    # Run the tests. Should print out 'XXX', 'OOO', 'XXX', 'OOO', 'True'
    w = check_row_win(X_win_row_1);    print(w)
    x = check_column_win(O_win_col_2); print(x)
    y = check_diag_win(X_win_diag1);   print(y)
    z = check_diag_win(O_win_diag2);   print(z)
    a = check_draw(a_draw_state);      print(a)
