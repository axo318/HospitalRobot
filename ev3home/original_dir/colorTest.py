
import ev3dev.ev3 as ev3
from time import sleep
import utilities as util
from ev3dev.ev3 import *

def test():
    required_mode = 'RGB-RAW'
    colorSensorL = ColorSensor("in1")
    colorSensorM = ColorSensor("in2")
    colorSensorR = ColorSensor("in3")
    colorSensorL.mode = required_mode
    colorSensorM.mode = required_mode
    colorSensorR.mode = required_mode
    print('colortest')
   
    while True:
        red_val = [colorSensorL.value(0), colorSensorL.value(1), colorSensorL.value(2)]
        green_val = [colorSensorM.value(0), colorSensorM.value(1), colorSensorM.value(2)]
        blue_val = [colorSensorR.value(0), colorSensorR.value(1), colorSensorR.value(2)]
        print('left',red_val,'middle',green_val,'right',blue_val)
        sleep(0.5)
# I get max 80 with white paper, 3mm separation 
# and 5 with black plastic, same separation
