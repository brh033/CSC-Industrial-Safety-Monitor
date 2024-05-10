from tkinter import *
import tkinter as tk
import tk_tools
import serial

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)
#ser.reset_input_buffer()

root = tk.Tk()
root.title("Guardian Sense-All")
root.geometry("800x600")

p1 = tk_tools.Gauge(root, width=400, height=300, max_value=600, label='MQ2', unit='ppm')
p1.grid(row=1,column=0,sticky=N+S+E+W)

p2 = tk_tools.Gauge(root, width=400, height=300, max_value=600, label='MQ8', unit='ppm')
p2.grid(row=1,column=1,sticky=N+S+E+W)

p3 = tk_tools.Gauge(root, width=400, height=300, max_value=600, label='MQ9', unit='ppm')
p3.grid(row=2,column=0,sticky=N+S+E+W)

p4 = tk_tools.Gauge(root, width=400, height=300, max_value=600, label='rad', unit='cpm')
p4.grid(row=2,column=1,sticky=N+S+E+W)

dict = {
    "MQ2": 0,
    "MQ8": 0,
    "MQ9": 0,
    "rad": 0
}
while True:
    if ser.in_waiting > 0:
        for i in range(0,2):
          line = ser.readline().decode('utf-8').rstrip()
          dict.update(MQ2 = line[5:8])
          dict.update(MQ8 = line[14:17])
          dict.update(MQ9 = line[23:26])
          dict.update(rad = line[44:47])
          i += 1
        p1.set_value(int(dict.get("MQ2")))
        p2.set_value(int(dict.get("MQ8")))
        p3.set_value(int(dict.get("MQ9")))
        p4.set_value(int(dict.get("rad")))
        root.update_idletasks()
        root.update()

