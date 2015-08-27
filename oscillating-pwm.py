#! /usr/bin/env python3

import RPi.GPIO as GPIO
from collections import OrderedDict
import time
import sys

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4, 14, 17, 18]

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

p = OrderedDict()

try:
    
    
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
