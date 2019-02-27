import sys
import time
from . import function, motors, sensors

class State:
    def __init__(self):
        # State
        self.state = "Operate"

        # Robot motors
        self.motors = motors.RobotMotors()

        # PID vars
        self.lasterror = 0
        self.error = 0
        self.integral = 0
        self.prevcourse = 0
        self.course = 0

        # Turning timer
        self.initialTime = None

        # All hardcoded locations
        self.locationA = ['L','L','R']
        self.curDestination = self.locationA
        self.counter = 0

        self.COUNTMEASURES = 0
        self.PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
        self.AFTER_TIMER = 0

    def setState(self, state):
        self.state = state

    def operate(self, left, mid, right):
        # Go straight
        if((left+right)/2 > 290 and mid < 50):
            print("straight")
            self.error = 0

        # Try and find the lost line

        elif((left+right)/2 > 290 and mid > 200):
            print("Line was lost, trying to find it")
            self.course = self.prevcourse

        # Otherwise center the line
        else:
            print("turn")

            self.error = -1*left + right
            self.derivative = self.error - self.lasterror
            self.lasterror = self.error
            self.integral = float(0.3) * self.integral + self.error
            self.course = (float(0.8)*self.error + float(0.4)*self.derivative + float(0.02)*self.integral)

        leftside, rightside = function.getOutput(self.course)
        self.motors.moveDirect(leftside, rightside)
        self.prevcourse = self.course


    def turn(self, direction, left, mid, right):
        # Mask the right sensor
        if(direction == 'L'):
            operate(left, mid, 300)
        # Mask the left sensor
        else:
            operate(300, mid, right)

    def timeDif(self):
        self.AFTER_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
        print(self.AFTER_TIMER - self.PREV_TIMER)
        self.PREV_TIMER = self.AFTER_TIMER

    def run(self):
        #self.timeDif()
        self.COUNTMEASURES += 1
        #color = sensors.getdetectedColor()
        color = ""
        colorValues = sensors.getColourValues()
        #print(str(self.COUNTMEASURES) , colorValues)
        [left,mid,right] = colorValues[0]
        #[left,mid,right] = [100,100,100]
        # OPERATE STATE
        self.timeDif()
        print("---------------")
        if(self.state == "Operate"):
            self.operate(left,mid,right)
            self.timeDif()
            # # Check if entering a junction
            # if(color=="red"):
            #     print("going to junction state")
            #     self.state = "Junction"
            #     return
            # else:
            #     self.operate(left,mid,right)

        # JUNCTION STATE
        elif(self.state == "Junction"):
            # Check if exiting junction
            if(color != "red"):
                print("going to POSTjunction state")
                self.initialTime = time.clock_gettime(time.CLOCK_MONOTONIC)
                self.state = "PostJunction"
                return
            else:
                self.operate(300, 0, 300)

        # POSTJUNCTION STATE
        elif(self.state == "PostJunction"):
            cur_time = time.clock_gettime(time.CLOCK_MONOTONIC)
            # Check if timer has ended
            if(cur_time - self.initialTime > 3):
                print("going to operate state")
                self.counter += 1
                self.state = "Operate"
            # Turn towards preset destination
            else:
                self.turn(curDestination[counter])
