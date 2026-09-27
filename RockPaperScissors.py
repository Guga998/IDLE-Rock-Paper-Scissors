import random

choices = ["rock", "paper", "scissors"]

while True:
    print("\nRock, Paper, Scissors")
    choice = input("Choose your weapon (rock/paper/scissors or q to quit): ").lower()

    if choice == "q":
        print("Goodbye!")
        break

    if choice not in choices:
        print("Invalid choice. Try again.")
        continue

    pc_choice = random.choice(choices)
    print(f"Computer chose: {pc_choice}")

    if choice == pc_choice:
        print("Draw")
    elif (choice == "rock" and pc_choice == "scissors") or \
         (choice == "scissors" and pc_choice == "paper") or \
         (choice == "paper" and pc_choice == "rock"):
        print("You Win!")
    else:
        print("You lost!")