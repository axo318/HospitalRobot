#! /usr/bin/env python3
# Core imports
import time
import ev3dev.ev3 as ev3

# Local Imports
import tutorial2 as tutorial2

print ('Welcome to ev3')

tutorial2.movement()
#tutorial.turnAllMotors()

print ("wait 10sec, then end")
time.sleep(10)
