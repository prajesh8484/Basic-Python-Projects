import pyfiglet
import sys
from termcolor import colored
from time import sleep
import os

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner maker
def aciimaker():
    clear_screen()
    print('-' * 70)
    ascii_banner = pyfiglet.figlet_format("A C I I banner").upper()
    print(colored(ascii_banner.rstrip("\n"), 'red', attrs=['bold']))
    print(colored("     -by prajsh8484      \n", 'yellow', attrs=['bold']))
    print('-' * 70)
    
    text = input("\nEnter Your Text: ")
    color = input("Enter Your Colour (grey, red, green, yellow, blue, magenta, cyan, white): ")
    colorlist = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    baner = pyfiglet.figlet_format(f"{text}").upper()

    def makebanner():
        print(colored(baner.rstrip("\n"), color, attrs=['bold']))

    if color.lower() in colorlist:
        makebanner()
    else:
        print(colored("ERROR: Please choose a color from the following list:", 'red'))
        print(colored("(--grey, red, green, yellow, blue, magenta, cyan, white)", 'yellow'))

# Ending message
def ending():
    print("\n\nThanks for using the code :)\n")
    a = input("Do you want to run the program again? (y for yes) (any key for no): ")
    if a.lower() == 'y':
        return True
    else:
        print("Exiting Program...")
        sleep(3)
        sys.exit()

# Main loop
def runloop():
    while True:
        aciimaker()
        if not ending():
            break

if __name__ == "__main__":
    runloop()
