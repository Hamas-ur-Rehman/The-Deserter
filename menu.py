import os

import sys
import pygame
from credits import credit
sys.path.append('./startgame')
from startgame import start
from playsound import playsound


def menu():
    os.system('cls')
    pygame.init()
    pygame.mixer.music.load("sounds/menu.wav")
    option = pygame.mixer.Sound("sounds/gun.mp3")
 
    pygame.mixer.music.play(-1)




    print("              )        (           (         (                (     ")
    print("    *   )  ( /(        )\ )        )\ )      )\ )  *   )      )\ )  ")
    print("  ` )  /(  )\()) (    (()/(   (   (()/( (   (()/(` )  /( (   (()/(  ")
    print("   ( )(_))((_)\  )\    /(_))  )\   /(_)))\   /(_))( )(_)))\   /(_)) ")
    print("  (_(_())  _((_)((_)  (_))_  ((_) (_)) ((_) (_)) (_(_())((_) (_))   ")
    print("  |_   _| | || || __|  |   \ | __|/ __|| __|| _ \|_   _|| __|| _ \  ")
    print("    | |   | __ || _|   | |) || _| \__ \| _| |   /  | |  | _| |   /  ")
    print("    |_|   |_||_||___|  |___/ |___||___/|___||_|_\  |_|  |___||_|_\  ")
    print("                                                                    ")
    print("      ___  ___ _____ _   _ _   _ ")
    print("     |  \/  ||  ___| \ | | | | |")
    print("     | .  . || |__ |  \| | | | |")
    print("     | |\/| ||  __|| . ` | | | |")
    print("     | |  | || |___| |\  | |_| |")
    print("     \_|  |_/\____/\_| \_/\___/ ")
    print("                             ")
    print("                             ")
    print("     1: Start game\n")
    print("     2: Credits\n")
    print("     3: Quit\n")
    choice = input("        Enter your choice: ")
    pygame.mixer.music.stop()
    if choice == "1":
        pygame.mixer.Sound.play(option)
        
        start()
    elif choice == "2":
        pygame.mixer.Sound.play(option)

        credit()
    elif choice == "3":
        pygame.mixer.Sound.play(option)

        quit()
    
