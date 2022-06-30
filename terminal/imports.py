#here there its the main import file
#what it does is to do the imports spread in to every file and if there is an error in the code, you enter a mini terminal to know whats happened...

try:
    import datetime
    import math
    import os
    import platform
    import random
    import socket
    import sys
    import time
    import webbrowser

    import pygame
    from colorama import Fore
    
    pygame.init()

except Exception as E:
    print ("Entering terminalN.I (No Imports)")

    help = """
    imports -> Show the imports that they use
    install -> Help to install python modules
    quit or exit -> Quit the program
    echo.error -> shows the error that there is in the modules
    """

    imports =  """
    pygame
    platform
    sys
    random
    datetime
    colorama (Fore)
    os
    webbrowser
    time
    socket
    math
    """

    print ("Done")

    while True:
        answer = input("/")

        if answer == "imports":
            print ("Imports:")
            print (imports)

        elif answer.lower() == "help":
            print (help)

        elif answer == "install":
            answer = input("What are you using? macOS, windows, other")

            if answer.lower() == "macos":
                print ("Go to spotlight search -> type Terminal -> go there and type -> pip3 (Python 3) or pip (Python 2) (Its better to install with pip3 because its the last version of python) install {package or module name}")
                print ("Example: pip3 install pygame <- This is the module to be installed")
                print ("And now it should be installing!")

            elif answer.lower() == "windows":
                print ("Go to search -> type cmd -> go there and type -> pip3 (Python 3) or pip (Python 2) (Its better to install with pip3 because its the last version of python) install {package or module name}")
                print ("Example: pip3 install pygame <- This is the module to be installed")
                print ("And now it should be installing!")

            elif answer.lower() == "other":
                print ("Search for the terminal that you use -> go there and type -> pip3 (Python 3) or pip (Python 2) (Its better to install with pip3 because its the last version of python) install {package or module name}")
                print ("Example: pip3 install pygame <- This is the module to be installed")
                print ("And now it should be installing!")

            print ("NOTE: All the python commands are for every OS (it allways starts with pip3 (or pip) install {package}), if you are not sure the module that there is an error, type echo.error (type help)")

        elif answer.lower() == "quit" or answer.lower() == "exit":
            quit()

        elif answer == "echo.error":
            print (E)
