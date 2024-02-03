import webbrowser as wb
import pyfiglet
import os
from termcolor import colored
import sys


# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the header/banner
def header():
    print('-' * 70)
    banner = pyfiglet.figlet_format("Site Opener").upper()
    print(colored(banner.rstrip("\n"), 'red', attrs=['bold']))
    print(colored("     -by prajesh8484     \n", 'yellow', attrs=['bold']))
    print('-' * 70)

# Function to display the application options and open selected sites
def app():
    print("\nHello! Welcome to Site Opener...\n")
    print("Press (1) for YouTube")
    print("Press (2) for Google Meet")
    print("Press (3) for Gmail")

    num = input("Enter the command: ")

    if num == '1':
        wb.open('https://youtube.com/', new=1)
        print(colored("\nSite opened in background!", 'green'))
    elif num == '2':
        wb.open('https://meet.google.com/', new=1)
        print(colored("\nSite opened in background!", 'green'))
    elif num == '3':
        wb.open('https://accounts.google.com/b/0/AddMailService', new=1)
        print(colored("\nSite opened in background!", 'green'))
    else:
        print(colored("\nPlease enter valid numbers from instructions\n", 'red'))

# Function to handle exiting or rerunning the program
def exzt():
    key = input('Thanks for using the code! Enter (y) to run again or any key to quit: ')
    
    if key.lower() == 'y':
        runloop()
    else:
        sys.exit()

# Main loop to keep the program running
def runloop():
    while True:
        clear_screen()
        header()
        app()
        exzt()

# Run the program
if __name__ == "__main__":
    clear_screen()
    runloop()
