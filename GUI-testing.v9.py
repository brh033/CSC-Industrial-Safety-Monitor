from tkinter import *
import tkinter as tk
import tk_tools
# import serial

# ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)

root = tk.Tk()

p1 = tk_tools.RotaryScale(root, max_value=2500.0, unit='cpm')
p1.grid(row=1,column=0,sticky=N+S+E+W)

p2 = tk_tools.RotaryScale(root, max_value=2500.0, unit='cpm')
p2.grid(row=1,column=1,sticky=N+S+E+W)

p3 = tk_tools.RotaryScale(root, max_value=2500.0, unit='cpm')
p3.grid(row=2,column=0,sticky=N+S+E+W)

p4 = tk_tools.RotaryScale(root, max_value=2500.0, unit='cpm')
p4.grid(row=2,column=1,sticky=N+S+E+W)

count = 30.0
p1.set_value(count)

def update_gauge():
    global p1, count
    count += 1 #geiger_input, mq-2_input, mq-8_input, mq-9_input
    p1.set_value(count)
    root.after(50, update_gauge)

root.after(50, update_gauge)
root.title("Guardian Sense-All")
root.mainloop()