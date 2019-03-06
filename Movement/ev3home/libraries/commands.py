

class Command():

    def __init__(self):
        self.active_command = "stop"
        self.current_path = []

        # All predetermined locations
        # REDO
        self.officeA = ['U','L','U','L','U']

    def dealWithCommand(self, temp_command):
        # New non-none is found so update the active
        if(temp_command != None):
            print(temp_command)
            command_list = temp_command.split(" ")
            pre = command_list[0]

            if(pre == "stop"):
                self.active_command = pre
            elif(pre == "start"):
                self.active_command = pre
                self.current_path = self.getPath(command_list[1])
            elif(pre == "test"):
                self.active_command = pre

        return self.getActiveCommand()

    def getActiveCommand(self):
        return self.active_command

    def getCurrentPath(self):
        return self.current_path

    def getPath(self, letter):
        # if(letter == "a"):
        return self.officeA
