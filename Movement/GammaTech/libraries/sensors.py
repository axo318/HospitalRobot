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

def getdetectedColor():
    # Find colour averages
    [red_vals,green_vals,blue_vals] = getColourValues()
    red_avg = sum(red_vals)/float(len(red_vals))
    green_avg = sum(green_vals)/float(len(green_vals))
    blue_avg = sum(blue_vals)/float(len(blue_vals))

    # Choose closest color
    if 205<red_avg<300  and 15<green_avg<50 and 10<blue_avg<60:
        return 'red'
    elif 20<red_avg<60 and 65<green_avg< 140 and 20<blue_avg<100:
        return 'green'
    elif 235<red_avg<400 and 105<green_avg<180 and 30<blue_avg<115:
        return 'yellow'
    else: return None

def detectedColor(red_avg,green_avg,blue_avg):
    # Choose closest color
    if 205<red_avg<300  and 15<green_avg<50 and 10<blue_avg<60:
        return 'red'
    elif 20<red_avg<60 and 65<green_avg< 140 and 20<blue_avg<100:
        return 'green'
    elif 235<red_avg<400 and 105<green_avg<180 and 30<blue_avg<115:
        return 'yellow'
    else: return None
