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
slow_f_a = 100
slow_f_m = -0.1
slow_f_c = 0

fast_f_a = 38
fast_f_m = -0.04
fast_f_c = 61

# Reverse Function Variables#
slow_r_a = 200
slow_r_m = -0.02
slow_r_c = -50

fast_r_a = 200
fast_r_m = -0.025
fast_r_c = -20

# Maximum and minimum power limits
maximum = 99
minimum = -99

def getOutput(courseValue, fast):
    f_a = slow_f_a
    f_m = slow_f_m
    f_c = slow_f_c

    r_a = slow_r_a
    r_m = slow_r_m
    r_c = slow_r_c

    if(fast):
        f_a = fast_f_a
        f_m = fast_f_m
        f_c = fast_f_c

        r_a = fast_r_a
        r_m = fast_r_m
        r_c = fast_r_c

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
