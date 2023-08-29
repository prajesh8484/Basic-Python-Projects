import random
import os
import pyfiglet
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    clear_screen()
    print('-' * 70)
    ascii_banner = pyfiglet.figlet_format("Number Guessing Game").upper()
    print(colored(ascii_banner.rstrip("\n"), 'red', attrs=['bold']))
    print(colored("     -by PRAJESH      \n", 'yellow', attrs=['bold']))
    print('-' * 70)

def get_player_input(prompt):
    return input(prompt)

def display_message(message, color='white'):
    print(colored(message, color))

def play_number_guessing_game():
    secret_number = random.randint(1, 100)
    user_guess = None
    guesses = 0

    while user_guess != secret_number:
        user_guess = int(get_player_input("Enter your guess: "))
        guesses += 1

        if user_guess == secret_number:
            display_message("You guessed it right!", 'green')
        else:
            if user_guess > secret_number:
                display_message("You guessed it wrong! Enter a smaller number", 'red')
            else:
                display_message("You guessed it wrong! Enter a larger number", 'red')

    display_message(f"You guessed the number in {guesses} guesses")

    return guesses

def update_highscore(new_score):
    try:
        with open("hiscore.txt", "r") as f:
            current_highscore = int(f.read())
    except FileNotFoundError:
        current_highscore = float("inf")

    if new_score < current_highscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(new_score))
        display_message("Congratulations! You have a new high score!", 'yellow')


def ask_replay():
    replay = get_player_input("Do you want to play again? (y/n): ")
    return replay.lower() == 'y'


def main():
    while True:
        display_banner()
        player_name = get_player_input("Enter your name: ")
        num_guesses = play_number_guessing_game()
        update_highscore(num_guesses)
        display_message("Thanks for playing the Number Guessing Game!", 'cyan')
        
        if not ask_replay():
            break
if __name__ == "__main__":
    main()
