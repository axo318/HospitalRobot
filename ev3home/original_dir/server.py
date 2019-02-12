#!/usr/bin/python3.4
import socket
import os

#variables
host = "192.168.105.102"
port = 9999

# Command to be saved
currentCommand = "stop"


# Methods
#---------------------------------------------------------------#

# Start the functionality
def start():
    print("Main is starting...")
    os.system('python3 /home/robot/main.py')

# Stop robot functionality
def stop():
    print("Main is stopping")

# Checks the incoming_str for containing command and applies it
def assignCurCommand(incoming_str):
    if("start" in incoming_str):
        currentCommand = "start"
        start()
    elif("stop" in incoming_str):
        currentCommand = "stop"
        stop()

# Waits for incoming connection and saves the command on a variable
def waitForPacket():
    # Define socket as ipv4 and tcp
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print(data)
        assignCurCommand(str(data))
        if not data:
            break

# MAIN
#--------------------------------------------------------------------#

def main():
    print("Server is starting")
    while(1):
        waitForPacket()


if __name__ == "__main__":
    main()
