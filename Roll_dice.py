Run the script:

python dice_roller.py


💻 Sample Code

Here is a simple implementation of the project logic:

import random

def roll_dice():
    print("🎲 Welcome to the Infinite Dice Roller! 🎲\n")
    
    while True:
        user_choice = input("Do you want to roll the dice? (y/n): ").strip().lower()
        
        if user_choice == 'y':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"You rolled a {die1} and a {die2} (Total: {die1 + die2})\n")
        elif user_choice == 'n':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.\n")

if __name__ == "__main__":
    roll_dice()
