#
#   Functionality of sensors stays here
#   If different mode is wanted, it can be changed by the only variable
#

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3


# Sets the sensor mode
required_mode = 'RGB-RAW'

# Returns all readings in a list
def getColourValues():
    colorSensorL = ColorSensor("in1")
    colorSensorM = ColorSensor("in2")
    colorSensorR = ColorSensor("in3")
    colorSensorL.mode = required_mode
    colorSensorM.mode = required_mode
    colorSensorR.mode = required_mode

    red_val = [colorSensorL.value(0), colorSensorM.value(0), colorSensorR.value(0)]
    green_val = [colorSensorL.value(1), colorSensorM.value(1), colorSensorR.value(1)]
    blue_val = [colorSensorL.value(2), colorSensorM.value(2), colorSensorR.value(2)]
    return [red_val,green_val,blue_val]
