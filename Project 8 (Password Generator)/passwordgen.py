import os
import pyfiglet
import random
from termcolor import colored
import sys

os.system('color')
os.system('cls')

def show_info():
    print('-'*70)
    banner = pyfiglet.figlet_format("PASSWORD GENERATOR").upper()
    print((colored(banner.rstrip("\n"), 'red', attrs=['bold'])))
    print((colored("     -by PRAJESH      \n", 'yellow', attrs=['bold'])))
    print('-'*70)
    print("\nGenerate custom passwords!")


def main():
    len = int(input("Enter length of your password: "))
    print(f"\n1.For only (lowercase) password")
    print(f"2.For (lowercase + numbers) password")
    print(f"3.For only (uppercase) password")
    print(f"4.For (uppercase + numbers) password")
    print(f"5.For (lowercase + uppercase) password")
    print(f"6.For (lowercase + uppercase + numbers) password")
    print(f"7.For (lowercase + uppercase + symbols) password")
    print(f"8.For (lowercase + uppercase + symbols + numbers) password")
    choice = int(input("\nEnter your choice: "))
    if(choice>8):
        print((colored("\nError!", 'red')))

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'l','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    symbols = ['~', '!', '@', '#', '$', '%', '^','&', '*', '_', '-', ';','?', '>', '.']

    nums = ['1','2','3','4','5','6','7','8','9','0']

    if (choice == 1):
        pas = random.sample(alpha, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))
    elif (choice == 2):
        arr = alpha + nums
        pas = random.sample(arr, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))        
    elif (choice == 3):
        pas = random.sample(Alpha, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))
    elif (choice == 4):
        arr = Alpha + nums
        pas = random.sample(arr, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))        
    elif (choice == 5):
        arr = Alpha + alpha
        pas = random.sample(arr, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))        
    elif (choice == 6):
        arr = Alpha + alpha + nums
        pas = random.sample(arr, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))        
    elif (choice == 7):
        arr = Alpha + alpha + symbols
        pas = random.sample(arr, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))        
    elif (choice == 8):
        arr = Alpha + alpha + nums + symbols 
        pas = random.sample(arr, len)
        Pass = "".join(pas)
        print(f"\nYour Password is:",end=" ")
        print((colored(f"{Pass}\n", 'yellow')))

def exet():
    choice = input("\nThanks for using the code. Press 'y' to run again or any other key to exit:")
    if choice == 'y':
        runloop()
    else:
        sys.exit()

def runloop():
    os.system('cls')
    show_info()
    main()
    exet()

runloop()
