import os
import pyfiglet
from termcolor import colored
import sys
import wikipedia

os.system('color')
os.system('cls')

# Function to display banner
def show_info():
    print('-'*70)
    banner = pyfiglet.figlet_format("GET INFO").upper()
    print((colored(banner.rstrip("\n"), 'red', attrs=['bold'])))
    print((colored("     -by PRAJESH      \n", 'yellow', attrs=['bold'])))
    print('-'*70)
    print("\nA project to search something")

def app():
    print((colored("Please enter exact words for example: Python (Programming language), Alex (name)", 'cyan')))
    name = input("\nEnter your query: ").strip()
    try:
        result = wikipedia.summary(f"{name}", sentences=5, auto_suggest=False)
        print('')
        print('-'*70,'>\n')
        print(result)
        print('')
        print('-'*70,'>')
    except Exception as e:
        print((colored(f"\nError! : {e}", 'red')))
        exet()

def exet():
    choice = input("\nThanks for using the code. Press 'y' to run again or any other key to exit:")
    if choice == 'y':
        run_loop()
    else:
        sys.exit()

def run_loop():
    os.system('cls')
    show_info()
    app()
    exet()


if __name__ == "__main__":
    run_loop()

