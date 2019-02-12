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

#MAIN
#--------------------------------------------------------------------#
def main():
    print("Sensor Test is stopping")
    print("\n")
    rightFrontMotor.stop()
    leftFrontMotor.stop()
    rightRearMotor.stop()
    leftRearMotor.stop()


    
if __name__ == "__main__":
    main()
