#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors


def operate(motors, error, lasterror, integral, prevcourse, office):
    # Get color readings and average
    colourValues = sensors.getColourValues()
    [left,mid,right] = colourValues[0]

    course=0

    if((left+right)/2 > 290 and mid < 40):
        error = 0
        course = 0

    elif((left+right)/2 > 290 and mid > 200):
        print("Line was lost, trying to find it")
        course = prevcourse
    else:
        error = -1*left + right

        derivative = error - lasterror
        lasterror = error
        integral = float(0.3) * integral + error
        course = (float(0.8)*error + float(0.4)*derivative + float(0.02)*integral)

    leftside, rightside = function.getOutput(course)
    motors.moveDirect(leftside, rightside)
    prevcourse = course


def timeDif():
    global AFTER_TIMER
    global PREV_TIMER
    AFTER_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print(AFTER_TIMER - PREV_TIMER)
    PREV_TIMER = AFTER_TIMER
# main Loop runs here
def main(input):

    # Initialize motors
    cur_motors = motors.RobotMotors()
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC)
    officeA = ['L','L','R']

    if input == 'start':


        # Initialize all variables
        lasterror = error = integral = prevcourse = 0
        office = officeA

        # Start operation loop
        while(1):
            timeDif()
            colourValues = sensors.getColourValues()
            [left,mid,right] = colourValues[0]
            red_vals = colourValues[0]
            green_vals = colourValues[1]
            blue_vals = colourValues[2]
            red_avg = sum(red_vals)/float(len(red_vals))
            green_avg = sum(green_vals)/float(len(green_vals))
            blue_avg = sum(blue_vals)/float(len(blue_vals))
            avg = (left + mid + right)/3
            color = sensors.detectedColor(red_avg,green_avg,blue_avg)

            if (color == 'red'):
               print("Red was detected")
               avg = (left + mid + 300)/3

               if(office[counter] == 'L'):
                   right = 300
               else:
                   left = 300

                   counter+=1

            else:
                operate(cur_motors, error, lasterror, integral, prevcourse, office)
    else:
        cur_motors.stop()
        print('stopping')

######### --MAIN-- ##########
if __name__ == "__main__":
    input = sys.argv[1]
    global AFTER_TIMER
    global PREV_TIMER

    PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("Ev3 is starting...")
    print("\n")
    main(input)
