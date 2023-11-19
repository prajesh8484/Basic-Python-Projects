import os
import pyfiglet
from termcolor import colored
import random
import sys

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the banner
def showinfo():
    print('-' * 70)
    banner = pyfiglet.figlet_format("O T P  T E S T").upper()
    print(colored(banner.rstrip("\n"), 'red', attrs=['bold']))
    print(colored("     -by prajesh8484      \n", 'yellow', attrs=['bold']))
    print('-' * 70)
    print("\nA test project to make simple OTP verification")

# Main OTP verification logic
def app():
    name = input("\nEnter your name: ").strip()
    print(f"Please check your inbox for OTP")
    
    # Generate and save OTP to file
    otp = random.randint(1000, 9999)
    with open('inbox.txt', 'w') as f:
        f.write(f"Dear {name}, [{otp}] is your one-time password (OTP) for verification")
    
    user_otp = input("\nEnter your OTP: ").strip()
    try:
        user_otp = int(user_otp)
    except ValueError:
        print(colored("\nError! Incorrect OTP format. Please enter numbers only.", 'red'))
    else:
        if user_otp == otp:
            clear_screen()
            banner = pyfiglet.figlet_format("SUCCESS!").upper()
            print(colored(banner.rstrip("\n"), 'green', attrs=['bold']))
            print(colored("\nVerification successful!", 'green', attrs=['bold']))
        else:
            print(colored("\nError! Incorrect OTP. Please try again.", 'red', attrs=['bold']))

# Exiting the program
def exet():
    choice = input("\nThanks for using the code. Enter 'y' to run again or press any key to exit: ")
    if choice.lower() == 'y':
        runloop()
    else:
        sys.exit()

# Loop logic
def runloop():
    clear_screen()
    showinfo()
    app()
    exet()

if __name__ == "__main__":
    runloop()
