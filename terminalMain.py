"""
Originaly Created by Paul Cannon Palacios
Code: Paul Cannon Palacios
Help: (from internet), Thanks to stack overflow and GeeksForGeeks!
ASCII art web: https://www.coolgenerator.com/ascii-text-generator
"""

import datetime
import platform
import random
import socket
import time
import webbrowser

import pygame
from colorama import Fore

pygame.init()

colorStyle = Fore.WHITE

count = 0

while count <= 50:
    print ()
    count += 1
    
title="""
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ██████╗ ███████╗████████╗ █████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ██████╔╝█████╗     ██║   ███████║
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ██╔══██╗██╔══╝     ██║   ██╔══██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    ██████╔╝███████╗   ██║   ██║  ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝
"""

print (Fore.LIGHTRED_EX + title)

print (Fore.WHITE + "Info:")
print ("    Help(), Copyright(), credits(), nextUpdatePlan()")
print ()

print (colorStyle)        

pin = ""

def program():
    global count
    global answer, echo, exit, windowReady, count1, timeSleep, defaultColorStyle
    global d1, d2, operation, totalOperation, mathDone
    global url, httpsWWW
    global timeSec
    global colorStyle
    
    count = 0

    answer = ""
    echo = ""
    exit = ""
    windowReady = False
    count1 = 0
    timeSleep = 0.1
    defaultColorStyle = Fore.WHITE

    d1 = 0
    d2 = 0
    operation = ""
    totalOperation = ""
    mathDone = False

    url = "https://www.google.com"
    httpsWWW = "https://www."

    r1 = 0
    r2 = 0
    randomVar = ""
    timeH = datetime.datetime.now()
    timeMin = datetime.datetime.now()
    timeSec = datetime.datetime.now()

    day = datetime.datetime.now()
    month = datetime.datetime.now()
    year = datetime.datetime.now()
    format = "DD/MM/YYYY"
    timeFormat = "24h"

    hostName = socket.gethostname()
    yourIP = socket.gethostbyname(hostName)

    pin = ""

    platformVersion = platform.version()
    platformSystem = platform.system()
    platformArchi = platform.architecture()
    platformJava = platform.java_ver()
    platformPipCompiler = platform.python_compiler()
    platformPipVersion = platform.python_version()
    platformProcesor = platform.processor()
    platformRel = platform.release()

    windowTXT = "[insert text in terminal]"
    
    def windowTXTDef():
        windowTXT = input("What text")

        if windowTXT.lower() == "[insert text in terminal]" or answer == "":
            print ("Can't be that text")
            
        else:
            print ("Text has been renamed to: ", windowTXT)


    def windowFunct():
        window = pygame.display.set_mode((X, Y), pygame.RESIZABLE)
        
        pygameFontDisplay = pygame.font.SysFont("orbitron", 50)

        text = pygameFontDisplay.render(windowTXT, False, (255, 255, 255))
            
        while True:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.display.quit()
                
            window.blit(text, (10, 10))
                
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    quit()
                    
    answer = input (">>>")

    if answer == "platform.version": 
        print (">>> Version", platformVersion)
        
    elif answer == "platform.system":
        print (">>> System", platformSystem)
        
    elif answer == "platform.archi" or answer == "platform.architecture":
        print (">>> Shell Architecture", platformArchi)

    elif answer == "platform.java":
        print (">>> Java version", platformJava)

    elif answer == "platform.pipCompiler":
        print (">>> Python compiler", platformPipCompiler)
        
    elif answer == "platform.Version":
        print (">>> Python version", platformVersion)
        
    elif answer == "platform.pythonVersion":
        print (">>> Python version", platformPipVersion)
        
    elif answer == "platform.procesor":
        print (">>> Python Procesor", platformProcesor)

    elif answer == "platform.rel" or answer == "platform.release":
        print (">>> Release", platformRel)
        
    elif answer == "set; colorStyle":
        colorStyle = input ("Avadable color styles: Green (1), white (2), black (3), yelow (4), blue (5), magenta (6) or grey (7)")
        
        if answer.lower() == "green" or answer == "1":
            colorStyle = Fore.GREEN
            
        elif answer.lower() == "white" or answer == "2":
            colorStyle = Fore.WHITE
        
        elif answer.lower() == "black" or answer == "3":
            colorStyle = Fore.BLACK

        elif answer.lower() == "yellow" or answer == "4":
            colorStyle = Fore.YELLOW
        
        elif answer.lower() == "blue" or answer == "5":
            colorStyle = Fore.BLUE
            
        elif answer.lower() == "magenta" or answer == "6":
            colorStyle = Fore.MAGENTA
        
        elif answer.lower() == "grey" or answer == "7":
            colorStyle = Fore.LIGHTBLACK_EX
            
        print (colorStyle)
            

        print ("\n>>>This is how it looks: ██")
        
    elif answer == "get ip":
        print (">>>Your host name is:")
        print (hostName)
        
        print (">>>Your IP is:")
        print (">>>", yourIP)
        print (">>> /!\ DO NOT SHARE IT WITH ANY ONE!")
            
    elif answer == "programMode":
        answer = ""
        
        while answer == "":
            answer = input (">>>")
            
            def quitProgramingMode():
                if answer == "exit = True":
                    print (">>> Quitted programing mode")
            
            if answer == "set; X, Y":
                Y = int(input(">>> Y"))
                X = int(input(">>> X"))
                
                if X <= 10:
                    print (">>> X can't be less than 10")
                    
                elif Y <= 10:
                    print (">>> Y can't be less than 10")
                
                else:
                    if windowReady == False:
                        print (">>> Window is not ready")
                        
                    elif windowReady == True:
                        print (">>> Window is now ready, start? Y/N")
                        
                        if answer.lower() == "no" or answer.lower() == "n":
                            print (">>> Abort")
                            
                        elif answer.lower() == "yes" or answer.lower() == "y":
                            print (">>> Loading window")

                            windowFunct()
                        
                    else:
                        answer = input (">>> WindowState is unknown, Start recovery? Y/N")
                        
                        if answer.lower() == "n" or answer.lower() == "no":
                            print (">>> Recomendation: Restart the terminal")
                            
                        elif answer.lower() == "y" or answer.lower() == "yes":
                            answer = input (">>>")
                            
                            if answer == "set; windowReady = False":
                                print (">>> Loading...")
                                
                                windowReady = False
                                
                                print (">>> The windowReady Var is set to ", windowReady)
                                
                            elif answer == "set; windowReady = True":
                                print (">>> Loading...")

                                windowReady = True
                                
                                print (">>> The windowReady Var is set to ", windowReady)
                                
            elif answer == "set; windowTXT":    
                windowTXTDef()
                
            elif answer == "if event = False":
                answer = input(">>>")
                
                if answer == "  set; event = True":
                    answer = input(">>>")
                    
                    if answer == "else_if event = True":
                        answer = input(">>>")
                        
                        if answer == "  set; event = event.selfVar":
                            windowReady = True
                            
                            Y = int(input(">>> Y"))
                            X = int(input(">>> X"))
                            
                            if X <= 10:
                                print (">>> X can't be less than 10")
                                
                            elif Y <= 10:
                                print (">>> Y can't be less than 10")
                            
                            print (">>> Window if now ready")
                            
                            windowFunct()
                            
                        elif answer == "  set; event = event.selfVar + set; windowTXT":
                            windowReady = True
                            
                            windowTXTDef()
                            
                            Y = int(input(">>> Y"))
                            X = int(input(">>> X"))
                            
                            if X <= 10:
                                print (">>> X can't be less than 10")
                                
                            elif Y <= 10:
                                print (">>> Y can't be less than 10")
                            
                            print (">>> Window if now ready")
                            
                            windowFunct()
                            
                        else:
                            print (Fore.RED + answer, "is not defined")
                            print (colorStyle)
                            
                    else:
                        print (Fore.RED + answer, "is not defined")
                        print (colorStyle)
                        
                else:
                    print (Fore.RED + answer, "is not defined")
                    print (colorStyle)
              
            else:
                print (Fore.RED + answer, "is not defined")
                print (colorStyle)
                
    elif answer == "set; echo.pin":
        pin = input(">>> #clear to clear pin or type something to pin ")
        
        print (">>> Pin set to ", pin)
                
        if pin == "#clear":
            pin = ""
            
        print ("Done")
        
    elif answer == "startProgram":
        print ("There is no program executed in the command line\nhelp() for more info")
                            
    elif answer == "echo":
        answer = input (">>> Set echo to?")
        echoCount = int(input (">>> How many echos?"))
        
        while echoCount >= 0:
            print (answer)
            
            echoCount -= 1
            
            time.sleep(0.01)
            
    elif answer.lower() == "joe mama":
        print (Fore.RED + "I HAVEE NOO FRIENDS!")
    
    elif answer == "exit" or answer == "quit" or answer == "close":
        #exit
        
        pygame.quit()
        quit()

    elif answer == "credits()":
        print (">>> By Paul Cannon Palacios")

    elif answer == "copyright()":
        print (">>> Absurd games ©2022")
        print ("    started: 9/06/2022")
        print ("    Beta: 11/06/2022")
        print ("    Release: ??/??/2022")
        
    elif answer == "help()":
        #help
        
        print (Fore.CYAN + ">>> Platform:")
        print ()
        print ("    platform.[version, system, archi (or) architecture, java, pipCompiler, pythonVersion, rel (or) release, verison]")
        print ()
        print ("set; colorStyle")
        print ()
        print ("createWindow")
        print ()
        print ("echo --> type something --> how many tymes")
        print ()
        print ("exit (or) quit")
        print ()
        print ("clear")
        print ()
        print ("math (Its like a very simple calculator)")
        print ()
        print ("random number generator (or) random number")
        print ()
        print ("open web --> Url")
        print ()
        print ("format --> change the format")
        print ()
        print ("time format --> change the time format")
        print ()
        print ("dateTime (or) date/time --> Show the tim")
        print ()
        print ("echo.pin [pin message]")
        print ()
        print ("set; colorStyle.Default")
        print ()
        print ("set; defaultColorStyle")
        print ()
        print ("FactoryReset --> Reset terminal")
        print ()
        print ("Use #(comment) to do a comment (or) do: (c)")
        print (colorStyle)
        
    elif answer == "":
        print ()
        
    elif answer == "set; colorStyle.Default":
        print ("Setting to default...")
        colorStyle = defaultColorStyle
        
    elif answer == "set; defaultColorStyle":
        defaultColorStyle = input ("Avadable color styles: Green (1), white (2), black (3), yelow (4), blue (5), magenta (6) or grey (7)")

        if answer.lower() == "green" or answer == "1":
            defaultColorStyle = Fore.GREEN
            
        elif answer.lower() == "white" or answer == "2":
            defaultColorStyle = Fore.WHITE

        elif answer.lower() == "black" or answer == "3":
            defaultColorStyle = Fore.BLACK

        elif answer.lower() == "yellow" or answer == "4":
            defaultColorStyle = Fore.YELLOW

        elif answer.lower() == "blue" or answer == "5":
            defaultColorStyle = Fore.BLUE
            
        elif answer.lower() == "magenta" or answer == "6":
            defaultColorStyle = Fore.MAGENTA

        elif answer.lower() == "grey" or answer == "7":
            defaultColorStyle = Fore.LIGHTBLACK_EX
            
    elif answer == "factoryReset" or answer == "factory reset":
        answer = input (Fore.RED + "Are you shure that you want to factory reset terminal? Y/N")
        
        if answer.lower() == "yes" or answer.lower() == "y":
            print ("Reseting settings to default...")
            
            program()
                
        elif answer.lower() == "no" or answer.lower() == "n":
            print (colorStyle + "Did NOT factory reset")
        
    elif answer == "timeFormat" or answer == "time format":
        print ("Do you want to change the time format?")
        answer = input ("Y/N")
        
        if answer.lower() == "n" or answer.lower() == "no":
            print ("Abort.")
            
        elif answer.lower() == "yes" or answer.lower() == "y":
            answer = input ("1. 24h\n2. 12h")
            
            if answer.lower() == "24h" or answer == "1":
                timeFormat = "24h"
                
            elif answer.lower() == "12h" or answer == "2":
                timeFormat = "12h"
                
            print ("Time format has been set to", timeFormat)
        
    elif answer == "math":
        def _math_():
            global d1, d2
            global totalOperation, mathDone
            
            d1 = int(input("Digit 1"))
            operation = str(input("Operations avadable: +, -, /, //, *, ^ or %"))
            d2 = int(input("Digit 2"))
            
            if "+" in operation:
                totalOperation = d1 + d2

            elif "-" in operation:
                totalOperation = d1 - d2
                
            elif "/" in operation:
                totalOperation = d1 / d2
                
            elif "//" in operation:
                totalOperation = d1 // d2
                
            elif "*" in operation:
                totalOperation = d1 * d2
                
            elif "^" in operation:
                totalOperation = d1 ^ d2
                
            elif "%" in operation:
                totalOperation = d1 % d2
                
            else:
                print ("Don't know that type of operation")
            
            print ("Result --> ", totalOperation)
            
            mathDone = input("Do you want to do more? Y/N")
            
            if mathDone.lower() == "y" or mathDone == "yes":
                mathDone = False
            
            elif mathDone.lower() == "n" or mathDone.lower() == "no":
                mathDone = True
                
            elif mathDone.lower() == "exit" or mathDone.lower() == "quit":
                quit()

            else:
                print ("That answer Dones not exist")
                
                mathDone = False
            
        while mathDone == False:
            _math_()
            
    elif answer == "random number generator" or answer == "random generator":
        r1 = int(input("Number 1"))
        r2 = int(input("Number 2"))
        
        randomVar = random.randint(r1, r2)
        
        print ("-->", randomVar)
            
    elif answer == "open web":
        url = input ("What web?")
        
        if 'https://www.' not in url:
            print ("Loading...")
            
        elif 'https://www.' in url:
            print ("Loading...")
                
        webbrowser.open(url)
        
        print ("Done!")
        
    elif answer == ".help()":
        print (Fore.RED + "There is no help argument\nDo help()")
        print (colorStyle)
        
    elif answer == "clock.help()":
        print (Fore.CYAN + ">>> Clock help:")
        print ("    How to change time: You can't realy change time, but you can add a costum time zone, pressing the (+) Button and typing a costum time zone, and there you have it!")
    
    elif answer == "terminal.help()":
        print (">>> type help()")
        
    elif answer == "format":
        print ("Your current format is: ", format)
        
        answer = input ("Change? Y/N?")
        
        if answer.lower() == "n" or answer.lower() == "no":
            print ("Abort.")
            
        elif answer.lower() == "y" or answer.lower() == "yes":
            answer = input ("1. DD/MM/YYYY\n2.MM/DD/YYYY\n3.YYYY/MM/DD")
            
            if answer.lower() == "dd/mm/yyyy" or answer.lower() == "1":
                format == "DD/MM/YYYY"
                
            elif answer.lower() == "mm/dd/yyyy" or answer.lower() == "2":
                format == "MM/DD/YYYY"

            elif answer.lower() == "yyyy/mm/dd" or answer.lower() == "3":
                format == "YYYY/MM/DD"
        
    elif answer == "date/time" or answer == "datetime" or answer == "dateTime":
        print (Fore.LIGHTMAGENTA_EX + "DateTime: Format:", format)
        
        if timeFormat == "24h":
            if format == "DD/MM/YYYY":
                print ("Hour", timeH.hour," Min", timeMin.minute)
                print ("Day", day.day,"Month", month.month,"Year", year.year)
            
            elif format == "MM/DD/YYYY":
                print ("Hour", timeH.hour," Min", timeMin.minute)
                print ("Month", month.month,"Day", day.day,"Year", year.year)
                
            elif format == "YYYY/MM/DD":
                print ("Hour", timeH.hour," Min", timeMin.minute)
                print ("Year", year.year,"Month", month.month,"Day", day.day)
            
        elif timeFormat == "12h":
            if format == "DD/MM/YYYY":
                print ("Hour", timeH.hour," Min", timeMin.minute)
                print ("Day", day.day,"Month", month.month,"Year", year.year)
            
            elif format == "MM/DD/YYYY":
                print ("Hour", timeH.hour," Min", timeMin.minute)
                print ("Month", month.month,"Day", day.day,"Year", year.year)
                
            elif format == "YYYY/MM/DD":
                print ("Hour", timeH.hour," Min", timeMin.minute)
                print ("Year", year.year,"Month", month.month,"Day", day.day)    
        
        print (colorStyle)
        
    elif answer == "nextUpdatePlan()":
        print (">>> Make a soundMaker")
        print ("    Fix bugs")
        print ("    Locate IP command line")
        print ("    Add commands: locate IP, program.[program], pinWeb")
        
    elif answer == "clear":
        count = 0
        
        while count <= 50:  
            print ()
            count += 1
            
    else:
        if "#" not in answer:
            print (Fore.RED + "Unknown command -->", answer)
            print ("Type Help() to get info of commands")
            print (colorStyle)

def updatePin():
    if pin != "":
        print ("📌PINED ECHO: ", pin)
    
while True:
    print (colorStyle)
    
    updatePin()
    program()
