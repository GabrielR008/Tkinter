from tkinter import *
from tkinter import ttk
import time
#reset function
def reset():
    minutes.set("00")
    seconds.set("00")
    
    minutes_entry.delete(0,END)
    minutes_entry.insert(0,"00")

#start function
def start():
    minutes = minutes_entry.get()
    print(minutes)

#Pause function
def pause():
    #pause timer
    print("pause")

pomodoro_window = Tk()
pomodoro_window.title("Pomodoro Timer")

pomodoro_window.geometry('600x400')

minutes = StringVar()
seconds = StringVar()

minutes.set("00")
seconds.set("00")

minutes_entry = Entry(pomodoro_window,width = 2,text = minutes)

#This segment will be used if I decide to put in images

#start_image = PhotoImage(file = "C:/Users/Gr880/Desktop/Coding/Pomodoro_Timer/Main/start.png")
#pause_image = PhotoImage(file = "C:/Users/Gr880/Desktop/Coding/Pomodoro_Timer/Main/pause.png")
#reset_image = PhotoImage(file = "C:/Users/Gr880/Desktop/Coding/Pomodoro_Timer/Main/reset.png")


start_button = Button(master = pomodoro_window,command = start,font = ("Times New Roman",20), bg = "green")
pause_button = Button(master = pomodoro_window,command = pause,font = ("Times New Roman",20), bg = "red")
reset_button = Button(master = pomodoro_window,command = reset,font = ("Times New Roman",20), bg = "blue")
minutes_entry.pack()
start_button.pack(padx = 50,pady =20)
pause_button.pack(padx = 50)
reset_button.pack(padx = 100)


pomodoro_window.mainloop() 

#git test