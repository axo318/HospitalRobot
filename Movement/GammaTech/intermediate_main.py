
#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors_v2, communications, commands

def operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors):

    #print(left, " ",mid," ", right)
    # Robot is going straight
    if((left+right)/2 > 260 and mid < 40):
        #print("Going straight")
        error = 0
        course = 0

    # Trying to refind the lost line
    elif((left+right)/2 > 170 and mid > 150):
        #print("Line was lost, trying to find it")
        course = prevcourse

    # Correct course to center the line
    else:
        #print("Correcting")
        error = -1*left + right

        derivative = error - lasterror
        lasterror = error
        integral = float(0.3) * integral + error
        course = (float(0.4)*error + float(0.3)*derivative + float(0.02)*integral)

    leftside, rightside = function.getOutput(course)
    cur_motors.moveDirect(leftside, rightside)
    prevcourse = course
    #print(course)
    return prevcourse

def timeDif():
    global AFTER_TIMER
    global PREV_TIMER
    AFTER_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print(AFTER_TIMER - PREV_TIMER)
    PREV_TIMER = AFTER_TIMER

# main Loop runs here
def main():

    # Initialize motors and sensors connections
    cur_sensors = sensors_v2.ev3Sensors()
    cur_motors = motors.RobotMotors()
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC)

    # Initialize communications server and current command
    com_server = communications.Communicator()
    com_server.listen()
    command_dealer = commands.Command()

    # Initialize navigation variables

    red_time = current_time = 0
    red_seen = False
    lasterror = error = integral = prevcourse = counter = course = 0
    office = []

    # Start operation loop
    while(1):
        #timeDif()
        # Firstly retrieve and deal with command
        temp_command = com_server.getCurrentCommand()
        if(temp_command != None):
            print(temp_command)
            command_dealer.dealWithCommand(temp_command)

        # Act on the active_command
        iteration_command = command_dealer.getActiveCommand()
        if(iteration_command == "stop"):
            cur_motors.stop()
            counter = 0
            # while(command_dealer.getActiveCommand() != "stop"):
            #     continue
            continue
        elif(iteration_command == "start"):
            office = command_dealer.getCurrentPath()

        # Get sensor values
        [red_vals,green_vals,blue_vals] = cur_sensors.getColourValues()
        [left,mid,right] = red_vals
        # Get current color
        red_avg = sum(red_vals)/float(len(red_vals))
        green_avg = sum(green_vals)/float(len(green_vals))
        blue_avg = sum(blue_vals)/float(len(blue_vals))
        avg = (left + mid + right)/3
        color = cur_sensors.detectedColor(red_avg,green_avg,blue_avg)
        # Get current time
        current_time = time.clock_gettime(time.CLOCK_MONOTONIC)

        # If seen red, then get ready for turn
        if (color == 'red'):
            #print("-----Red was detected-----")
            avg = (left + mid + 300)/3
            red_time = time.clock_gettime(time.CLOCK_MONOTONIC)
            red_seen = True

            print(counter)
            print(office[counter])

            while(color == 'red'):
                [red_vals,green_vals,blue_vals] = cur_sensors.getColourValues()
                [left,mid,right] = red_vals
                # Get current color
                red_avg = sum(red_vals)/float(len(red_vals))
                green_avg = sum(green_vals)/float(len(green_vals))
                blue_avg = sum(blue_vals)/float(len(blue_vals))
                avg = (left + mid + right)/3
                color = cur_sensors.detectedColor(red_avg,green_avg,blue_avg)

                if(office[counter] == 'L'):
                    prevcourse = operate(left, mid, 300, lasterror, integral, prevcourse, office, cur_motors)
                elif(office[counter] == 'R'):
                    prevcourse = operate(300, mid, right, lasterror, integral, prevcourse, office, cur_motors)
                else:
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors)
            print("out of here")
            counter+=1

        elif(color == 'yellow'):
            cur_motors.waiting()
            time.sleep(5)
            cur_motors.runTimed()
        # Otherwise do what was being done before
        else:
            if(red_seen):
                print("Going: ", office[counter])
                if(office[counter] == 'L'):
                    prevcourse = operate(left, mid, 300, lasterror, integral, prevcourse, office, cur_motors)
                elif(office[counter] == 'R'):
                    prevcourse = operate(300, mid, right, lasterror, integral, prevcourse, office, cur_motors)
                else:
                    red_seen = False
                    #red_time = current_time
                    #counter+=1
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors)
            else:
                red_time = current_time
                prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors)

######### --MAIN-- ##########
if __name__ == "__main__":

    global AFTER_TIMER
    global PREV_TIMER

    PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("Ev3 is starting...")
    print("\n")
    main()
