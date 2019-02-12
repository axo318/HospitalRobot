# Some simple open loop scripts

import ev3dev.ev3 as ev3
import time
import utilities as util
from ev3dev.ev3 import *
from time import sleep
import math

rightMotor = ev3.LargeMotor('outA')
rightMotor.connected
leftMotor = ev3.LargeMotor('outB')
leftMotor.connected
#rightRearMotor = ev3.LargeMotor('outC')
#rightRearMotor.connected
#leftRearMotor = ev3.LargeMotor('outD')
#leftRearMotor.connected

# Returns list with sensor data
def colorValues():
    colorSensorL = ColorSensor("in1")
    colorSensorM = ColorSensor("in2")
    colorSensorR = ColorSensor("in3")
    colorSensorL.mode='RGB-RAW'
    colorSensorM.mode='RGB-RAW'
    colorSensorR.mode='RGB-RAW'
    values = [colorSensorL.value(), colorSensorM.value(), colorSensorR.value()]
    return values

def move(courseValue):
    if courseValue >= 0:
       rightside = -1*((100/(1 + (math.exp(float(-0.03) * courseValue)))) - 20)
       leftside = -1*((100/(1 + (math.exp(float(-0.03) * -1 * courseValue)))) - 20)
    else:
       leftside = -1*((100/(1 + (math.exp(float(-0.03) * -1 * courseValue)))) - 20)
       rightside = -1*((100/(1 + (math.exp(float(-0.03) * courseValue)))) - 20)


    #leftside = -(300 - (7.5*courseValue))/10
    #rightside = -(300 + (7.5*courseValue))/10

    print("leftside is:" + str(leftside))
    print("rightside is:" + str(rightside))

    if(leftside>90):
        leftside=90
    if(rightside>90):
        rightside=90
    if(leftside<-90):
        leftside=-90
    if(rightside<-90):
        rightside=-90
    print("leftside after is:" + str(leftside))
    print("rightside after is:" + str(rightside))


    # Left side
    leftMotor.run_direct(duty_cycle_sp=-leftside)
    #leftRearMotor.run_direct(duty_cycle_sp=leftside)

    # Right side
    rightMotor.run_direct(duty_cycle_sp=-rightside)
    #rightRearMotor.run_direct(duty_cycle_sp=rightside)


# MAIN
#--------------------------------------------------------------------#
def main():
    print("Sensor Test is starting")
    print("\n")

    lasterror = error = integral = prevcourse = 0

    while(1):
        values = colorValues()
        left = values[0]
        mid = values[1]
        right = values[2]
        print("Left Sensor: "+ str(left))
        print("Middle Sensor: "+str(mid))
        print("Right Sensor: "+str(right))
        avg = (left + mid + right)/3            # Find average

        if(avg > 165 and mid < 50):
            error = 0
            course = 0
            print("Go straight")
        elif(avg > 195 and mid > 250):
            print("Line was lost, trying to find it")
            course = prevcourse
        elif(avg > 150 and avg < 250):
            rightMotor.run_timed(time_sp=70, speed_sp=-500)
        else:
            error = -1*left + right
            print("Error is: "+ str(error))
            derivative = error - lasterror
            lasterror = error
            integral = float(0.3) * integral + error
            course = (float(0.8)*error + float(0.4)*derivative + float(0.02)*integral)
            print("Current Course is "+ str(course))
        move(course)
        prevcourse = course
        print("\n")


if __name__ == "__main__":
    main()
