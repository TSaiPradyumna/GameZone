import tkinter as tk
from tkinter import ttk
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')

#speed
#----------------------------------------------------------------------------------------------


def convert():
    kn_input1=entry_int.get()
    km_output=kn_input1*1.85184
    output_string1.set(km_output)

def convert2():
    ms_input2=entry_int2.get()
    mh_output2=ms_input2*2.237136
    output_string2.set(mh_output2)

def convert3():
    m_input3=entry_int3.get()
    ms_output3=m_input3*(340.3)
    output_string3.set(ms_output3)

def convert4():
    kh_input4=entry_int4.get()
    cms_output4=kh_input4*(27.77778)
    output_string4.set(cms_output4)
#----------------------------------------------------------------------------------------------


title_label=ttk.Label(master=win,text="Knot to Kilometre per Seconds",font="Calibri 24 bold")
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

title_label2=ttk.Label(master=win,text="Metre per Seconds to Miles per Hour",font="Calibri 24 bold")
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
title_label3=ttk.Label(master=win,text="Mach is Metre per Second",font="Calibri 24 bold")
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

title_label4=ttk.Label(master=win,text="Kilometres per Hour to Centimetres per second",font="Calibri 24 bold")
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