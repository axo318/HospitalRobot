#! /usr/bin/env python3
# Core imports
import time
import ev3dev.ev3 as ev3

# Local Imports
import tutorial as tutorial

print ('Welcome to ev3')

#ev3.Sound.speak('Welcome to e v 3').wait()

# Step A: Basic open driving
#tutorial.operateWheelsBasic()

tutorial.movement()
#tutorial.turnAllMotors()

# Step B: Turn on an off an LED using a switch
#tutorial.makeLightSwitch()

# Step C: Use switches to drive robot back and forward
#tutorial.makeLightAndMotorSwitch()

# Step D: Record values from the ultrasonic to a text file
#tutorial.recordUltraSonic()

# remove this if you want it to exit as soon as its done:
print ("wait 10sec, then end")
time.sleep(10)
