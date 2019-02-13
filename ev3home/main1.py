#! /usr/bin/env python3
#
#  PAPADOC
#  ROUTE 1
#
import sys
import time
from time import sleep
from libraries import function, motors, sensors
from motors import RobotMotors

#Initialize time and color rectangles
start_time = 0
waiting_time = 0
color = ''
detectedColorForTurning = ''
run = True
cur_motors = motors.RobotMotors()
input = None
def operate(motors, error, lasterror, integral, prevcourse):
    global start_time
    global waiting_time
    global color
    global detectedColorForTurning
    global run
    global input
    global cur_motors
    # Get color readings and average
    current_time = time.clock_gettime(time.CLOCK_MONOTONIC)
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

    if current_time < start_time + 7 or current_time < waiting_time + 8:
        if detectedColorForTurning == 'red':
            avg = (left + mid + 300)/3
            right = 300

        elif detectedColorForTurning == 'green':
            avg = (300 + mid + right)/3
            left = 300

        elif detectedColorForTurning == 'yellow' and current_time < waiting_time + 7:
            print("waiting")
            cur_motors.waiting()

        elif detectedColorForTurning == 'yellow' and current_time >= waiting_time + 7:
            print("starting to move again")
            cur_motors.runTimed()
            print('sleeping')
            run = True
            color = None

    if color != None:
        if color == 'red':
            print('red detected, start moving left')
            error = 0
            course = 0
            side = 0
            start_time = current_time
            detectedColorForTurning = 'red'

        elif color == 'green':
            print('green detected, start moving right')
            error = 0
            course = 0
            side = 0
            start_time = current_time
            detectedColorForTurning = 'green'

        elif color == 'yellow' and run == True:
            print('yellow detected, going straight')
            error = 0
            course = 0
            #motors.waiting()
            #input = 'stop'
            if run:
                waiting_time = current_time
            run = False
            detectedColorForTurning = 'yellow'


    elif not color:
        if((left+right)/2 > 290 and mid < 40 and (green_vals[0]+green_vals[2])/2 > 260 and green_vals[1] < 30 and (blue_vals[0]+blue_vals[2])/2 > 320 and blue_vals[1] <40):
            error = 0
            course = 0
        elif((left+right)/2 > 290 and mid > 200 and (green_vals[0]+green_vals[2])/2 > 260 and green_vals[1] < 200 and (blue_vals[0]+blue_vals[2])/2 > 320 and blue_vals[1] < 180):
            print("Line was lost, trying to find it")
            course = prevcourse
        else:
            error = -1*left + right

            derivative = error - lasterror
            lasterror = error
            integral = float(0.3) * integral + error
            course = (float(0.8)*error + float(0.4)*derivative + float(0.02)*integral)

    if run:
        leftside, rightside = function.getOutput(course)
        motors.moveDirect(leftside, rightside)
        prevcourse = course
    #else:
    #    cur_motors.waiting()


# main Loop runs here
def main(input):

    # Initialize motors
    cur_motors = motors.RobotMotors()

    if input == 'start':

        # Initialize all variables
        lasterror = error = integral = prevcourse = 0

        # Start operation loop
        while(1):
            operate(cur_motors, error, lasterror, integral, prevcourse)
    else:
        cur_motors.stop()
        print('stopping')

######### --MAIN-- ##########
if __name__ == "__main__":
    input = sys.argv[1]

    print("Ev3 is starting...")
    print("\n")
    main(input)
