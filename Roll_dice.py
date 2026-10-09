import random


def roll_dice():
    print("=" * 40)
    print("🎲  WELCOME TO THE INFINITE DICE ROLLER  🎲")
    print("=" * 40)

    while True:
        user_input = input("\nRoll the dice? (Y/N): ").strip()

        if user_input in ["y", "Y"]:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)

            print("\nRolling...")
            print(f"🎲 Die 1: {die1}")
            print(f"🎲 Die 2: {die2}")
            print(f"✨ Total: {die1 + die2}")

            if die1 == die2:
                print("🎉 DOUBLES!")

        elif user_input in ["n", "N"]:
            print("\nThanks for playing! Goodbye! 👋")
            break

        else:
            print("❌ Invalid input. Please enter 'Y' to roll or 'N' to stop.")


if __name__ == "__main__":
    roll_dice()


