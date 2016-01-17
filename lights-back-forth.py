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

def cycle_pin(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    
for i in pins[::-1]:
    pins.append(i)

c = cycle(pins)

try:
    for x in c:
        cycle_pin(x)

except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
