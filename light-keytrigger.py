#! /usr/bin/env python3

import RPi.GPIO as GPIO
import curses
from time import sleep
from sys import exit
from os import system
import mypins

GPIO.setmode(GPIO.BCM)

pins = mypins.pins6

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

myscreen = curses.initscr()

curses.noecho()

myscreen.border(0)
myscreen.addstr(12, 25, "Press 1-{} to light up some lights, or 'e' to exit".format(len(pins)))
myscreen.refresh()


while True:
    light = myscreen.getkey()
    try:   
        lightnum = int(light) - 1
    except ValueError:
        lightnum = len(pins)
    if 0 <= lightnum <= len(pins)-1:
        GPIO.output(pins[lightnum], GPIO.HIGH)
        sleep(0.1)
        GPIO.output(pins[lightnum], GPIO.LOW)
    elif light == "e":
        system('clear')
        exit(0)

curses.endwin()
