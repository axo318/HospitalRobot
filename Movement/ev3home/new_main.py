#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors

global cur_motors
global error
global lasterror
global integral
global  prevcourse
global  office
global counter

cur_motors =  motors.RobotMotors()
#error = lasterror = integral = prevcourse = office = 0

def operate(left, mid, right, lasterror, integral, prevcourse, office):
    # Get color readings and average
    course = 0

    if((left+right)/2 > 330 and mid < 40):
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
        course = (float(0.4)*error + float(0.3)*derivative + float(0.02)*integral)

    leftside, rightside = function.getOutput(course)
    cur_motors.moveDirect(leftside, rightside)
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
    officeA = ['R','L','R']
    red_time = current_time = 0
    red_seen = False

    # Stop everything and return if the arg is not start
    if input != 'start':
        cur_motors.stop()
        print('stopping')
        return

    # Initialize all variables
    lasterror = error = integral = prevcourse = counter = 0
    office = officeA

    # Start operation loop
    while(1):
        timeDif()
        [red_vals,green_vals,blue_vals] = sensors.getColourValues()
        # colourValues = sensors.getColourValues()
        [left,mid,right] = red_vals
        #[red_vals,green_vals,blue_vals] = colourValues
        # red_vals = colourValues[0]
        # green_vals = colourValues[1]
        # blue_vals = colourValues[2]
        red_avg = sum(red_vals)/float(len(red_vals))
        green_avg = sum(green_vals)/float(len(green_vals))
        blue_avg = sum(blue_vals)/float(len(blue_vals))
        avg = (left + mid + right)/3
        color = sensors.detectedColor(red_avg,green_avg,blue_avg)

        current_time = time.clock_gettime(time.CLOCK_MONOTONIC)

        #print("red time: ", red_time, " current time: ", current_time)

        if (color == 'red'):
            print("-----Red was detected-----")

            avg = (left + mid + 300)/3
            red_time = time.clock_gettime(time.CLOCK_MONOTONIC)
            red_seen = True

            print(counter)
            print(red_seen)


            if(office[counter] == 'L'):
                operate(left, mid, 300, lasterror, integral, prevcourse, office)
            else:
                operate(300, mid, right, lasterror, integral, prevcourse, office)

        else:
            if(red_seen):
                # print("TIME DIFFERENCE: ", current_time - red_time)
                if(current_time - red_time < 3 and office[counter] == 'L'):
                    operate(left, mid, 300, lasterror, integral, prevcourse, office)
                elif(current_time - red_time < 3 and office[counter] == 'R'):
                    operate(300, mid, right, lasterror, integral, prevcourse, office)
                else:
                    red_seen = False
                    red_time = current_time
                    counter+=1
                    operate(left, mid, right, lasterror, integral, prevcourse, office)
            else:
                red_time = current_time
                operate(left, mid, right, lasterror, integral, prevcourse, office)

######### --MAIN-- ##########
if __name__ == "__main__":
    input = sys.argv[1]
    global AFTER_TIMER
    global PREV_TIMER

    PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("Ev3 is starting...")
    print("\n")
    main(input)
