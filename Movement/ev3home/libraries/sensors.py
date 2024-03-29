#
#   Functionality of sensors stays here
#   If different mode is wanted, it can be changed by the only variable
#

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3


# Sets the sensor mode
required_mode = 'RGB-RAW'
ultrasonic_mode = 'US-DIST-CM'

class ev3Sensors:
    # Initializes robot right and left motors
    def __init__(self):
        self.colorSensorL = ColorSensor("in1")
        self.colorSensorM = ColorSensor("in2")
        self.colorSensorR = ColorSensor("in3")
        self.ultrasonicSensor = UltrasonicSensor("in4")
        self.ultrasonicSensor.mode = ultrasonic_mode
        self.colorSensorL.mode = required_mode
        self.colorSensorM.mode = required_mode
        self.colorSensorR.mode = required_mode

    def getSensorData(self):
        [red_vals,green_vals,blue_vals] = self.getColourValues()
        [left,mid,right] = red_vals

        # Get current color
        red_avg = sum(red_vals)/float(len(red_vals))
        green_avg = sum(green_vals)/float(len(green_vals))
        blue_avg = sum(blue_vals)/float(len(blue_vals))
        avg = (left + mid + right)/3
        color = self.detectedColor(red_avg,green_avg,blue_avg)

        return color,red_vals

    def calibrate(self, motors):
        step=3
        angle=250
        calibration_data = []
        motors.moveAngle(-angle)

        for i in range(0,2*angle,step):
            motors.moveAngle(step)
            color, vals = self.getSensorData()
            calibration_data.append(vals)
            print(vals)

        #left_readings = [x[0] for x in calibration_data].sort()
        #mid_readings = [x[1] for x in calibration_data].sort()
        #right_readings = [x[2] for x in calibration_data].sort()


    def getDistance(self):
        return self.ultrasonicSensor.value()

    # Returns all readings in a list
    def getColourValues(self):
        red_val = [self.colorSensorL.value(0), self.colorSensorM.value(0), self.colorSensorR.value(0)]
        green_val = [self.colorSensorL.value(1), self.colorSensorM.value(1), self.colorSensorR.value(1)]
        blue_val = [self.colorSensorL.value(2), self.colorSensorM.value(2), self.colorSensorR.value(2)]
        return [red_val,green_val,blue_val]

    def detectedColor(self,red_avg,green_avg,blue_avg):
        # Choose closest color
        if 160<red_avg<300  and 15<green_avg<60 and 10<blue_avg<60:
            return 'red'
        elif 20<red_avg<60 and 65<green_avg< 140 and 20<blue_avg<100:
            return 'green'
        elif 235<red_avg<400 and 105<green_avg<180 and 30<blue_avg<115:
            return 'yellow'
        else: return None
