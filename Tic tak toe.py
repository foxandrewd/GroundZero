from tkinter import *

tkWindow = Tk()
tkWindow.title('PythonExamples.org - Tkinter Example')


def toggleText0():
    if (button0['text'] == 'Submit'):
        button0['text'] = 'X'
    elif (button0['text'] == 'X'):
        button0['text'] = 'O'
    else:
        button0['text'] = 'Submit'


def toggleText1():
    if (button1['text'] == 'Submit'):
        button1['text'] = 'X'
    elif (button1['text'] == 'X'):
        button1['text'] = 'O'
    else:
        button1['text'] = 'Submit'

def toggleText2():
    if (button2['text'] == 'Submit'):
        button2['text'] = 'X'
    elif (button2['text'] == 'X'):
        button2['text'] = 'O'
    else:
        button2['text'] = 'Submit'

def toggleText3():
    if (button3['text'] == 'Submit'):
        button3['text'] = 'X'
    elif (button3['text'] == 'X'):
        button3['text'] = 'O'
    else:
        button3['text'] = 'Submit'

def toggleText4():
    if (button4['text'] == 'Submit'):
        button4['text'] = 'X'
    elif (button4['text'] == 'X'):
        button4['text'] = 'O'
    else:
        button4['text'] = 'Submit'

def toggleText5():
    if (button5['text'] == 'Submit'):
        button5['text'] = 'X'
    elif (button5['text'] == 'X'):
        button5['text'] = 'O'
    else:
        button5['text'] = 'Submit'

def toggleText6():
    if (button6['text'] == 'Submit'):
        button6['text'] = 'X'
    elif (button6['text'] == 'X'):
        button6['text'] = 'O'
    else:
        button6['text'] = 'Submit'

def toggleText7():
    if (button7['text'] == 'Submit'):
        button7['text'] = 'X'
    elif (button7['text'] == 'X'):
        button7['text'] = 'O'
    else:
        button7['text'] = 'Submit'

def toggleText8():
    if (button8['text'] == 'Submit'):
        button8['text'] = 'X'
    elif (button8['text'] == 'X'):
        button8['text'] = 'O'
    else:
        button8['text'] = 'Submit'



button0 = Button(tkWindow, text='Submit', command=toggleText0, padx=50, pady=50)

button1 = Button(tkWindow, text='Submit', command=toggleText1, padx=50, pady=50)

button2 = Button(tkWindow, text='Submit', command=toggleText2, padx=50, pady=50)

button3 = Button(tkWindow, text='Submit', command=toggleText3, padx=50, pady=50)

button4 = Button(tkWindow, text='Submit', command=toggleText4, padx=50, pady=50)

button5 = Button(tkWindow, text='Submit', command=toggleText5, padx=50, pady=50)

button6 = Button(tkWindow, text='Submit', command=toggleText6, padx=50, pady=50)

button7 = Button(tkWindow, text='Submit', command=toggleText7, padx=50, pady=50)

button8 = Button(tkWindow, text='Submit', command=toggleText8, padx=50, pady=50)

button0.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)
button5.grid(row=1, column=2)
button6.grid(row=2, column=0)
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
tkWindow.mainloop()