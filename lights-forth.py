#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
from itertools import cycle 
import sys
import mypins

GPIO.setmode(GPIO.BCM)

pins = mypins.pins6

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

c = cycle(pins)
i = 1

try:
    for x in c:
        x = int(x)
        GPIO.output(x, GPIO.HIGH)
        ti = 0.75 if i % 4 == 0 else 0.5
        time.sleep(ti)
        GPIO.output(x, GPIO.LOW)
        i+=1
        
except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
