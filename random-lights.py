#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time
from itertools import cycle 
import sys
from random import choice, randrange
import mypins

GPIO.setmode(GPIO.BCM)

pins = mypins.pins6 

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

try:
    while True:
        light = int(choice(pins))
        rand = randrange(1, 10, 1) / 10
        GPIO.output(light, GPIO.HIGH)
        time.sleep(rand)
        GPIO.output(light, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
