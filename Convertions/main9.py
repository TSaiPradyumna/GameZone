import tkinter as tk
from tkinter import ttk
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')

#data
#----------------------------------------------------------------------------------------------


def convert():
    g_input1=entry_int.get()
    t_output=g_input1*0.001
    output_string1.set(t_output)

def convert2():
    m_input2=entry_int2.get()
    k_output2=m_input2*1024
    output_string2.set(k_output2)

def convert3():
    t_input3=entry_int3.get()
    z_output3=t_input3*(0.000000001)
    output_string3.set(z_output3)

def convert4():
    y_input4=entry_int4.get()
    z_output4=y_input4*(1208.926)
    output_string4.set(z_output4)
#----------------------------------------------------------------------------------------------


title_label=ttk.Label(master=win,text="Gigabytes to Terabytes",font="Calibri 24 bold")
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

title_label2=ttk.Label(master=win,text="Mebibits to Kibibits",font="Calibri 24 bold")
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
title_label3=ttk.Label(master=win,text="Terabytes to Zetabytes",font="Calibri 24 bold")
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

title_label4=ttk.Label(master=win,text="Yobibits to Zetabits",font="Calibri 24 bold")
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