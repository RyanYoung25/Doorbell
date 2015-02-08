#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    #Default 7, 11, 13
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(7, False)

def blink():
    setup()
    while True:
        GPIO.output(7, True)
        time.sleep(.5)
        GPIO.output(7, False)
        time.sleep(.5)
