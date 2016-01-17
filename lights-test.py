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

try:
    for x in c:
        x = int(x)
        GPIO.output(x, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(x, GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
