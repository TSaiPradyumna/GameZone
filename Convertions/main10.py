import tkinter as tk
from tkinter import ttk
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')

#currency
#----------------------------------------------------------------------------------------------


def convert():
    d_input1=entry_int.get()
    i_output=d_input1*82.64
    output_string1.set(i_output)

def convert2():
    i_input2=entry_int2.get()
    jy_output2=i_input2*1.72
    output_string2.set(jy_output2)

def convert3():
    e_input3=entry_int3.get()
    i_output3=e_input3*(90.5980)
    output_string3.set(i_output3)

def convert4():
    c_input4=entry_int4.get()
    i_output4=c_input4*(62.2298)
    output_string4.set(i_output4)
#----------------------------------------------------------------------------------------------


title_label=ttk.Label(master=win,text="INR to USD",font="Calibri 24 bold")
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

title_label2=ttk.Label(master=win,text="INR to JPY",font="Calibri 24 bold")
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
title_label3=ttk.Label(master=win,text="EUR to INR",font="Calibri 24 bold")
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

title_label4=ttk.Label(master=win,text="CAD to INR",font="Calibri 24 bold")
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