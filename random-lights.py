#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
from itertools import cycle 
import sys
from random import choice, randrange

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 17]

for x in pins:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.LOW)

GPIO.setwarnings(False)

try:
    while True:
        light = int(choice(pins))
        rand = randrange(1, 10, 1) / 10
        GPIO.output(light, GPIO.HIGH)
        time.sleep(rand)
        GPIO.output(light, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    sys.exit(0)
