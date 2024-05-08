import time
import random

def get_cpm():
    count = 0
    current_minute = time.time()
    new_datetime = current_minute + 10
    while time.time() < new_datetime:
        if GPIO.input(12) == True:
                count = count + 1
        # Simulating Geiger counter input
        # count += 1
        # time.sleep(random.randint(0, 1))  # Simulated pulse detection delay
    
    counts_per_min = (count//10)*60
    return count

if __name__ == "__main__":
    while True:
        cpm = get_cpm()
        print("Counts per minute:", cpm)
