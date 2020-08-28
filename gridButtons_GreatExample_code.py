import tkinter as tk
root = tk.Tk()

# Make a 2D grid/array of buttons, inside the Tkinter main window which is called 'root' in this example
for rowNum in range(3):                 # rowNum will take on the value 0, then 1, then 2 ( i.e. in [0,1,2] )
    for colNum in range(3):             # colNum will take on the value 0, then 1, then 2 ( i.e. in [0,1,2] )
        button = tk.Button( root ,                                              # This button's parent TKinter object will be the main TKinter window, here it's called 'root'
                            text = str(rowNum)+" "+str(colNum) ,                # Button text will be "3 4" when rowNum==3 and colNum==4
                            command = lambda r=rowNum, c=colNum: printOnClick(r, c)  # Run the printOnClick(r,c) function when button is clicked. r is row num, c is col num.
                           )
        button.grid(row=rowNum, column=colNum)                                  # Add this button to a grid structure in the root window, with row=rowNum & column=colNum

# Show how Tkinter's grid_slaves() function works well
def printOnClick(r, c):
    widget = root.grid_slaves(row=r, column=c)[0]                           # Use TKinter's grid_slaves function to get the Button at pos (r,c) and store it in var 'widget'
    [button_row, button_column] = widget['text'].split(' ')                 # Retrieve the button's row and column numbers from 'widget's' 'text' element
    print("Button Clicked was: Row = " + button_row + ", Column = " + button_column)    # Print out the Row and Column numbers of the button that got clicked on

# Run the TKinter Main GUI Program, show it on the screen:
tk.mainloop()
