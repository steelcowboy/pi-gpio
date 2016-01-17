#! /usr/bin/env python3

import RPi.GPIO as GPIO
from collections import OrderedDict
import time
import sys
import mypins

GPIO.setmode(GPIO.BCM)

pins = mypins.pins6

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

p = OrderedDict()

try:
    for x, y in enumerate(pins):
       p["pin{0}".format(x)] = GPIO.PWM(y, 0.5)
    for key in p:
        p[key].start(5)
        time.sleep(0.1)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
