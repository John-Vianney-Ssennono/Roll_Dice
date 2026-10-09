import random  # Import the random module for generating random numbers

# Function to simulate rolling two dice indefinitely until the user decides to stop


def roll_dice():
    print("=" * 40)  # Print a line of equal signs for visual separation
    # Print the welcome message for the dice roller
    print("🎲  WELCOME TO THE INFINITE DICE ROLLER  🎲")
    print("=" * 40)  # Print a line of equal signs for visual separation

    while True:  # Loop indefinitely until the user decides to stop
        user_input = input("\nRoll the dice? (Y/N): ").strip()

        if user_input in ["y", "Y"]:  # Check if the user wants to roll the dice
            die1 = random.randint(1, 6)  # Roll the first die
            die2 = random.randint(1, 6)  # Roll the second die

            print("\nRolling...")  # Indicate that the dice are being rolled
            print(f"🎲 Die 1: {die1}")  # Print the result of the first die
            print(f"🎲 Die 2: {die2}")  # Print the result of the second die
            print(f"✨ Total: {die1 + die2}")  # Print the total of both dice

            if die1 == die2:
                print("🎉 DOUBLES!")

        elif user_input in ["n", "N"]:
            print("\nThanks for playing! Goodbye! 👋")
            break

        else:  # Handle invalid input from the user
            # Prompt the user to enter a valid input
            print("❌ Invalid input. Please enter 'Y' to roll or 'N' to stop.")


if __name__ == "__main__":  # Check if the script is being run directly
    roll_dice()  # Call the roll_dice function to start the game
