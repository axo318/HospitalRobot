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
        self.right2Motor = ev3.LargeMotor('outC')
        self.right2Motor.connected
        self.leftMotor = ev3.LargeMotor('outB')
        self.leftMotor.connected
        self.left2Motor = ev3.LargeMotor('outD')
        self.left2Motor.connected

    def moveDirect(self, leftside, rightside):
        self.leftMotor.run_direct(duty_cycle_sp=leftside)
        self.left2Motor.run_direct(duty_cycle_sp=-leftside)
        self.rightMotor.run_direct(duty_cycle_sp=rightside)
        self.right2Motor.run_direct(duty_cycle_sp=-rightside)

    def runTimed(self):
        self.leftMotor.run_timed(speed_sp=-500, time_sp=500)
        self.left2Motor.run_timed(speed_sp=500, time_sp=500)
        self.rightMotor.run_timed(speed_sp=-500, time_sp=500)
        self.right2Motor.run_timed(speed_sp=500, time_sp=500)
        #time.sleep(1)

    def stop(self):
        self.rightMotor.stop()
        self.right2Motor.stop()
        self.leftMotor.stop()
        self.left2Motor.stop()

    def waiting(self):
        print('motors waiting..')
        self.leftMotor.run_direct(duty_cycle_sp=0)
        self.lrft2Motor.run_direct(duty_cycle_sp=0)
        self.rightMotor.run_direct(duty_cycle_sp=0)
        self.right2Motor.run_direct(duty_cycle_sp=0)

    def uTurn(self):
        self.rightMotor.run_to_rel_pos(position_sp=540, speed_sp=900)
        self.leftMotor.run_to_rel_pos(position_sp=-540, speed_sp=900)
