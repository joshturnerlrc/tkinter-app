#importing
from tkinter import *

def button_click():
    typed_text = entryA.get()
    output_text.delete(0.0, END)
    try:
        meaning = my_dictionary [typed_text]
    except:
        meaning = "the word you entered cannot be found"
    output_text.insert(END, meaning)
    print(typed_text)

def function1():
    textarea.delete(0.0, END)
    textarea.insert(END, "menu1")

def function2():
    textarea.delete(0.0, END)
    textarea.insert(END, "menu2")

def on_click():
    number = v.get()
    textbox.delete(0.0, END)
    textbox.inset(END, number)








window = Tk()
window.title("GUI")

##text above box
#labelA = Label(window, text="enter something here: ")
#labelA.grid(row=0, column=0, sticky=W)

##entry box
#entryA = Entry(window, width=20, bg="light green")
#entryA.grid(row=1, column=0, sticky=E)

##clickable button
#buttonA = Button(window, text="submit", width=8, command=button_click)
#buttonA.grid(row=2, column=0, sticky= W)


##output area
#output_text = Text(window,width=30, height=10, wrap=WORD, background="yellow")
#output_text.grid (row=3, column=0, columnspan=2, sticky=W)

##dictionary
#my_dictionary = {"dictionary": "test"}

##dictionaru button
#buttonA = Button(window, text="dictionary", width=8, command=button_click)
#buttonA.grid(row=2, column=0, sticky= E)

##menubar
#menubar = Menu(window)

#firstmenu = Menu(menubar, tearoff=0)
#firstmenu.add_command(label = "option 1", command=function1)
#firstmenu.add_command(label = "quit", command=window.destroy)
#menubar.add_cascade(label="menu1", menu=firstmenu)

#secondmenu = Menu(menubar, tearoff=0)
#secondmenu.add_command(label ="Option 1", command=function2)
#secondmenu.add_command(label ="quit!", command=window.destroy)
#menubar.add_cascade(label="menu2", menu=secondmenu)

#window.config(menu=menubar)

##spinbox widget
v=IntVar()
spin = Spinbox(window, textvariable=V, from_=1, to = 10)
spin.grid(row+0, column = 0, sticky=W)

##textbox
textbox = Text(window, width=20, height=10)
textbox.grid(row=1, column=0, sticky=W)

##button
button = Button(window


window.mainloop()

