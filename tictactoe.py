# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:22:26 2020

Project Zero - "GroundZero" project

Developers: Andrew Fox and Reuben Corrigan

@author: foxa
"""

import sys, os
import numpy as np
import pandas as pd

CONST_GAME_SIZE = 3     # Indicates we want a 3x3 game of Tic-Tac-Toe

X_WIN_STRING = 'X'*CONST_GAME_SIZE    # i.e. 'XXX' for a 3x3 Game
O_WIN_STRING = 'O'*CONST_GAME_SIZE    # i.e. 'OOO' for a 3x3 Game

gameboard_state = [ ['','',''],       # A blank (starting) gameboard state
                    ['','',''],
                    ['','','']
                  ]

def newgame_clear_board(gameboard_state):
    for i in range(CONST_GAME_SIZE):
        for j in range(CONST_GAME_SIZE):
            gameboard_state[i][j] = ''
    return gameboard_state


def gameboard_is_full(gameboard_state):
    for i in range(CONST_GAME_SIZE):
        for j in range(CONST_GAME_SIZE):
            if gameboard_state[i][j] == '':
                return False
    # All the board positions were filled with X or O. Hence, it's full.
    return True

def X_has_won(gameboard_state):
    if check_row_win(gameboard_state)       == 'X' \
       or check_column_win(gameboard_state) == 'X' \
       or check_diag_win(gameboard_state)   == 'X':
        return True
    else:
        return False

def O_has_won(gameboard_state):
    if check_row_win(gameboard_state)       == 'O' \
       or check_column_win(gameboard_state) == 'O' \
       or check_diag_win(gameboard_state)   == 'O':
        return True
    else:
        return False

def check_draw(gameboard_state):
    if gameboard_is_full(gameboard_state):
        if   X_has_won(gameboard_state): return False
        elif O_has_won(gameboard_state): return False
        else:                            return True

def check_row_win(gameboard_state):
    for i in range(CONST_GAME_SIZE):
        row_string = ''
        for j in range(CONST_GAME_SIZE):
            row_string += gameboard_state[i][j]
        if row_string == X_WIN_STRING:
            return 'X'
        elif row_string == O_WIN_STRING:
            return 'O'
    return '-'

def check_column_win(gameboard_state):
    # Notation is as: GBS[i][j] is GBS[row_i][column_j]
    # An example win for X would be GBS[0][2]=='X' and GBS[1][2]=='X' and GBS[2][2]=='X'
    column_strings = ['']*CONST_GAME_SIZE
    for i in range(CONST_GAME_SIZE):        # i refers to Row number
        for j in range(CONST_GAME_SIZE):    # j refers to Column number
            column_strings[j] += gameboard_state[i][j]

    for col_j in range(CONST_GAME_SIZE):
        column_str = column_strings[col_j]
        if column_str == X_WIN_STRING:
            return 'X'
        elif column_str == O_WIN_STRING:
            return 'O'
    return '-'

def check_diag_win(gameboard_state):
    diag_1_str = '' ; diag_2_str = '' ;
    for x in range(CONST_GAME_SIZE):
        diag_1_str += gameboard_state[x][x]
        if diag_1_str == X_WIN_STRING:
            return 'X'
        elif diag_1_str == O_WIN_STRING:
            return 'O'
    for x in range(CONST_GAME_SIZE):
        diag_2_str += gameboard_state[CONST_GAME_SIZE-1-x][x]
        if diag_2_str == X_WIN_STRING:
            return 'X'
        elif diag_2_str == O_WIN_STRING:
            return 'O'
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

# Run the tests. Should print out 'X', 'O', 'X', 'O', 'True'
w = check_row_win(X_win_row_1); print(w)
x = check_column_win(O_win_col_2); print(x)
y = check_diag_win(X_win_diag1); print(y)
z = check_diag_win(O_win_diag2); print(z)
a = check_draw(a_draw_state); print(a)
