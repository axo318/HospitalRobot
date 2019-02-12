# some utilities for conversion

import time
import ev3dev.ev3 as ev3

# Get time in milliseconds
def timestamp_now (): return int (time.time () * 1E3)


# fill in others here e.g.
# wheelTicsToMetres()
# driveForwardMetres(distance)