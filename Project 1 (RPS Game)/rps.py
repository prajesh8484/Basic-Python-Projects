import random
import pyfiglet
import os
import sys
from termcolor import colored

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the game header/banner
def header():
    print('-' * 70)
    ascii_banner = pyfiglet.figlet_format("RPS game").upper()
    print(colored(ascii_banner.rstrip("\n"), 'red', attrs=['bold']))
    print(colored("     -by prajesh8484      \n", 'yellow', attrs=['bold']))
    print('-' * 70)

# Play the Rock-Paper-Scissors game
def play_game():
    while True:
        clear_screen()
        header()

        user_action = input("* Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]

        if user_action not in possible_actions:
            print(colored("\nPlease choose a valid option (rock, paper, or scissors).\n", 'red'))
            continue
        
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"\n-Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("\n-Rock smashes scissors! You win!")
            else:
                print("\n-Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("\n-Paper covers rock! You win!")
            else:
                print("\n-Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("\n-Scissors cuts paper! You win!")
            else:
                print("\n-Rock smashes scissors! You lose.")

        play_again = input("\n# Play again? (y/n): ")
        if play_again.lower() != "y":
            sys.exit()

if __name__ == "__main__":
    play_game()
