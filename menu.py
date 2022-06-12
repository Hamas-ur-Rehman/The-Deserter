import os
import sys
from credits import credit
sys.path.append('./startgame')
from startgame import start


def menu():
    os.system('cls')

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
    if choice == "1":
        start()
    elif choice == "2":
        credit()
    elif choice == "3":
        quit()
    
