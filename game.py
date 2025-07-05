import random
import time
import os
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

SYMBOLS = ['@', '#', '$', '%', '&', '*', '!', '?', '^', '~']

def play_game():
    print("Welcome to MIND MAZE!")
    print("Memorize the sequence of symbols.")
    print("You have 3 seconds to remember each sequence.")
    print("Type the exact sequence to proceed to the next level.\n")
    input("Press ENTER to start...")

    level = 1
    high_score = 0

    while True:
        clear_screen()
        print(f"Level: {level}")
        sequence = [random.choice(SYMBOLS) for _ in range(level)]

   
        print("Memorize this sequence:")
        print(" ".join(sequence))
        time.sleep(3)

        clear_screen()
        guess = input("Enter the sequence (symbols separated by space): ").strip().split()

        if guess == sequence:
            print("Correct! Proceeding to next level...")
            level += 1
            high_score = level-1
            time.sleep(1.5)
        else:
            print("Wrong sequence!")
            print(f"The correct sequence was: {' '.join(sequence)}")
            print(f" Your highest level: {high_score}")
            break

    print("\nThanks for playing Mind Maze!")
    play_again = input("Do you want to try again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        sys.exit()


if __name__ == "__main__":
    play_game()
