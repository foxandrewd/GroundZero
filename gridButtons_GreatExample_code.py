import tkinter as tk
root = tk.Tk()

# Make a 2D grid/array of buttons, inside the Tkinter main window which is called 'root' in this example
for rowNum in range(5):
    for colNum in range(5):
        button = tk.Button( root ,
                            text = str(rowNum)+" "+str(colNum) ,
                            command = lambda r=rowNum, c=colNum: printOnClick(r, c)
                           )
        button.grid(row=rowNum, column=colNum)

# Show how Tkinter's grid_slaves() function works really great!!!
def printOnClick(r, c):
    widget = root.grid_slaves(row=r, column=c)[0]
    #print(widget, widget['text'])
    [button_row, button_column] = widget['text'].split(' ')
    print("Button Clicked was: Row = " + button_row + ", Column = " + button_column)

# Run the TKinter Main GUI Program, show it on the screen:
tk.mainloop()
