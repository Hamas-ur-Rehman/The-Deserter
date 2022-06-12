lines = ["Welcome to the game!",
         "You have been drafted to the US Army.",         
         ]


import os
from time import sleep
import sys
import winsound
import pygame


def start():
    
    
    os.system('cls')
    print("   _    _      _                            _          _   _                                       ")
    print("  | |  | |    | |                          | |        | | | |                                      ")
    print("  | |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___    __ _  __ _ _ __ ___   ___ ")
    print("  | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \\")
    print("  \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | (_| | (_| | | | | | |  __/")
    print("   \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|  \__, |\__,_|_| |_| |_|\___|")
    print("                                                                         __/ |                     ")
    print("                                                                        |___/                      ")
    global Name
    global Age 
    global rank
    Age = 18
    rank = "Private"
    Name = input("Enter your name: ")
    pygame.mixer.music.load("./sounds/thunderrain.mp3")
    option = pygame.mixer.Sound("sounds/gun.mp3")

    pygame.mixer.music.play(-1)
    winsound.PlaySound(r'./sounds/typewriter.wav', winsound.SND_ASYNC)
    os.system('cls')
    for line in lines:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.1)          # wait a little to make the effect look good.
        print('')  
    winsound.PlaySound(None, winsound.SND_PURGE)
    print('\n')
    print('''   
    YOUR BIO DATA:

              ::                        Name: {}    
             -**-                       Age:{}
            -+==++                      rank: {}
           =++++++*.                    
         :*=+++*+++*-         
        +*==+**+#+++**.       
      =#+==+#=  :*++++*+.     
    =#+==+**:     =*+==+*+.   
  =#*+=++*-        .+*++++*=. 
 -#=++++-            :+*++++# 
 -#+*+:                :*#**# 
 =#=.                    :=#+ 
    '''.format(Name,Age,rank))

    input("Press enter to continue")   
    pygame.mixer.Sound.play(option)
    os.system('cls')

