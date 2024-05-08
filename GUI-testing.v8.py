import plotly.graph_objects as go
import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)

# read from Arduino
input_info = ser.readline()
print("Read input " + input_info.decode("utf-8").strip() + "from Arduino")

while 1:
    # write 
    ser.write(b'status\n')
    input_info = ser.readline().decode("utf-8").strip()
    if (input_info == ""):
        print(".")
    else:
        print("Read input back: " + input_info)

    time.sleep(5)

    ser.write(b'set on\n')
    input_info = ser.readline().decode("utf-8").strip()
    if (input_info == ""):
        print(".")
    else:
        print("Read input back: " + input_info)

    time.sleep(5)

    ser.write(b'set of\n')
    input_info = ser.readline().decode("utf-8").strip()
    if (input_info == ""):
        print(".")
    else:
        print("Read input back: " + input_info)

    time.sleep(5)

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 270,
    domain = {"x": [0,1], "y": [0,1]},
    title = {"text": "speed"}
))

fig.show()