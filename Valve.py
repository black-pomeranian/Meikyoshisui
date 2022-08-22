#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

open_time = float(sys.argv[1])

for i in range(50):
    print("{0}回目".format(i))
    GPIO.output(17, True)
    time.sleep(open_time)
    GPIO.output(17, False)
    time.sleep(1)

GPIO.cleanup()