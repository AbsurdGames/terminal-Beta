from imports import *
from pygameWindow import X, Y, backgroundColor, pygameText, txtSize, window

_ = ">>> "

platformOptions = """"
    platform.version
    platform.system
    platform.architecture
    platform.java_ver
    platform.python_compiler
    platform.python_version
    platform.processor
    platform.release"""

answer = ""
line = 0

help2 = """
Commands:
    platform: (platform.[option])
    |   version
    |   system
    |   architecture
    |   java_version
    |   python_compiler
    |   python_version
    |   processor
    |   release

    clear:
    |   clear --> clears all, but not the terminal title
    |   clear.all --> clears all
        
    history --> Show the commands history
    
    quit/exit --> exit the terminal
    
    ip --> Shows your IP
    
    https://www.[web] --> Opens the web
    
    echo:
    |   echo.repeat --> Shows what you typed on the echo and you can repeat more times
    |   echo.echo --> Shows what you typed
    |   echo.pin --> Pin a word that you type
    |   echo.unpin --> Unpin the pin that you typed before

    date & time:
        date/time --> Show the date and time
        timeFormat --> You can change the time format
    
    math --> Calculator (shell version) 
    
    random generator --> You can do a costum random generator
    
    create window --> You can create a window

"""

credits = """
Programing: Paul Cannon Palacios
Help: Pau Cava de las Heras
Tutorials: GeeksForGeeks and StackOverflow
"""

nextVersion = """
In the next version there will be:
    [STILL NO PLANS]
    
"""

history = []

platformVersion = platform.version()
platformSystem = platform.system()
platformArchi = platform.architecture()
platformJava = platform.java_ver()
platformPipCompiler = platform.python_compiler()
platformPipVersion = platform.python_version()
platformProcesor = platform.processor()
platformRel = platform.release()

timeH = datetime.datetime.now()
timeMin = datetime.datetime.now()
timeSec = datetime.datetime.now()

day = datetime.datetime.now()
month = datetime.datetime.now()
year = datetime.datetime.now()
format = "DD/MM/YYYY"
timeFormat = "24h"

echoCount = 0

hostName = socket.gethostname()
yourIP = socket.gethostbyname(hostName)

pin = ""

title="""
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ██████╗ ███████╗████████╗ █████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ██████╔╝█████╗     ██║   ███████║
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ██╔══██╗██╔══╝     ██║   ██╔══██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗    ██████╔╝███████╗   ██║   ██║  ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝

By Paul Cannon Palacios
Beta 1.2.1
Copyright ©2022

Type help(), credits() or versions(), nextVersion() for more info...
"""

def intError():
    print (Fore.RED + "Needs to be an integer (number)")

def titleTXT():
    print (Fore.RED + title + Fore.WHITE)

titleTXT()

