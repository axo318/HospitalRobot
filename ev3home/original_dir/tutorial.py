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
    #motor2.run_timed(speed_sp=500, time_sp=2500)
    time.sleep(0.5)
    motor1.run_timed(speed_sp=-500, time_sp=2500)
    #motor2.run_timed(speed_sp=-500, time_sp=2500)
    waitForMotor(motor1)                         # Can use something like this to prevent the program from progressing
    motor1.run_timed(speed_sp=1000, time_sp=2500)
    #motor2.run_timed(speed_sp=1000, time_sp=2500)
    waitForMotor(motor1)
    print('sleeping for 1 second')
    time.sleep(1)

def waitForMotor(motor):
    time.sleep(0.1)         # Make sure that motor has time to start
    while motor.state==["running"]:
        print('Motor is still running')
        time.sleep(0.1)



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
    colorSensorL = ColorSensor("in1")
    colorSensorM = ColorSensor("in2")
    colorSensorR = ColorSensor("in3")
    colorSensorL.mode='COL-REFLECT'
    colorSensorM.mode='COL-REFLECT'
    colorSensorR.mode='COL-REFLECT'
    values = [colorSensorL.value(), colorSensorM.value(), colorSensorR.value()]
    calibrate_white()
    return values

def turnRight():
    #turn right
    leftFrontMotor.run_timed(speed_sp=-600,time_sp=60)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=-600,time_sp=60)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=400,time_sp=60)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=400,time_sp=60)#, stop_action="hold").wait()

def turnLeft():
    #turn right
    leftFrontMotor.run_timed(speed_sp=400,time_sp=60)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=400,time_sp=60)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=-600,time_sp=60)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=-600,time_sp=60)#, stop_action="hold").wait()

def goStraight():
    #go straight
    leftFrontMotor.run_timed(speed_sp=-600,time_sp=70)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=-600,time_sp=70)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=-600,time_sp=70)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=-600,time_sp=70)#, stop_action="hold").wait()

def turnAllMotors():

    leftFrontMotor.run_timed(speed_sp=-400,time_sp=100)#, stop_action="hold").wait()
    leftRearMotor.run_timed(speed_sp=-400,time_sp=100)#, stop_action="hold").wait()
    rightFrontMotor.run_timed(speed_sp=-400,time_sp=100)#, stop_action="hold").wait()
    rightRearMotor.run_timed(speed_sp=-400,time_sp=100)#, stop_action="hold").wait()

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
    upperThreshold = 55
    lowerThreshold = 55
    blackDetected = False

    while movement:
        values = colorValues()

        if ((values[1] <= upperThreshold) and (values[0] <= lowerThreshold)):
            turnLeft()
        elif ((values[1] <= lowerThreshold) and (values[2] <= lowerThreshold)):
            turnRight()
        elif values[1] <= upperThreshold:
            goStraight()
        elif ((values[1] > upperThreshold) and (values[0] <= lowerThreshold)):
            turnLeft()
        elif ((values[1] > upperThreshold) and (values[2] <= lowerThreshold)):
            turnRight()
        elif(values[0] > 80 and values[1] > 80 and values[2] > 80):
            stopMotors()            
        else: stopMotors()
