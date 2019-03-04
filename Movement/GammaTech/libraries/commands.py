

class Command():

    def __init__(self):
        self.active_command = "stop"
        self.current_path = []

        # All predetermined locations
        self.officeA = ['L','L','L','R','R', 'L', 'L', 'L']
        self.officeTestL = ['L','L', 'S', 'L', 'S', 'L', 'S', 'L', 'S', 'L', 'S', 'L', 'S', 'L', 'S']
        self.officeTestR = ['R', 'R', 'S', 'R', 'S', 'R', 'S', 'R', 'S', 'R', 'S', 'R', 'S', 'R', 'S']
        self.officeDemo = ['R', 'L', 'S', 'L', 'S', 'R', 'S', 'S', 'S', 'R', 'S'] 
                           #'R', 'S', 'L', 'S', 'L', 'S', 'R', 'S']

    def dealWithCommand(self, temp_command):
        command_list = temp_command.split(" ")
        pre = command_list[0] 

        if(pre == "stop"):
            self.active_command = pre
        elif(pre == "start"):
            self.active_command = pre
            self.current_path = self.getPath(command_list[1])

        #return self.active_command

    def getActiveCommand(self):
        return self.active_command

    def getCurrentPath(self):
        return self.current_path

    def getPath(self, letter):
        if(letter == "a"):
            return self.officeA
        elif(letter == "L"):
            return self.officeTestL
        elif(letter == "R"):
            return self.officeTestR
        elif(letter == "Demo"):
            return self.officeDemo
