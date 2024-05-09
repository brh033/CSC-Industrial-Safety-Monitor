from tkinter import *
import tkinter as tk
import tk_tools
import RPi as GPIO

# Initialize communication with RPi
RPi.init()

class MainGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg="white")
        #run a method that sets up the layout
        self.setupGUI()
        
    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, height=2,\
            width=15, font=("Arial", 20))
        self.display.grid(row = 0, column = 0,\
            columnspan=4,\
            sticky = E+W+N+S)
        self.pack(fill=BOTH, expand=1)

        root = tk.Tk()

        p1 = tk_tools.RotaryScale(root, max_value=210, unit='cpm')
        p1.grid(row=1,column=0,sticky=N+S+E+W)

        p2 = tk_tools.RotaryScale(root, max_value=210, unit='cpm')
        p2.grid(row=1,column=1,sticky=N+S+E+W)

        p3 = tk_tools.RotaryScale(root, max_value=210, unit='cpm')
        p3.grid(row=2,column=0,sticky=N+S+E+W)

        p4 = tk_tools.RotaryScale(root, max_value=210, unit='cpm')
        p4.grid(row=2,column=1,sticky=N+S+E+W)

    def update_gauge(self):
        # get input from RPi
        

        global p, count
        count = 30.0
        p.set_value(count)
        count += 1.0 
        p.set_value(count)

        # send to RPi
        # window.after(50, update_gauge)

    def update(self):
        try:
            pass
        except:
            self.display["text"] = "ERROR"

###########################################
window = Tk()
# window.after(50, update_gauge)
window.title("Sense All")
MainGUI(window)
window.mainloop()