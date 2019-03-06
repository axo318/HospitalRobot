#
#   Class that deals with operation logs
#   This is going to work only if the debugging option is enabled
#

import os
import sys
import time


class Logger:
    # Constructor
    def __init__(self, debug):
        self.debug = debug
        self.startTime = None
        self.curOfficePath = []
        self.curLogPath = ""
        self.openedFile = None
        self.idNum = None

    # Init in the beginning of every path
    def initialize(self, office):
        if (self.debug):
            self.startTime = time.clock_gettime(time.CLOCK_MONOTONIC)
            self.curOfficePath = office
            self.curLogPath = self.getCurrentLogPath()
            self.openedFile = open(self.curLogPath, 'w')
            self.idNum = 0

    # Closes the current logger if stop command is issued
    def kill(self):
        self.curOfficePath = []
        self.curLogPath = ""
        if(self.openedFile != None):
            self.openedFile.close()
        self.idNum = None

    # Main logging functionality
    def log(self, course, sensorVals, motorVals, counterVals):
        if(self.debug and self.openedFile != None):
            c = ","
            s = "|"
            perc = counterVals[0]/len(self.curOfficePath)
            line = str(self.idNum) +s+ str(round(course,2)) +s+ str(sensorVals[0])+c+str(sensorVals[1])+c+str(sensorVals[2]) +s+ str(round(motorVals[0],1))+c+str(round(motorVals[1],1)) +s+ str(counterVals[0])+c+counterVals[1] +s+ str(round(perc,2)) + "\n"
            self.openedFile.write(line)
            self.idNum += 1

    # Helper
    def getCurrentLogPath(self):
        prev_files = os.listdir("logs")
        cur_log_num = 0
        for f in prev_files:
            if "log_" in f:
                cur_log_num += 1
        return "logs/log_" + str(cur_log_num) + ".txt"
