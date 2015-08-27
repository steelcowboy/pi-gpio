#! /usr/bin/env python3

import RPi.GPIO as GPIO
import curses
from time import sleep
from sys import exit
from os import system

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 17]

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.LOW)

GPIO.setwarnings(False)

myscreen = curses.initscr()

curses.noecho()

myscreen.border(0)
myscreen.addstr(12, 25, "Press 1-3 to light up some lights, or 'e' to exit")
myscreen.refresh()


while True:
    light = myscreen.getkey()
    try:   
        lightnum = int(light) - 1
    except ValueError:
        lightnum = 4
    if 0 <= lightnum <= 2:
        GPIO.output(pins[lightnum], GPIO.HIGH)
        sleep(0.2)
        GPIO.output(pins[lightnum], GPIO.LOW)
    elif light == "e":
        system('clear')
        exit(0)

curses.endwin()
