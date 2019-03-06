Ev3home folder contains all ev3 files
The operate.py script sends the arguments as commands to control the robot

-- DIRECTIONS FOR ROBOT USE -- (QaA)

1) How to turn on the robot?
  A) Press the middle ev3 button until the light goes green
  
2) How to start the robot functionality/server
  A) Go to terminal,
      ssh robot@192.168.105.102 (password:maker)
      python3 main_white_line.py
      (if we need logs enabled: python3 main_white_line.py --debug)
      (if we need fast speed: python3 main_white_line.py --fast)
      (if both are needed: python3 main_white_line.py --fast --debug)
      
3) How to control the robot remotely?
  A) Get GammaTech/Movement/operate.py anywhere on personal dice
      python3 operate.py "start a"  (to start robot towards path a)
      python3 operate.py "stop"     (to stop robot and reset path)
      
4) How to customize path a?
  A) Go to the robot home folder (ssh into it as shown before)
      nano ~/libraries/commands.py
      and then edit the list named "officeA" with the following commands:
        L - Left turn
        R - Right turn
        S - Straight turn
        U - List must start with U, and it must also follow any of the three commands above
        e.g. ["U","L","U","R","U","S"]
