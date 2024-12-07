import tkinter as tk
from tkinter import ttk
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')

#area
#----------------------------------------------------------------------------------------------


def convert():
    ac_input1=entry_int.get()
    sq_output=ac_input1*43560
    output_string1.set(sq_output)

def convert2():
    h_input2=entry_int2.get()
    a_output2=h_input2*2.471054
    output_string2.set(a_output2)

def convert3():
    sm_input3=entry_int3.get()
    sy_output3=sm_input3*(1.19599)
    output_string3.set(sy_output3)

def convert4():
    sf_input4=entry_int4.get()
    si_output4=sf_input4*(144)
    output_string4.set(si_output4)
#----------------------------------------------------------------------------------------------


title_label=ttk.Label(master=win,text="Acres to Square feet",font="Calibri 24 bold")
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

title_label2=ttk.Label(master=win,text="Hectares to Acres",font="Calibri 24 bold")
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
title_label3=ttk.Label(master=win,text="Square metres to Square yards",font="Calibri 24 bold")
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

title_label4=ttk.Label(master=win,text="Square feet to Square inches",font="Calibri 24 bold")
title_label4.pack()


input_frame4=ttk.Frame(master=win)
entry_int4=tk.IntVar()
entry4=ttk.Entry(master=input_frame4,textvariable=entry_int4)
button4=ttk.Button(master=input_frame4,text="Convert",command=convert4)
entry4.pack(side='left',padx=10)
button4.pack(side='left')
input_frame4.pack(pady=10)

output_string4=tk.StringVar()
output_label4=ttk.Label(master=win,text="Output",font="Calibri 24 bold",textvariable=output_string4)
output_label4.pack(pady=5)

#----------------------------------------------------------------------------------------------

win.mainloop()