from tkinter import *
import tkinter as tk
import tk_tools
import serial

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)
ser.reset_input_buffer()

root = tk.Tk()

p1 = tk_tools.RotaryScale(root, max_value=2500.0, unit='ppm')
p1.grid(row=1,column=0,sticky=N+S+E+W)

p2 = tk_tools.RotaryScale(root, max_value=2500.0, unit='ppm')
p2.grid(row=1,column=1,sticky=N+S+E+W)

p3 = tk_tools.RotaryScale(root, max_value=2500.0, unit='ppm')
p3.grid(row=2,column=0,sticky=N+S+E+W)

p4 = tk_tools.RotaryScale(root, max_value=2500.0, unit='cpm')
p4.grid(row=2,column=1,sticky=N+S+E+W)

count = 30.0
p1.set_value(count)

def update_gauge():
    global p1, count
    #count += 1 #geiger_input, mq-2_input, mq-8_input, mq-9_input
    p1.set_value(dict.get(MQ2))
    #root.after(50, update_gauge)

#root.after(50, update_gauge)
root.title("Guardian Sense-All")
root.mainloop()
dict = {
    "MQ2": 0,
    "MQ8": 0,
    "MQ9": 0,
    "rad": 0
}
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        dict.update(MQ2 = line[5:8])
        update_gauge()