#
#   Class for creating and holding both motor objects
#   All different moving methods should be added as methods
#

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3


class RobotMotors:
    # Initializes robot right and left motors
    def __init__(self):
        self.rightMotor = ev3.LargeMotor('outA')
        self.rightMotor.connected
        self.leftMotor = ev3.LargeMotor('outB')
        self.leftMotor.connected

    def moveDirect(self, leftside, rightside):
        self.leftMotor.run_direct(duty_cycle_sp=-leftside)
        self.rightMotor.run_direct(duty_cycle_sp=-rightside)

    def runTimed(self):
        self.leftMotor.run_timed(speed_sp=800, time_sp=1000)
        self.rightMotor.run_timed(speed_sp=800, time_sp=1000)
        #time.sleep(1)

    def stop(self):
        self.rightMotor.stop()
        self.leftMotor.stop()

    def waiting(self):
        print('motors waiting..')
        self.leftMotor.run_direct(duty_cycle_sp=0)
        self.rightMotor.run_direct(duty_cycle_sp=0)
