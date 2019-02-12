#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors

#Initialize time
start_time = 0
color = ''
def operate(motors, error, lasterror, integral, prevcourse):
    global start_time
    global color
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

    if current_time < start_time + 7:
        if color == 'R':
            avg = (left + mid + 300)/3
            right = 300
            print('masking right sensor...........')
        elif color == 'G':
            avg = (300 + mid + right)/3
            left = 300
            print('masking left sensor...........')
    
    if red_avg > 180 and green_avg<100 and blue_avg<120:
        print('red detected, start moving left')
        error = 0
        course = 0
        side = 0
        start_time = current_time  
        color = 'R'
        if side == 0:
            pass
        else:
            pass   
    elif 20<red_avg< 60 and 65<green_avg< 140 and 20<blue_avg<100:
        print('green detected, start moving right')
        error = 0
        course = 0
        side = 0
        start_time = current_time  
        color = 'G'
        if side == 0:
            pass
        else:
            pass   
    elif(avg > 180 and mid < 50):
        error = 0
        course = 0
        print("Go straight")
    elif(avg > 150 and mid > 250):
        print("Line was lost, trying to find it")
        course = prevcourse
    # elif(avg > 150 and avg < 250):
    #     rightMotor.run_timed(time_sp=70, speed_sp=-500)
    else:
        error = -1*left + right
        print("Error is: "+ str(error))
        derivative = error - lasterror
        lasterror = error
        integral = float(0.3) * integral + error
        course = (float(0.8)*error + float(0.4)*derivative + float(0.02)*integral)
        print("Current Course is "+ str(course))
    leftside, rightside = function.getOutput(course)
    motors.moveDirect(leftside, rightside)
    prevcourse = course
    print("\n")


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
