import tkinter as tk
from tkinter import ttk
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')

#WEIGHT AND MASS
#----------------------------------------------------------------------------------------------


def convert():
    Kg_input1=entry_int.get()
    pounds_output=Kg_input1*2.204623
    output_string1.set(pounds_output)

def convert2():
    Carats_input2=entry_int2.get()
    kg_output2=Carats_input2*0.0002
    output_string2.set(kg_output2)

def convert3():
    centigram_input3=entry_int3.get()
    metric_output3=centigram_input3*0.00000001
    output_string3.set(metric_output3)

#----------------------------------------------------------------------------------------------


title_label=ttk.Label(master=win,text="Kilograms To Pounds",font="Calibri 24 bold")
title_label.pack()

#input field
input_frame=ttk.Frame(master=win)
entry_int=tk.IntVar()
entry=ttk.Entry(master=input_frame,textvariable=entry_int)
button=ttk.Button(master=input_frame,text="Convert",command=convert)
entry.pack(side='left',padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string1=tk.StringVar()
output_label1=ttk.Label(master=win,text="Output",font="Calibri 24 bold",textvariable=output_string1)
output_label1.pack(pady=5)

#----------------------------------------------------------------------------------------------

title_label2=ttk.Label(master=win,text="Carats to Kilogram",font="Calibri 24 bold")
title_label2.pack()


input_frame2=ttk.Frame(master=win)
entry_int2=tk.IntVar()
entry2=ttk.Entry(master=input_frame2,textvariable=entry_int2)
button2=ttk.Button(master=input_frame2,text="Convert",command=convert2)
entry2.pack(side='left',padx=10)
button2.pack(side='left')
input_frame2.pack(pady=10)

output_string2=tk.StringVar()
output_label2=ttk.Label(master=win,text="Output",font="Calibri 24 bold",textvariable=output_string2)
output_label2.pack(pady=5)
#----------------------------------------------------------------------------------------------
title_label3=ttk.Label(master=win,text="Centigram to Metric Ton",font="Calibri 24 bold")
title_label3.pack()


input_frame3=ttk.Frame(master=win)
entry_int3=tk.IntVar()
entry3=ttk.Entry(master=input_frame3,textvariable=entry_int3)
button3=ttk.Button(master=input_frame3,text="Convert",command=convert3)
entry3.pack(side='left',padx=10)
button3.pack(side='left')
input_frame3.pack(pady=10)

output_string3=tk.StringVar()
output_label3=ttk.Label(master=win,text="Output",font="Calibri 24 bold",textvariable=output_string3)
output_label3.pack(pady=5)

#----------------------------------------------------------------------------------------------


win.mainloop()