import tkinter as tk
from tkinter import ttk
#creating a winsdow  
wins=tk.Tk()
wins.title("Any Thing Converter")
wins.geometry('900x600')
sec_output=0
def convert():
    global sec_output
    minute_input=entry_int.get()
    sec_output=minute_input*60
    output_string.set(sec_output)

title_label=ttk.Label(master=wins,text="Minutes to Seconds",font="Calibri 24 bold")
title_label.pack()


#input field
input_frame=ttk.Frame(master=wins)

entry_int=tk.IntVar()
entry=ttk.Entry(master=input_frame,textvariable=entry_int)
button=ttk.Button(master=input_frame,text="Convert",command=convert)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string=tk.StringVar()
output_label=ttk.Label(master=wins,text="Output",font="Calibri 24 bold",textvariable=output_string)
output_label.pack(pady=5)

wins.mainloop()