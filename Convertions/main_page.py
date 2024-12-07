import tkinter as tk
from tkinter import ttk
import os,sys
#creating a window
win=tk.Tk()
win.title("Any Thing Converter")
win.geometry('900x600')
#defining functions
def func1():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main1.py")
def func2():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main2.py")
    
def func3():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main3.py")

def func4():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main4.py")

def func5():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main5.py")

def func6():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main6.py")

def func7():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main7.py")

def func8():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main8.py")

def func9():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main9.py")

def func10():
    os.system(r"E:\MAIN_INTERFACE\Convertions\main10.py")


#Minutes to seconds
label1=ttk.Label(master=win,text="Time Convertions",font="Calibri 24 bold")
label1.place(x=30,y=48,width=300,height=60)

button1=ttk.Button(master=win,text="Convert",command=func1)
button1.place(x=350,y=56,width=200,height=40)


#Minutes to seconds
label2=ttk.Label(master=win,text="Volume Convertions",font="Calibri 24 bold")
label2.place(x=30,y=98,width=300,height=60)

button2=ttk.Button(master=win,text="Convert",command=func2)
button2.place(x=350,y=108,width=200,height=40)


#Minutes to seconds
label3=ttk.Label(master=win,text="Length Convertions",font="Calibri 24 bold")
label3.place(x=30,y=148,width=300,height=60)

button3=ttk.Button(master=win,text="Convert",command=func3)
button3.place(x=350,y=158,width=200,height=40)

#Minutes to seconds
label4=ttk.Label(master=win,text="Mass Convertions",font="Calibri 24 bold")
label4.place(x=30,y=198,width=300,height=60)

button4=ttk.Button(master=win,text="Convert",command=func4)
button4.place(x=350,y=210,width=200,height=40)

#Minutes to seconds
label5=ttk.Label(master=win,text="Temp Convertions",font="Calibri 24 bold")
label5.place(x=30,y=248,width=300,height=60)

button5=ttk.Button(master=win,text="Convert",command=func5)
button5.place(x=350,y=260,width=200,height=40)

#Minutes to seconds
label6=ttk.Label(master=win,text="Area Convertions",font="Calibri 24 bold")
label6.place(x=30,y=298,width=300,height=60)

button6=ttk.Button(master=win,text="Convert",command=func6)
button6.place(x=350,y=310,width=200,height=40)

#Minutes to seconds
label7=ttk.Label(master=win,text="Speed Convertions",font="Calibri 24 bold")
label7.place(x=30,y=348,width=300,height=60)

button7=ttk.Button(master=win,text="Convert",command=func7)
button7.place(x=350,y=360,width=200,height=40)

#Minutes to seconds
label8=ttk.Label(master=win,text="Angle Convertions",font="Calibri 24 bold")
label8.place(x=30,y=398,width=300,height=60)

button8=ttk.Button(master=win,text="Convert",command=func8)
button8.place(x=350,y=410,width=200,height=40)

#Minutes to seconds
label9=ttk.Label(master=win,text="Data Convertions",font="Calibri 24 bold")
label9.place(x=30,y=448,width=300,height=60)

button9=ttk.Button(master=win,text="Convert",command=func9)
button9.place(x=350,y=460,width=200,height=40)

#Minutes to seconds
label10=ttk.Label(master=win,text="Currency Convertions",font="Calibri 24 bold")
label10.place(x=30,y=498,width=300,height=60)

button10=ttk.Button(master=win,text="Convert",command=func10)
button10.place(x=350,y=510,width=200,height=40)

#run
win.mainloop()