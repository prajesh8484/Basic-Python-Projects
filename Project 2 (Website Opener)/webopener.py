import webbrowser as wb
import pyfiglet
import os
from termcolor import colored
import sys

os.system('color')
os.system('cls')

def runloop():
    codn = True
    while codn == True:
        header()
        app()
        exzt()

def header():
    print('-'*70)
    banner = pyfiglet.figlet_format("Site Opener").upper()
    print((colored(banner.rstrip("\n"), 'red', attrs=['bold'])))
    print((colored("     -by prajesh8484     \n", 'yellow', attrs=['bold'])))
    print('-'*70)



def app():
    print("\nHello! welcome to site opener...\nPress(1) for Youtube")
    print("Press(2) for Google meet")
    print("Press(3) for Gmail")

    num = input("Enter the command: ")

    if num == '1':
        wb.open('https://youtube.com/', new=1)
        print((colored("\nSite opened in background!", 'green')))
    elif num == '2':
        wb.open('https://meet.google.com/', new=1)
        print((colored("\nSite opened in background!", 'green')))
    
    elif num == '3':
        wb.open('https://accounts.google.com/b/0/AddMailService', new=1)
        print((colored("\nSite opened in background!", 'green'))
    
    else:
        print((colored("\nPlease enter numbers from instructions\n", 'red')))

def exzt():
    key = input('Thanks for using the code! enter (y) to run again or any key to quit: ')
    
    if key=='y' or key=='Y':
        runloop()
    else:
        sys.exit()
