#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time, sys
from itertools import cycle
from threading import Thread
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

def runLEDs():
    for x in c:
        cycle_pin(x)

for i in pins[::-1]:
    pins.append(i)

c = cycle(pins)

try:
    t1 = Thread(target=runLEDs)
    t1.daemon = True
    t1.start()
    while True:
        #if GPIO.input(pins[0]):
        #print("Hit the first one!")
        time.sleep(1)
except KeyboardInterrupt:
    t1.join()
    GPIO.output(pins, GPIO.LOW)
    sys.exit(0)
