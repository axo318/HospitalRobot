
#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors_v2

cur_motors =  motors.RobotMotors()

def operate(left, mid, right, lasterror, integral, prevcourse, office):
    
    print(prevcourse)
    print(left," ", mid, " ", right)

    if((left+right)/2 > 330 and mid < 40):
        print("Going straight")
        error = 0
        course = 0

    elif((left+right)/2 > 200 and mid > 150):
        print("Line was lost, trying to find it")
        course = prevcourse
    else:
        print("Correcting")
        error = -1*left + right

        derivative = error - lasterror
        lasterror = error
        integral = float(0.3) * integral + error
        course = (float(0.4)*error + float(0.3)*derivative + float(0.02)*integral)

    leftside, rightside = function.getOutput(course)
    cur_motors.moveDirect(leftside, rightside)
    prevcourse = course
    return prevcourse

def timeDif():
    global AFTER_TIMER
    global PREV_TIMER
    AFTER_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print(AFTER_TIMER - PREV_TIMER)
    PREV_TIMER = AFTER_TIMER

# main Loop runs here
def main(input):

    # Initialize motors
    cur_sensors = sensors_v2.ev3Sensors()
    cur_motors = motors.RobotMotors()
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC)
    officeA = ['L','L','L','L','L']
    red_time = current_time = 0
    red_seen = False

    # Stop everything and return if the arg is not start
    if input != 'start':
        cur_motors.stop()
        print('stopping')
        return

    # Initialize all variables
    lasterror = error = integral = prevcourse = counter = course = 0
    office = officeA

    # Start operation loop
    while(1):
        #timeDif()
        [red_vals,green_vals,blue_vals] = cur_sensors.getColourValues()
        [left,mid,right] = red_vals

        red_avg = sum(red_vals)/float(len(red_vals))
        green_avg = sum(green_vals)/float(len(green_vals))
        blue_avg = sum(blue_vals)/float(len(blue_vals))
        avg = (left + mid + right)/3
        color = cur_sensors.detectedColor(red_avg,green_avg,blue_avg)

        current_time = time.clock_gettime(time.CLOCK_MONOTONIC)

        if (color == 'red'):
            print("-----Red was detected-----")
            avg = (left + mid + 300)/3
            red_time = time.clock_gettime(time.CLOCK_MONOTONIC)
            red_seen = True
            prevcourse = 0

            print(counter)
            

            if(office[counter] == 'L'):
                prevcourse = operate(left, mid, 300, lasterror, integral, prevcourse, office)
            else:
                prevcourse = operate(300, mid, right, lasterror, integral, prevcourse, office)

        else:
            if(red_seen):
                # print("TIME DIFFERENCE: ", current_time - red_time)
                if(current_time - red_time < 4.5 and office[counter] == 'L'):
                    prevcourse = operate(left, mid, 300, lasterror, integral, prevcourse, office)
                elif(current_time - red_time < 4.5 and office[counter] == 'R'):
                    prevcourse = operate(300, mid, right, lasterror, integral, prevcourse, office)
                else:
                    red_seen = False
                    red_time = current_time
                    counter+=1
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office)
            else:
                red_time = current_time
                prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office)

######### --MAIN-- ##########
if __name__ == "__main__":
    input = sys.argv[1]
    global AFTER_TIMER
    global PREV_TIMER

    PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("Ev3 is starting...")
    print("\n")
    main(input)
