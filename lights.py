#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
from itertools import cycle 
import sys

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 17]

for x in pins:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.LOW)

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
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    sys.exit(0)
