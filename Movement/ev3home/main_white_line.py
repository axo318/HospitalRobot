
#! /usr/bin/env python3
#
#   Main Script
#   Controls the flow of operations
#
import sys
import time
from libraries import function, motors, sensors, communications, commands, logger

def operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors, counter, cur_logger):

    # Robot is going straight
    if((left+right)/2 < 150 and mid > 290):
        error = 0
        course = 0

    # Trying to refind the lost line
    elif((left+right)/2 < 100 and mid < 70):
        course = prevcourse

    # Correct course to center the line
    else:
        error = left + (-1*right)

        derivative = error - lasterror
        lasterror = error
        integral = float(0.3) * integral + error
        course = (float(0.4)*error + float(0.3)*derivative + float(0.02)*integral)

    leftside, rightside = function.getOutput(course, FAST)
    cur_motors.moveDirect(leftside, rightside)
    prevcourse = course

    # Log everything
    sensorVals = [left,mid,right]
    motorVals = [leftside,rightside]
    counterVals = [counter,office[counter]]

    cur_logger.log(course, sensorVals, motorVals, counterVals)

    return prevcourse

def timeDif():
    global AFTER_TIMER
    global PREV_TIMER
    AFTER_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print(AFTER_TIMER - PREV_TIMER)
    PREV_TIMER = AFTER_TIMER

def checkCurrentIntersection(office, counter, left, right, red_seen):
    if(office[counter] == 'L'):
        right = 55
    elif(office[counter] == 'R'):
        left = 55
    elif(office[counter] == 'S'):
        right = left = 55
    else:
        red_seen = False

    return left, right, red_seen

def exitGracefully():
    print("Terminating ev3 operation")
    exit()

# main Loop runs here
def main():

    # Initialize motors and sensors connections
    cur_sensors = sensors.ev3Sensors()
    cur_motors = motors.RobotMotors()

    # Initialize communications server and current command
    com_server = communications.Communicator()
    com_server.listen()
    command_dealer = commands.Command()

    # Initialize logger class
    cur_logger = logger.Logger(DEBUG)

    # Initialize navigation variables
    red_time = current_time = 0
    red_seen = False
    lasterror = error = integral = prevcourse = counter = course = 0
    office = []
    previous_command = ""

    try:
        # Start operation loop
        while(1):
            # Firstly retrieve and deal with command
            temp_command = com_server.getCurrentCommand()
            iteration_command = command_dealer.dealWithCommand(temp_command)

            # Act on the active_command
            if(iteration_command == "stop"):
                cur_motors.stop()
                if(previous_command != "stop"):
                    cur_logger.kill()
                counter = 0
                previous_command = "stop"
                continue

            elif(iteration_command == "start"):
                office = command_dealer.getCurrentPath()
                if(previous_command != "start"):
                    cur_logger.initialize(office)   # Init logging function
                previous_command = "start"

            elif(iteration_command == "test"):
                cur_sensors.calibrate(cur_motors)
                command_dealer.dealWithCommand("stop")
                previous_command = "test"
                continue

            # Get countersensor values
            color,[left,mid,right] = cur_sensors.getSensorData()

            # RED is seen only once
            if (color == 'red'):
                red_seen = True

                # While in red stay here
                while(color == 'red'):
                    color,[left,mid,right] = cur_sensors.getSensorData()
                    prevcourse = 0
                counter+=1

            # Yellow is seen
            elif(color == 'yellow'):
                cur_motors.waiting()
                time.sleep(5)
                cur_motors.runTimed()
            # Otherwise do what was being done before
            else:
                if(red_seen):
                    left, right, red_seen = checkCurrentIntersection(office, counter, left, right, red_seen)
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors, counter, cur_logger)
                else:
                    red_time = current_time
                    prevcourse = operate(left, mid, right, lasterror, integral, prevcourse, office, cur_motors, counter, cur_logger)

    # If user kills program
    except KeyboardInterrupt:
        com_server.die()
        cur_motors.stop()
        exitGracefully()

######### --MAIN-- ##########
if __name__ == "__main__":
    args = sys.argv[1:]

    global AFTER_TIMER
    global PREV_TIMER

    # Check if debugging is on
    global DEBUG
    if "--debug" in args:
        DEBUG = True
    else:
        DEBUG = False

    # Check if fast speed is needed
    global FAST
    if "--fast" in args:
        FAST = True
    else:
        FAST = False

    PREV_TIMER = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("Ev3 is starting...")
    print("\n")
    main()
