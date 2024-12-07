import tkinter as tk
from tkinter import ttk
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')

def button_function():
    print("a button is pressed")



#ttk label
label=ttk.Label(master=win,text="Converter")
label.pack()



#creating text
text=tk.Text(master=win)
text.pack()

#ttk entry
entry=ttk.Entry(master=win)
entry.pack()



#ttk button
button=ttk.Button(master=win,text="A Button",command=button_function)
button.pack()

#running
win.mainloop()