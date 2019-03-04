
#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors_v2, communications, commands

def operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors):

    # Robot is going straight
    if((left+right)/2 > 260 and mid < 40):
        error = 0
        course = 0

    # Trying to refind the lost line
    elif((left+right)/2 > 170 and mid > 150):
        course = prevcourse

    # Correct course to center the line
    else:
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

def checkCurrentIntersection(office, counter, left, right, red_seen):
    if(office[counter] == 'L'):
        right = 300
    elif(office[counter] == 'R'):
        left = 300
    else:
        red_seen = False

    return left, right, red_seen

def exitGracefully():
    print("Terminating ev3 operation")
    exit()

# main Loop runs here
def main():

    # Initialize motors and sensors connections
    cur_sensors = sensors_v2.ev3Sensors()
    cur_motors = motors.RobotMotors()

    # Initialize communications server and current command
    com_server = communications.Communicator()
    com_server.listen()
    command_dealer = commands.Command()

    # Initialize navigation variables
    red_time = current_time = 0
    red_seen = False
    lasterror = error = integral = prevcourse = counter = course = 0
    office = []

    try:
        # Start operation loop
        while(1):
            # Firstly retrieve and deal with command
            temp_command = com_server.getCurrentCommand()
            iteration_command = command_dealer.dealWithCommand(temp_command)

            # Act on the active_command
            if(iteration_command == "stop"):
                cur_motors.stop()
                counter = 0
                continue
            elif(iteration_command == "start"):
                office = command_dealer.getCurrentPath()

            # Get sensor values
            color,[left,mid,right] = cur_sensors.getSensorData()

            # RED is seen only once
            if (color == 'red'):
                #print("-----Red was detected-----")
                avg = (left + mid + 300)/3
                red_seen = True

                print(counter)
                print(office[counter])

                # While in red stay here
                while(color == 'red'):
                    color,[left,mid,right] = cur_sensors.getSensorData()
                    left, right, red_seen = checkCurrentIntersection(office, counter, left, right, red_seen)
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors)
                print("out of here")
                counter+=1

            # Yellow is seen
            elif(color == 'yellow'):
                cur_motors.waiting()
                time.sleep(5)
                cur_motors.runTimed()
            # Otherwise do what was being done before
            else:
                if(red_seen):
                    print("Going: ", office[counter])
                    left, right, red_seen = checkCurrentIntersection(office, counter, left, right, red_seen)
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors)
                else:
                    red_time = current_time
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors)

    # If user kills program
    except KeyboardInterrupt:
        com_server.die()
        cur_motors.stop()
        exitGracefully()

######### --MAIN-- ##########
if __name__ == "__main__":

    global AFTER_TIMER
    global PREV_TIMER

    PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("Ev3 is starting...")
    print("\n")
    main()
