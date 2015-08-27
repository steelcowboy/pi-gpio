#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
from itertools import cycle 
import sys

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4, 14, 17, 18]

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

c = cycle(pins)
i = 1

try:
    for x in c:
        x = int(x)
        GPIO.output(x, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(x, GPIO.LOW)
        i+=1
        
except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
