# Import necessary libraries
import os
import pyfiglet
from termcolor import colored
import sys
from datetime import datetime

os.system('color')

# Display program information
def show_info():
    print('-' * 70)
    banner = pyfiglet.figlet_format("Auto sorter").upper()
    print(colored(banner.rstrip("\n"), 'red', attrs=['bold']))
    print(colored("     -by PRAJESH      \n", 'yellow', attrs=['bold']))
    print('-' * 70)
    print(colored("• A miniproject to sort your list :)", 'cyan'))

# Get total number of elements from user
def get_number_of_elements():
    while True:
        try:
            num = int(input("\nEnter total number of elements in your list: "))
            return num
        except ValueError:
            print(colored("\nError! Please enter an integer.", 'red'))

# Get list elements from user
def get_list(num):
    print('')
    user_list = [input(f"Enter your element no.{n}: ") for n in range(1, num + 1)]
    return user_list

# Sort list in ascending order
def sort_list_ascending(lst):
    return sorted(lst)

# Save sorted list to file
def save_output_to_file(lst):
    with open('2)output.txt', 'w') as file:
        for element in lst:
            file.write(f"{element}\n")
    print(colored("\n» Output Pasted on output.txt Successfully!", 'green', attrs=['bold']))

# Record sorted list in history file
def make_history(lst):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date = now.strftime("%d/%m/%y")
    formatted_string = f"\n{date}  {current_time}\n\n"

    with open(r'3)history.txt', 'a') as history_file:
        history_file.write(formatted_string)

        for element in lst:
            history_file.write(f"{element}\n")

        history_file.write('-' * 70)

# Main function to run the program
def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    show_info()

    total_elements = get_number_of_elements()
    user_list = get_list(total_elements)

    sorted_list = sort_list_ascending(user_list)

    print("\n» Your output is:")
    for element in sorted_list:
        print(element)

    # Save output to file and record in history
    save_output_to_file(sorted_list)
    make_history(sorted_list)

    # Ask user if they want to run again
    choice = input("\nThanks for using the code. Enter 'y' to run again or press any key to exit:")
    if choice.lower() == 'y':
        main()
    else:
        sys.exit()

if __name__ == "__main__":
    main()

