from tkinter import *
import time

def clocktime():
    system_time=time.strftime('%H:%M:%S %p')
    clock.config(text=system_time)
    clock.after(1000, clocktime)

window=Tk()
window.geometry("600x400")

clock=Label(window, font='Helvetica 26 bold', width=10, fg="Navy Blue", bg="white", relief=RIDGE, padx=10, pady=5)
clock.place(x=185, y=30)

clocktime()

alarm_clock=Label(window, text="Alarm Clock", font='Helvetica 20 bold', fg="Navy Blue", justify=CENTER)
alarm_clock.place(x=220, y=120)

set_time=Label(window, text="Set Time", font='Helvetica 15 bold', fg="Navy Blue", justify=CENTER)
set_time.place(x=255, y=190)

hour=StringVar(window, value="H")
min=StringVar(window, value="M")
sec=StringVar(window, value="S")

hourTime=Entry(window, textvariable=hour, font='Helvetica 15', width=10, fg="Navy Blue", bd=5,  bg="white", justify=CENTER)
hourTime.place(width=45, x=225, y=250)

minTime=Entry(window, textvariable=min, font='Helvetica 15', width=10, fg="Navy Blue", bd=5,  bg="white", justify=CENTER)
minTime.place(width=45, x=280, y=250)

secTime=Entry(window, textvariable=sec, font='Helvetica 15', width=10, fg="Navy Blue", bd=5,  bg="white", justify=CENTER)
secTime.place(width=45, x=335, y=250)

window.mainloop()