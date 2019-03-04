#
#   The Function used for distributing the power to the motors is held here
#   Returns touple for left,right power level
#

import math


# Funcion Variables y = a * 1/(1 + e^(m*x)) + c
# a -> function coefficient
# m -> input multiplier in the exponent (should be negative)
# c -> function offset

# Forward Function Variables#
f_a = 100
f_m = -0.07
f_c = 0

# Reverse Function Variables#
r_a = 200
r_m = -0.02
r_c = -50

# Maximum and minimum power limits
maximum = 99
minimum = -99

def getOutput(courseValue):
    # Going left (positive value)
    if courseValue >= 0:
       rightside = -1*((f_a/(1 + (math.exp(float(f_m) * courseValue)))) + f_c)
       leftside = -1*((r_a/(1 + (math.exp(float(r_m) * -1 * courseValue)))) + r_c)
    # Going right (negative value)
    else:
       leftside = -1*((f_a/(1 + (math.exp(float(f_m) * -1 * courseValue)))) + f_c)
       rightside = -1*((r_a/(1 + (math.exp(float(r_m) * courseValue)))) + r_c)

    # Make sure the power range stays within wanted limits
    if(leftside > maximum):
        leftside = maximum
    if(rightside > maximum):
        rightside = maximum

    if(leftside < minimum):
        leftside = minimum
    if(rightside < minimum):
        rightside = minimum

    return leftside, rightside
