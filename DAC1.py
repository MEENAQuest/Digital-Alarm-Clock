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

window.mainloop()