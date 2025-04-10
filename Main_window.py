from tkinter import *
from tkinter import ttk
import time
#reset function
def reset():
    minutes.set("00")
    seconds.set("00")
    
    minutes_entry.delete(0,END)
    seconds_entry.delete(0,END)

    minutes_entry.insert(0,"00")
    seconds_entry.insert(0,"00")



#start function
def start():
    
    minutes = minutes_entry.get()
    print('Minutes:'+ minutes)

    seconds = seconds_entry.get()
    print("Seconds:"+seconds)
    

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
seconds_entry = Entry(pomodoro_window,width = 2,text = seconds)

start_button = Button(master = pomodoro_window,command = start,font = ("Times New Roman",20), bg = "green",text = "Start")
pause_button = Button(master = pomodoro_window,command = pause,font = ("Times New Roman",20), bg = "red",text="Stop")
reset_button = Button(master = pomodoro_window,command = reset,font = ("Times New Roman",20), bg = "blue",text = "Reset")


#Grid System
pomodoro_window.columnconfigure((0,1,2),weight = 1)
pomodoro_window.rowconfigure(0,weight = 1)
pomodoro_window.rowconfigure(1,weight = 1)


#***FIX ME (Notes in Git)***
#Entries
minutes_entry.grid(row = 0,column = 0,sticky = "w")
seconds_entry.grid(row = 0,column = 1,sticky = "e")

#Buttons
start_button.grid(row = 1, column = 0,sticky = "nesw")
pause_button.grid(row = 1, column = 1,sticky = "nesw")
reset_button.grid(row = 1, column = 2,sticky = "nesw")


#This segment will be used if I decide to put in images

#start_image = PhotoImage(file = "C:/Users/Gr880/Desktop/Coding/Pomodoro_Timer/Main/start.png")
#pause_image = PhotoImage(file = "C:/Users/Gr880/Desktop/Coding/Pomodoro_Timer/Main/pause.png")
#reset_image = PhotoImage(file = "C:/Users/Gr880/Desktop/Coding/Pomodoro_Timer/Main/reset.png")





pomodoro_window.mainloop()

