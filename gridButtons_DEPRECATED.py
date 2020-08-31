import tkinter as tk  # Import the TKinter library/module so we can use it
DEBUG = 3
root = tk.Tk()  # Create the top-level Window object. It's not displayed yet, though!

buttons = { 0:{0:None,1:None,2:None}, 1:{0:None,1:None,2:None}, 2:{0:None,1:None,2:None} }
button_pos = {}

# Make a 2D array of buttons
for rowN in range(3):
    for colN in range(3):
        button = tk.Button(root, text = "", height=3, width=6,
                           command = lambda r=rowN, c=colN: doStuffOnClick(r, c) )
        buttons[rowN][colN] = button            # Save this new button into the "buttons" List variable
        button_pos[button] = (rowN, colN)       # Save the position of this button into the "button_pos" Dict
        if DEBUG >= 2:
            print(button , button_pos[button])      # 
        button.grid(row=rowN, column=colN)      # Place this new button into the current TKinter grid layout
    #endfor colNum
#endfor rowNum

# Print out some helpful information when we click on one of the buttons in the grid
def doStuffOnClick(r, c):
    theButton = buttons[r][c]
    print("The button name/ID is: " + str(theButton) )
    theButtonPos = button_pos[theButton]
    (button_row, button_column) = button_pos[theButton]
    print("Button Clicked was: Row=" + str(button_row) + \
          ", Column=" + str(button_column) )                        # Backslash ('\') lets you continue ur code statement on the next line

tk.mainloop()   # Run the TKinter Main GUI Program, i.e. show it on the screen.
