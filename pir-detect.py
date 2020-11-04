## Code for the PIR detection part of PiPatrol

import RPi.GPIO as GPIO      # module for GPIO
import time                  # module for time delays

time.sleep(1)                # stops program for 1 second

GPIO.setmode(GPIO.BOARD)     # technicality about numbering
GPIO.setwarnings(False)      # disable annoying warnings
GPIO.setup(4, GPIO.IN)       # setting up our pin

while True:                  # infinite loop
    i = GPIO.input(4)        # storing input signal
    if i==0:                 # if no human detected
        time.sleep(0.1)      # just sleep for 100 ms
    elif i==1:               # if human detected
        time.sleep(0.1)      
        i = GPIO.input(4)
        if i==1:             # confirm it isn't a fluke
            <OTHER THINGS>   # do these things