while True:
    answer = input(_)
    
    if pin != "":
        print ("📌 ", pin)
    
    line += 1
    history.extend(answer)

    if answer == "help()":
        print (Fore.CYAN + help2, Fore.WHITE)
        
    elif answer == "credits()":
        print (credits)

    elif answer == "platform":
        print ("You have these options:")
        print (platformOptions)

    elif answer == "platform.version":
        print ("    Version", platformVersion)
        
    elif answer == "platform.system":
        print ("    System", platformSystem)
        
    elif answer == "platform.archi" or answer == "platform.architecture":
        print ("    Shell Architecture", platformArchi)

    elif answer == "platform.java" or answer == "java_ver" or answer == "platform.java_version":
        print ("    Java version", platformJava)

    elif answer == "platform.pipCompiler" or answer == "platform.python_compiler":
        print ("    Python compiler", platformPipCompiler)
        
    elif answer == "platform.Version" or answer == "platform.version":
        print ("    Python version", platformVersion)
        
    elif answer == "platform.pythonVersion" or answer == "platform.python_version":
        print ("    Python version", platformPipVersion)
        
    elif answer == "platform.procesor" or answer == "platform.processor":
        print ("    Python Procesor", platformProcesor)

    elif answer == "platform.rel" or answer == "platform.release":
        print ("    Release", platformRel)

    elif answer == "platform.ALL":
        print (_, "Version", platformVersion)
        print ("    System", platformSystem)
        print ("    Shell Architecture", platformArchi)
        print ("    Java version", platformJava)
        print ("    Python compiler", platformPipCompiler)
        print ("    Python version", platformVersion)
        print ("    Python version", platformPipVersion)
        print ("    Python Procesor", platformProcesor)
        print ("    Release", platformRel)

    elif answer == "history":
        print (history)

    elif answer.lower() == "clear":
        try:
            os.system("clear")
            os.system("printf '\033c'")

            titleTXT()

        except Exception as E2:
            print ("Can't clear by an error")
            print ("Error:")
            print (E2)

    elif answer.lower() == "clear.all":
        try:
            os.system("clear")
            os.system("printf '\033c'")

        except Exception as E2:
            print ("Can't clear by an error")
            print ("Error:")
            print (E2)

    elif answer.lower() == "quit" or answer.lower() == "exit":
        quit()

    elif answer == "ip":
        print (_, "Your host name is:")
        print (hostName)
        
        print (_, "Your IP is:")
        print (_, yourIP)

    elif "https://www." in answer:
        print ("Opening", answer,"...")
        
        webbrowser.open(answer) 
        
        print ("Done!")

    elif answer == "echo.repeat":
        answer = input (">>> Set echo to?")
        echoCount = int(input (">>> How many echos?"))
        
        while echoCount >= 0:
            print (answer)
            
            echoCount -= 1
            
            time.sleep(0.01)
        
    elif answer == "echo.echo":
        answer = input (">>> Set echo to?")
        
        print (answer)
        
    elif answer == "echo.unpin":
        pin = ""

    elif answer == "math":
        def _math_():
            global d1, d2
            global totalOperation, mathDone
            
            try:
                d1 = int(input("Digit 1"))
            
            except:
                intError()
                
            operation = ("Operations avadable: +, -, /, //, *, ^ or %")
            
            try:
                d2 = int(input("Digit 2"))

            except:
                intError()

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

    elif answer == "random number generator" or answer == "random generator":
        r1 = int(input("Number 1"))
        r2 = int(input("Number 2"))
        
        randomVar = random.randint(r1, r2)
        
        print ("-->", randomVar)

    elif answer.lower() == "create window":
        answer = "start"

        while True:
            answer = input(">>> Geometry, background color, text, text size, quit/exit or start")

            if answer.lower() == "geometry":
                X = int(input(">>> Geometry X"))
                Y = int(input(">>> Geometry Y"))

            elif answer.lower() == "background color" or answer.lower() == "color" or answer.lower() == "background":
                answer = input (">>> IN RBG!")

                backgroundColor = answer

            elif answer.lower() == "text":
                answer = input (">>> What text")

                pygameText = answer

            elif answer.lower() == "text size" or answer.lower() == "size":
                try:
                    txtSize = int(input("Set the text size, MUST HAVE NUMBERS"))
                    
                    if txtSize > 1:
                        print ("DONE! The text size its to ", txtSize)

                    elif txtSize <= 1:
                        print ("The text can't be smaller or equal than 1")

                except:
                    intError()

            elif answer.lower() == "start":
                try:
                    window()

                except:
                    print (Fore.RED + "There was an error opening the window")

            elif answer.lower() == "exit" or answer.lower() == "quit":
                break

    elif answer == "echo.pin":
        pin = input(">>> pin your message (Leave in blank to delete it or type #delete)")
        
        if answer.lower() == "#delete":
            pin = ""

    elif answer == "":
        print ("")
    
    else:
        if "#" not in answer:
            print (Fore.RED + _, "Error in line ", line," There is no command called", answer)
            print (_, "Type help() to get help of the commands")
            print (Fore.WHITE + "")
