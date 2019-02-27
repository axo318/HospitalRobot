import sys
sys.path.insert(0, sys.path[0] + "/..")

from libraries import motors

cur_motors = motors.RobotMotors()

while(1):
    string = input("Insert left,right power >> ")
    [left, right] = string.split(",")
    cur_motors.moveDirect(-1*int(left), -1*int(right))
