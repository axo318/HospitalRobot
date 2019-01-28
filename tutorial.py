# Some simple open loop scripts

import ev3dev.ev3 as ev3
import time
import utilities as util
from ev3dev.ev3 import *
from time import sleep

rightFrontMotor = ev3.LargeMotor('outA')
rightFrontMotor.connected
leftFrontMotor = ev3.LargeMotor('outB')
leftFrontMotor.connected
rightRearMotor = ev3.LargeMotor('outC')
rightRearMotor.connected
leftRearMotor = ev3.LargeMotor('outD')
leftRearMotor.connected


def operateWheelsBasic():
    print("spin the wheels")

    motor1=ev3.LargeMotor('outA')
    motor1.connected
    motor2=ev3.LargeMotor('outB')
    motor2.connected

    # run_time takes milliseconds
    motor1.run_timed(speed_sp=500, time_sp=2500) # Not blocking, notice how it skips to next command
    motor2.run_timed(speed_sp=500, time_sp=2500)
    time.sleep(0.5)
    motor1.run_timed(speed_sp=-500, time_sp=2500)
    motor2.run_timed(speed_sp=-500, time_sp=2500)
    waitForMotor(motor1)                         # Can use something like this to prevent the program from progressing
    motor1.run_timed(speed_sp=1000, time_sp=2500)
    motor2.run_timed(speed_sp=1000, time_sp=2500)
    waitForMotor(motor1)
    print('sleeping for 1 second')
    time.sleep(1)

def waitForMotor(motor):
    time.sleep(0.1)         # Make sure that motor has time to start
    while motor.state==["running"]:
        print('Motor is still running')
        time.sleep(0.1)

def makeLightSwitch():
    print ("turn on LED w switch")
    print ("for 10 seconds")

    t_start = util.timestamp_now()
    ts = ev3.TouchSensor(ev3.INPUT_1)
    while True:
        ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[ts.value()])
        t_now = util.timestamp_now()
        if (t_now - t_start > 10E3):
            print ("finishing")
            break

    print ("turning off light")
    print (" ")
    ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[0])

def makeLightAndMotorSwitch():
    print ("drive forward and back")
    print ("using switches")
    print ("for 30 seconds")

    motor = ev3.LargeMotor('outA')
    motor.connected

    t_start = util.timestamp_now()
    ts = ev3.TouchSensor(ev3.INPUT_1)
    ts2 = ev3.TouchSensor(ev3.INPUT_2)
    while True:
        ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[ts.value()])
        ev3.Leds.set_color(ev3.Leds.RIGHT, (ev3.Leds.GREEN, ev3.Leds.RED)[ts2.value()])

        if (ts.value()):
            motor.run_timed(speed_sp=100, time_sp=50)
        elif (ts2.value()):
            motor.run_timed(speed_sp=-100, time_sp=50)

        t_now = util.timestamp_now()
        if (t_now - t_start > 30E3):
            print ("im done")
            break

    print ("turning off light, done")
    ev3.Leds.set_color(ev3.Leds.LEFT, (ev3.Leds.GREEN, ev3.Leds.RED)[0])

def recordUltraSonic():
    print("Record readings from ultrasonic")
    print("Will print after back button is pressed")

    btn = ev3.Button()

    sonar = ev3.UltrasonicSensor(ev3.INPUT_1)
    sonar.connected
    sonar.mode = 'US-DIST-CM' # Will return value in mm

    readings = ("")
    readings_file = open('results.txt', 'w')

    while not btn.backspace:
        readings = readings + str(sonar.value()) + '\n'
    readings_file.write(readings)
    readings_file.close() # Will write to a text file in a column

def colorValues():
    cl = ColorSensor()
    cl.mode='COL-REFLECT'
    return cl.value()

def turnRight():
    #turn right
    leftFrontMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=400,time_sp=50)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=400,time_sp=50)#, stop_action="hold").wait()

def turnLeft():
    #turn right
    leftFrontMotor.run_timed(speed_sp=400,time_sp=50)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=400,time_sp=50)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()

def goStraight():
    #go straight
    leftFrontMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()

def turnAllMotors():

    leftFrontMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=-400,time_sp=50)#, stop_action="hold").wait()

def stopMotors():
    leftFrontMotor.stop()
    leftRearMotor.stop()
    rightFrontMotor.stop()
    rightRearMotor.stop()

def movement():
    rightFrontMotor = ev3.LargeMotor('outA')
    rightFrontMotor.connected
    leftFrontMotor = ev3.LargeMotor('outB')
    leftFrontMotor.connected
    rightRearMotor = ev3.LargeMotor('outC')
    rightRearMotor.connected
    leftRearMotor = ev3.LargeMotor('outD')
    leftRearMotor.connected

    movement = True
    upperThreshold = 15
    lowerThreshold = 5
    blackDetected = False

    while movement:
        colorValue = colorValues()

        if colorValue < upperThreshold:
            blackDetected = True
            #turnAllMotors()
            goStraight()
            #print("colorValue is: " + colorValue)
        elif ((colorValue >= upperThreshold) and blackDetected):
            #turnAllMotors()
            turnLeft()
            #print("colorValue is: " + colorValue + " - blackDetected!!!")
        elif colorValue >= upperThreshold:
            blackDetected = True
            #turnAllMotors()
            turnRight()
            #print("colorValue is: " + colorValue)
        else: stopMotors()
