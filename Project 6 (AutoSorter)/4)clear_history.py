import os
import sys
from termcolor import colored

# Set console color and clear screen
os.system('color')
os.system('cls' if os.name == 'nt' else 'clear')

# Prompt user to clear history
a = input("Enter any key to clear history: " )

try:
    # Open history file in write mode to clear it
    with open(r'3)history.txt', 'w') as w:
        w.write('')
except Exception as e:
    # Handle any errors
    print((colored(f"\nError: {e}", 'red')))
    g = input("\nPress any key to exit...")
    sys.exit()
else:


