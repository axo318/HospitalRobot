import sys
sys.path.append("..")

from libraries import function

while(1):
    sensorAvg = input("Insert input >> ")
    leftside, rightside = function.getOutput(float(sensorAvg))
    print("Left side power is: "+ str(leftside))
    print("Right side power is: "+ str(rightside))
