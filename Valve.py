#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys


class ControlValve:
    def __init__(self):
        print("valve.py")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.OUT)
        
    def openValve(valve_open_time):
        open_time = valve_open_time
        GPIO.output(17, True)
        time.sleep(open_time)
        GPIO.output(17, False)
            
    def stopValveControl():
        GPIO.cleanup()