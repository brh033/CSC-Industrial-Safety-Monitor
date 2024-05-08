import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import RPi

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=5)

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with rpi
RPi.init()

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # read from Arduino
    input_info = ser.readline()
    print("Read input " + input_info.decode("utf-8").strip() + "from Arduino")

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(input_info)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Gauges')
    plt.ylabel('cpm')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
