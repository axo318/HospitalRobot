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

# Returns list with sensor data
def colorValues():
    colorSensorL = ColorSensor("in1")
    colorSensorM = ColorSensor("in2")
    colorSensorR = ColorSensor("in3")
    colorSensorL.mode='COL-REFLECT'
    colorSensorM.mode='COL-REFLECT'
    colorSensorR.mode='COL-REFLECT'
    values = [colorSensorL.value(), colorSensorM.value(), colorSensorR.value()]
    return values

def move(courseValue):
    leftside = -(200 - (7.5*courseValue))/10
    rightside = -(200 + (7.5*courseValue))/10
    
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
    leftFrontMotor.run_direct(duty_cycle_sp=leftside)
    leftRearMotor.run_direct(duty_cycle_sp=leftside)

    # Right side
    rightFrontMotor.run_direct(duty_cycle_sp=rightside)
    rightRearMotor.run_direct(duty_cycle_sp=rightside)


# MAIN
#--------------------------------------------------------------------#
def main():
    print("Sensor Test is starting")
    print("\n")

    lasterror = error = integral = 0

    while(1):
        values = colorValues()
        left = values[0]
        mid = values[1]
        right = values[2]
        print("Left Sensor: "+ str(left))
        print("Middle Sensor: "+str(mid))
        print("Right Sensor: "+str(right))
        avg = (left + mid + right)/3            # Find average

        if(avg > 55 and mid < 50):
            error = 0
            course = 0
            print("Go straight")
        else:
            error = -1*left + right
            print("Error is: "+ str(error))
            derivative = error - lasterror
            lasterror = error
            integral = float(0.3) * integral + error
            course = (float(1.0)*error + float(0.28)*derivative + float(0.1)*integral)
            print("Current Course is "+ str(course))
        move(course)
        print("\n")


if __name__ == "__main__":
    main()
    rightFrontMotor.stop()
    leftFrontMotor.stop()
    rightRearMotor.stop()
    leftRearMotor.stop()
